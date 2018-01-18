import pytest
from django.contrib import auth
from django.contrib.auth.models import User
from exam_app.serializers import BasketSerializers


def create_test_user():
    u1 = User.objects.create_user(username='test', first_name='test',
                                  last_name='test', email='test@test.ru',
                                  password='test')
    return u1


@pytest.mark.django_db
def test_register(client):
    create_test_user()
    client.post('/api/users/', {'username' : 'test', 'first_name' : 'test',
                                  'last_name' : 'test', 'email' : 'test@tests.ru',
                                  'password' : 'test'})
    obj = User.objects.get(username='test')
    assert obj
