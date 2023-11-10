import pytest
import json

pytestmark = pytest.mark.django_db


class TestCategoryEndpoints:
    endpoint = "/category/"

    def test_category_get_data(self, category_factory, api_client):
        category_factory.create_batch(4)

        response = api_client().get(self.endpoint)

        assert response.status_code == 200
        assert len(json.loads(response.content)) == 4


class TestBrandEndpoints:
    endpoint = "/brand/"

    def test_brand_get_data(self, brand_factory, api_client):
        brand_factory.create_batch(4)

        response = api_client().get(self.endpoint)

        assert response.status_code == 200
        assert len(json.loads(response.content)) == 4


class TestProductEndpoints:
    endpoint = "/product/"

    def test_product_get_data(self, product_factory, api_client):
        product_factory.create_batch(4)

        response = api_client().get(self.endpoint)

        assert response.status_code == 200
        assert len(json.loads(response.content)) == 4
