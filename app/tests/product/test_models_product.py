import pytest

pytestmark = pytest.mark.django_db


class TestCategoryModel:
    def test_category_model_return_str(self, category_factory):
        data = category_factory(name="test_categ")
        assert data.__str__() == "test_categ"


class TestBrandModel:
    def test_brand_model_return_str(self, brand_factory):
        data = brand_factory(name="test_brand")
        assert data.__str__() == "test_brand"


class TestProductModel:
    def test_product_model_return_str(self, product_factory):
        data = product_factory(name="test_product")
        assert data.__str__() == "test_product"
