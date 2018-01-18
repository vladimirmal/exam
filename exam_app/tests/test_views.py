import pytest
from django.contrib import auth
from django.contrib.auth.models import User


def create_test_user():
    u1 = User.objects.create_user(username='test', first_name='test',
                                  last_name='test', email='test@tests.ru',
                                  password='test')
    return u1


@pytest.mark.django_db
def test_main_page(client):
    response = client.get('/api/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_products(client):
    response = client.get('/api/products/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_basket(client):
    response = client.get('/api/basket/')
    assert response.status_code == 401
    create_test_user()
    client.post('/api-auth/login/?next=/api/', {'username': 'test', 'password': 'test'})
    responses = client.get('/api/basket/')
    assert responses.status_code == 200


@pytest.mark.django_db
def test_category(client):
    response = client.get('/api/category/')
    assert response.status_code == 200




