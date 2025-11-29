import pytest
import requests
import generators
from data import Url

@pytest.fixture
def generate_user_data(token=None):
    headers = {}
    if token:
        headers = {"Authorization": f"Bearer {token}"}
    email = generators.email_generator()
    password = generators.password_generator()
    name = generators.name_generator()
    user_data_body = {'email': email, 'password': password, 'name': name}
    login_body = {'email': email, 'password': password}
    yield [user_data_body, login_body]
    login_user = requests.post(url= f'{Url.MAIN_URL}{Url.AUTH_LOG}', json=login_body)
    if token and not token.startswith("Bearer "):
        token = f"Bearer {token}"
    requests.delete(f'{Url.MAIN_URL}{Url.DEL_USER}', headers=headers)

@pytest.fixture
def create_user_data(token=None):
    headers = {}
    if token:
        headers = {"Authorization": f"Bearer {token}"}
    email = generators.email_generator()
    password = generators.password_generator()
    name = generators.name_generator()
    user_data_body = {'email': email, 'password': password, 'name': name}
    login_body = {'email': email, 'password': password}
    requests.post(url= f'{Url.MAIN_URL}{Url.AUTH_LOG}', json=user_data_body)
    login_user = requests.post(url= f'{Url.MAIN_URL}{Url.AUTH_LOG}', json=login_body)
    yield [user_data_body, login_body, email, password]
    if token and not token.startswith("Bearer "):
        token = f"Bearer {token}"
    requests.delete(f'{Url.MAIN_URL}{Url.DEL_USER}', headers=headers)