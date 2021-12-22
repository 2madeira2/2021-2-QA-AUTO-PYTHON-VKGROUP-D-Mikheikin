from mysql.models import RequestsCount, RequestTypeCount, MostFrequentRequest, Largest4xxRequest, UserWith5xxRequests


class MySQLBuilder:

    def __init__(self, client):
        self.client = client

    def create_requests_count(self, count):
        req_count = RequestsCount(count=count)
        self.client.session.add(req_count)
        return req_count

    def create_request_type_count(self, req_type, count):
        req_type_count = RequestTypeCount(req_type=req_type, count=count)
        self.client.session.add(req_type_count)
        return req_type_count

    def create_most_frequent_request(self, url, count):
        most_freq_req = MostFrequentRequest(url=url, count=count)
        self.client.session.add(most_freq_req)
        return most_freq_req

    def create_largest_4xx_request(self, url, size, ip):
        largest_4xx_req = Largest4xxRequest(url=url, size=size, ip=ip)
        self.client.session.add(largest_4xx_req)
        return largest_4xx_req

    def create_user_with_5xx_requests(self, ip, requests_number):
        user_with_5xx_reqs = UserWith5xxRequests(ip=ip, requests_number=requests_number)
        self.client.session.add(user_with_5xx_reqs)
        return user_with_5xx_reqs
