import requests
import allure
import generators
from data import Url, ResponseBody

class TestLoginUser:
    
    @allure.title('Test successful user login, with complete login data. Handle:/api/auth/login')
    def test_successful_courier_login(self, create_user_data):
        with allure.step("Формирование данных для авторизации"):
            login_data = {'email': create_user_data[2], 'password': create_user_data[3]}
            with allure.step("Отправка POST-запроса на авторизацию пользователя"):
                response_status = requests.post(f'{Url.MAIN_URL}{Url.AUTH_LOG}', json=login_data)
                with allure.step("Проверка успешного статуса ответа 200"):
                    assert response_status.status_code == 200

    @allure.title('Test User Login Deficit Data Error with empty email. Handle:/api/auth/login')
    def test_user_login_empty_email_error(self, create_user_data):
        with allure.step("Формирование данных с пустым email"):
            data_response = {'email': '', 'password': create_user_data[3]}
            with allure.step("Отправка POST-запроса с пустым email"):
                response_status = requests.post(f'{Url.MAIN_URL}{Url.AUTH_LOG}', json=data_response)
                with allure.step("Проверка статуса ошибки 401 и сообщения о некорректных данных"):
                    assert response_status.status_code == 401 and (response_status.json() == ResponseBody.INCORRECT_EMAIL_OR_PASSWORD)

    @allure.title('Test User Login Deficit Data Error with empty password. Handle:/api/auth/login')
    def test_user_login_empty_password_error(self, create_user_data):
        with allure.step("Формирование данных с пустым паролем"):
            data_response = {'email': create_user_data[2], 'password': ''}
            with allure.step("Отправка POST-запроса с пустым паролем"):
                response_status = requests.post(f'{Url.MAIN_URL}{Url.AUTH_LOG}', json=data_response)
                with allure.step("Проверка статуса ошибки 401 и сообщения о некорректных данных"):
                    assert response_status.status_code == 401 and (response_status.json() == ResponseBody.INCORRECT_EMAIL_OR_PASSWORD)

    @allure.title('Test User Login Deficit Data Error with false email. Handle:/api/auth/login')
    def test_user_login_false_email_error(self, create_user_data):
        with allure.step("Генерация некорректного email и формирование данных"):
            data_response = {'email': generators.false_email_generator(), 'password': create_user_data[3]}
            with allure.step("Отправка POST-запроса с некорректным email"):
                response_status = requests.post(f'{Url.MAIN_URL}{Url.AUTH_LOG}', json=data_response)
                with allure.step("Проверка статуса ошибки 401 и сообщения о некорректных данных"):
                    assert response_status.status_code == 401 and (response_status.json() == ResponseBody.INCORRECT_EMAIL_OR_PASSWORD)

    @allure.title('Test User Login Deficit Data Error with false email. Handle:/api/auth/login')
    def test_user_login_false_password_error(self, create_user_data):
        with allure.step("Генерация некорректного пароля и формирование данных"):
            data_response = {'email': create_user_data[2], 'password': generators.false_password_generator()}
            with allure.step("Отправка POST-запроса с некорректным паролем"):
                response_status = requests.post(f'{Url.MAIN_URL}{Url.AUTH_LOG}', json=data_response)
                with allure.step("Проверка статуса ошибки 401 и сообщения о некорректных данных"):
                    assert response_status.status_code == 401 and (response_status.json() == ResponseBody.INCORRECT_EMAIL_OR_PASSWORD)