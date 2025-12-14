import requests
import allure
from data import Url, ResponseBody

class TestCreateUser:
    
    @allure.title('Test Successful new user creation. Handle:/api/auth/register')
    def test_create_new_user(self, generate_user_data):
        registration = requests.post(f'{Url.MAIN_URL}{Url.AUTH_REG}', json=generate_user_data[0])
        assert registration.status_code == 200 and registration.json()

    @allure.title('Test creation of two identical users error. Handle:/api/auth/register')
    def test_creation_user_clone_error(self, create_user_data):
        response_status = requests.post(f'{Url.MAIN_URL}{Url.AUTH_REG}', json=create_user_data[0])
        assert response_status.status_code == 403 and (response_status.json() == ResponseBody.EXISTING_USER)

    @allure.title('Test User Registration Deficit Data Error, Not enough: Email. Handle:/api/auth/register')
    def test_creation_user_deficit_data_error_email(self, create_user_no_email):
        response_status = requests.post(f'{Url.MAIN_URL}{Url.AUTH_REG}', json=create_user_no_email)
        assert response_status.status_code == 403 and (response_status.json() == ResponseBody.NOT_ENOUGH_DATA)

    @allure.title('Test User Registration Deficit Data Error, Not enough: Password. Handle:/api/auth/register')
    def test_creation_user_deficit_data_error_password(self, create_user_no_password):
        response_status = requests.post(f'{Url.MAIN_URL}{Url.AUTH_REG}', json=create_user_no_password)
        assert response_status.status_code == 403 and (response_status.json() == ResponseBody.NOT_ENOUGH_DATA)

    @allure.title('Test User Registration Deficit Data Error, Not enough: Name. Handle:/api/auth/register')
    def test_creation_user_deficit_data_error_email(self, create_user_no_name):
        response_status = requests.post(f'{Url.MAIN_URL}{Url.AUTH_REG}', json=create_user_no_name)
        assert response_status.status_code == 403 and (response_status.json() == ResponseBody.NOT_ENOUGH_DATA)