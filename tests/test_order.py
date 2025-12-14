import requests
import allure
from data import OrderBurger, Url, ResponseBody

class TestOrder:

    @allure.title('Make order with authorization. Handle: /api/orders')
    def test_make_auth_order(self, create_burger_data):
        login = create_burger_data[0]
        burger = OrderBurger.MY_BURGER
        headers = create_burger_data[4]
        response_status = requests.post(f'{Url.MAIN_URL}{Url.ORDER}', json=burger, headers=headers)
        assert response_status.status_code == 200
        
    @allure.title('Make order without authorization. Handle: /api/orders')
    def test_make_no_auth_order(self):
        burger = OrderBurger.MY_BURGER
        response_status = requests.post(f'{Url.MAIN_URL}{Url.ORDER}', json=burger)
        assert response_status.status_code == 200

    @allure.title('Make order with ingredients. Handle: /api/orders')
    def test_make_ingred_order(self, create_burger_data):
        login = create_burger_data[0]
        burger = OrderBurger.MY_BURGER
        headers = create_burger_data[4]
        response_status = requests.post(f'{Url.MAIN_URL}{Url.ORDER}', json=burger, headers=headers)
        assert response_status.status_code == 200

    @allure.title('Make order without ingredients. Handle: /api/orders')
    def test_make_no_ingred_order(self):
        burger = OrderBurger.EMPTY
        response_status = requests.post(f'{Url.MAIN_URL}{Url.ORDER}', json=burger)
        assert response_status.status_code == 400 and (response_status.json() == ResponseBody.NOT_ENOUGH_INGREDIENTS)

    @allure.title('Make order with invalid ingredients. Handle: /api/orders')
    def test_make_invalid_ingred_order(self):
        burger = OrderBurger.INVALID
        response_status = requests.post(f'{Url.MAIN_URL}{Url.ORDER}', json=burger)
        assert response_status.status_code == 500

    @allure.title('Make order with incorrect ingredients. Handle: /api/orders')
    def test_make_incorrect_ingred_order(self):
        burger = OrderBurger.INCORRECT
        response_status = requests.post(f'{Url.MAIN_URL}{Url.ORDER}', json=burger)
        assert response_status.status_code == 400 and (response_status.json() == ResponseBody.INCORRECT_INGREDIENT)