import requests
import allure
from data import Url

class TestCreateUser:
    @allure.title('Test Successful new user creation. Handle:/api/auth/login')
    def