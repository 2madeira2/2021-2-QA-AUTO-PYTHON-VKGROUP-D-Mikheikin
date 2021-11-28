import requests
import logging
from urllib.parse import urljoin
from resources import locations

MAX_RESPONSE_LENGTH = 500
MAX_CAMPAIGNS_SHOW = 200
MAX_SEGMENTS_SHOW = 200

logger = logging.getLogger('test')


class ResponseErrorException(Exception):
    pass


class ResponseStatusCodeException(Exception):
    pass


class InvalidLoginException(Exception):
    pass


class ApiClient:

    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()

    def get_token(self, user, password):
        location = 'https://auth-ac.my.com/auth'

        headers = self.post_headers
        headers.update({
            'Origin': 'https://target.my.com',
            'Referer': 'https://target.my.com/',
            'Content-Type': 'application/x-www-form-urlencoded'
        })

        data = {
            'email': user,
            'password': password,
            'continue': 'https://target.my.com/auth/mycom?state=target_login%3D1%26ignore_opener%3D1#email',
            'failure': 'https://account.my.com/login/'
        }

        self._request('POST', location, headers=headers, data=data, jsonify=False)

    def _request(self, method, location, headers=None, data=None, json=None, params=None, files=None,
                 expected_status=200, jsonify=True):
        url = urljoin(self.base_url, location)

        self.log_pre(method, url, headers, data, expected_status)
        if json is not None:
            response = self.session.request(method, url, headers=headers, json=json)
        else:
            response = self.session.request(method, url, headers=headers, data=data, params=params, files=files)
        self.log_post(response)

        if response.status_code != expected_status:
            raise ResponseStatusCodeException(f'Got {response.status_code} {response.reason} for URL "{url}"!\n'
                                              f'Expected status_code: {expected_status}.')

        if jsonify:
            json_response = response.json()
            return json_response
        return response

    @property
    def post_headers(self):
        return {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
            "Content-Type": "application/json",
        }

    def post_login(self, user, password):
        location = '/csrf/'

        self.get_token(user, password)
        csrftoken = self._request('GET', location, jsonify=False)

        return csrftoken

    def upload_content(self, headers, expected_status=200, image=None):
        logo_headers = headers
        logo_headers.pop('Content-Type')
        logo = {'file': ("logo.png", open(image, 'rb'), 'image/png')}
        request = self._request('POST', '/api/v2/content/static.json', headers=logo_headers, files=logo, jsonify=False)
        assert request.status_code == expected_status
        return request.json()['id']

    def post_create_campaign(self, name, logo_path, expected_status=200):
        location = locations.CREATE_CAMPAIGN_LOCATION

        headers = self.post_headers
        headers.update({
            'Referer': 'https://target.my.com/campaign/new',
            'X-CSRFToken': self.session.cookies.get('csrftoken')
        })

        url_id_request = self._request('GET', '/api/v1/urls/', params={'url': 'mail.ru'}, jsonify=False)
        assert url_id_request.status_code == expected_status
        url_id = url_id_request.json()['id']
        pic_id = self.upload_content(headers, image=logo_path)

        campaign_json = {
            "name": name,
            "objective": "traffic",
            "autobidding_mode": "second_price_mean",
            "mixing": "fastest",
            "package_id": 961,
            "banners": [{
                "urls": {
                    "primary": {
                        "id": url_id
                    }
                },
                "textblocks": {},
                "content": {
                    "image_240x400": {
                        "id": pic_id
                    }
                },
                "name": ""
            }]
        }
        campaign_id_request = self._request('POST', location, headers=headers, json=campaign_json, jsonify=False)
        assert campaign_id_request.status_code == expected_status
        campaign_id = campaign_id_request.json()['id']
        campaign_list_request = self._request('GET', location, params={'limit': MAX_CAMPAIGNS_SHOW}, jsonify=False)
        assert campaign_list_request.status_code == expected_status
        campaign_list = campaign_list_request.json()['items']

        assert campaign_id in [c['id'] for c in campaign_list]

        deleted_status = {'status': "deleted"}
        self._request('POST', f'/api/v2/campaigns/{campaign_id}.json', headers,
                      json=deleted_status, expected_status=204, jsonify=False)

    def post_create_segment(self, name):
        segment_id = self.create_segment(name)
        id_from_list = self.get_segment_id(segment_id)
        assert segment_id == id_from_list
        self.delete_segment_by_id(segment_id)

    def post_delete_segment(self, name):
        segment_id = self.create_segment(name)
        self.delete_segment_by_id(segment_id)
        id_from_list = self.get_segment_id(segment_id)

        assert segment_id != id_from_list

    @staticmethod
    def log_pre(method, url, headers, data, expected_status):
        logger.info(f'Performing {method} request:\n'
                    f'URL: {url}\n'
                    f'HEADERS: {headers}\n'
                    f'DATA: {data}\n\n'
                    f'expected status: {expected_status}\n\n')

    @staticmethod
    def log_post(response):
        log_str = 'Got response:\n' \
                  f'RESPONSE STATUS: {response.status_code}'

        if len(response.text) > MAX_RESPONSE_LENGTH:
            if logger.level == logging.INFO:
                logger.info(f'{log_str}\n'
                            f'RESPONSE CONTENT: COLLAPSED due to response size > {MAX_RESPONSE_LENGTH}. '
                            f'Use DEBUG logging.\n\n')
            elif logger.level == logging.DEBUG:
                logger.debug(f'{log_str}\n'
                             f'RESPONSE CONTENT: {response.text}\n\n')
        else:
            logger.info(f'{log_str}\n'
                        f'RESPONSE CONTENT: {response.text}\n\n')

    def get_segment_id(self, segment_id, expected_code=200):
        location = locations.GET_SEGMENT_ID_LOCATION
        segments_request = self._request('GET', location, params={'limit': MAX_SEGMENTS_SHOW}, jsonify=False)
        assert segments_request.status_code == expected_code
        segments = segments_request.json()
        segment_arr = [s['id'] for s in segments['items'] if s['id'] == segment_id]
        if not segment_arr:
            return None
        else:
            return segment_arr[0]

    def delete_segment_by_id(self, segment_id):
        location = locations.DELETE_SEGMENT_BY_ID_LOCATION + str(segment_id) + ".json"
        headers = self.post_headers
        headers.update({'X-CSRFToken': self.session.cookies.get('csrftoken')})

        self._request('DELETE', location, headers=headers, jsonify=False, expected_status=204)

    def create_segment(self, name, expected_status=200):
        location = locations.CREATE_SEGMENT_LOCATION

        headers = self.post_headers
        headers.update({
            "X-CSRFToken": self.session.cookies.get('csrftoken'),
        })

        json = {
            "name": name,
            "pass_condition": 1,
            "relations":
                [{
                    "object_type": "remarketing_player",
                    "params": {
                        "type": "positive",
                        "left": 365,
                        "right": 0
                    }
                }],
            "logicType": "or"
        }

        segment_id = self._request('POST', location, headers=headers, json=json, jsonify=False)
        assert segment_id.status_code == expected_status
        return segment_id.json()['id']
