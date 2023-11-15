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

    def test_product_not_data_is_active_False(self, product_factory, api_client):
        product_factory.create(is_active=True)
        product_factory.create(is_active=True)

        # (is_active=False) is not seen in the endpoint
        product_factory.create(is_active=False)

        response = api_client().get(self.endpoint)

        assert response.status_code == 200
        assert len(json.loads(response.content)) == 2

    def test_product_get_all_products(self, product_factory, api_client):
        product_factory.create_batch(4)

        response = api_client().get(self.endpoint)

        assert response.status_code == 200
        assert len(json.loads(response.content)) == 4

    def test_return_single_product_by_name(self, product_factory, api_client):
        product_factory.create_batch(4)
        obj = product_factory.create(name="Product1-search-for-name-product")

        response = api_client().get(f"{self.endpoint}?product__name={obj.name}")

        assert len(json.loads(response.content)) == 5

    def test_return_filter_products_by_category_name(
        self, product_factory, category_factory, api_client
    ):
        product_factory.create_batch(4)
        catg_test = category_factory.create(name="category-test-filter")
        product_factory.create(category=catg_test)

        response = api_client().get(f"{self.endpoint}?category__name={catg_test.name}")

        assert len(json.loads(response.content)) == 1

    def test_return_filter_products_by_brand_name(
        self, product_factory, brand_factory, api_client
    ):
        product_factory.create_batch(4)
        brand_test = brand_factory.create(name="brand-test-filter")
        product_factory.create(brand=brand_test)

        response = api_client().get(f"{self.endpoint}?brand__name={brand_test.name}")

        assert len(json.loads(response.content)) == 1
