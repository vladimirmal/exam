import pytest
from exam_app.models import Products, Categories


@pytest.mark.django_db
def test_categories():
    Categories.objects.create(title="Test")
    category = Categories.objects.get(title="Test")
    assert category
