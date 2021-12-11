import pytest

from test_api.base import ApiBase


@pytest.mark.API
class TestApiLogin(ApiBase):
    authorize = False

    def test_login(self, credentials):
        self.api_client.post_login(*credentials)


@pytest.mark.API
class TestApiCampaign(ApiBase):

    def test_create_campaign(self, get_random_name, logo_path):
        self.api_client.post_create_campaign(get_random_name, logo_path)


@pytest.mark.API
class TestApiSegment(ApiBase):

    def test_create_segment(self, get_random_name):
        self.api_client.post_create_segment(get_random_name)

    def test_delete_segment(self, get_random_name):
        self.api_client.post_delete_segment(get_random_name)
