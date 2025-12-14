import pytest
import requests
import generators
from data import Url

@pytest.fixture
def generate_user_data():
    email = generators.email_generator()
    password = generators.password_generator()
    name = generators.name_generator()
    user_data_body = {'email': email, 'password': password, 'name': name}
    login_body = {'email': email, 'password': password}
    yield [user_data_body, login_body]
    login_user = requests.post(url= f'{Url.MAIN_URL}{Url.AUTH_LOG}', json=login_body)
    token = login_user.json().get('accessToken')
    headers = {"Authorization": f"Bearer {token}"}
    requests.delete(f'{Url.MAIN_URL}{Url.DEL_USER}', headers=headers)

@pytest.fixture
def create_user_data():
    email = generators.email_generator()
    password = generators.password_generator()
    name = generators.name_generator()
    user_data_body = {'email': email, 'password': password, 'name': name}
    login_body = {'email': email, 'password': password}
    requests.post(url= f'{Url.MAIN_URL}{Url.AUTH_REG}', json=user_data_body)
    login_user = requests.post(url= f'{Url.MAIN_URL}{Url.AUTH_LOG}', json=login_body)
    yield [user_data_body, login_body, email, password]
    token = login_user.json().get('accessToken')
    headers = {"Authorization": f"Bearer {token}"}
    requests.delete(f'{Url.MAIN_URL}{Url.DEL_USER}', headers=headers)

@pytest.fixture
def create_user_no_email():
    password = generators.password_generator()
    name = generators.name_generator()
    user_data_body = {'password': password, 'name': name}
    requests.post(url= f'{Url.MAIN_URL}{Url.AUTH_LOG}', json=user_data_body)
    yield [user_data_body]

@pytest.fixture
def create_user_no_password():
    email = generators.email_generator()
    name = generators.name_generator()
    user_data_body = {'email': email, 'name': name}
    requests.post(url= f'{Url.MAIN_URL}{Url.AUTH_LOG}', json=user_data_body)
    yield [user_data_body]

@pytest.fixture
def create_user_no_name():
    email = generators.email_generator()
    password = generators.password_generator()
    user_data_body = {'email': email, 'password': password}
    requests.post(url= f'{Url.MAIN_URL}{Url.AUTH_LOG}', json=user_data_body)
    yield [user_data_body]

@pytest.fixture
def create_burger_data():
    email = generators.email_generator()
    password = generators.password_generator()
    name = generators.name_generator()
    user_data_body = {'email': email, 'password': password, 'name': name}
    login_body = {'email': email, 'password': password}
    requests.post(url=f'{Url.MAIN_URL}{Url.AUTH_REG}', json=user_data_body)
    login_user = requests.post(url=f'{Url.MAIN_URL}{Url.AUTH_LOG}', json=login_body)
    token = login_user.json().get('accessToken')
    if token.startswith("Bearer "):
        token = token[7:]
    headers = {"Authorization": f"Bearer {token}"}
    yield [user_data_body, login_body, email, password, headers]
    requests.delete(f'{Url.MAIN_URL}{Url.DEL_USER}', headers=headers)