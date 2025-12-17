import requests
import allure
from data import OrderBurger, Url, ResponseBody

class TestOrder:

    @allure.title('Make order with authorization. Handle: /api/orders')
    def test_make_auth_order(self, create_burger_data):
        with allure.step("Подготовка данных для авторизованного заказа"):
            login = create_burger_data[0]
            burger = OrderBurger.MY_BURGER
            headers = create_burger_data[4]
            with allure.step("Отправка POST-запроса на создание заказа с авторизацией"):
                response_status = requests.post(f'{Url.MAIN_URL}{Url.ORDER}', json=burger, headers=headers)
                with allure.step("Проверка успешного статуса ответа 200"):
                    assert response_status.status_code == 200
        
    @allure.title('Make order without authorization. Handle: /api/orders')
    def test_make_no_auth_order(self):
        with allure.step("Подготовка данных для неавторизованного заказа"):
            burger = OrderBurger.MY_BURGER
            with allure.step("Отправка POST-запроса на создание заказа без авторизации"):
                response_status = requests.post(f'{Url.MAIN_URL}{Url.ORDER}', json=burger)
                with allure.step("Проверка успешного статуса ответа 200"):
                    assert response_status.status_code == 200

    @allure.title('Make order with ingredients. Handle: /api/orders')
    def test_make_ingred_order(self, create_burger_data):
        with allure.step("Подготовка данных заказа с ингредиентами"):
            login = create_burger_data[0]
            burger = OrderBurger.MY_BURGER
            headers = create_burger_data[4]
            with allure.step("Отправка POST-запроса на создание заказа с ингредиентами"):
                response_status = requests.post(f'{Url.MAIN_URL}{Url.ORDER}', json=burger, headers=headers)
                with allure.step("Проверка успешного статуса ответа 200"):
                    assert response_status.status_code == 200

    @allure.title('Make order without ingredients. Handle: /api/orders')
    def test_make_no_ingred_order(self):
        with allure.step("Подготовка данных заказа без ингредиентов"):
            burger = OrderBurger.EMPTY
            with allure.step("Отправка POST-запроса на создание заказа без ингредиентов"):
                response_status = requests.post(f'{Url.MAIN_URL}{Url.ORDER}', json=burger)
                with allure.step("Проверка статуса ошибки 400 и сообщения о недостающих ингредиентах"):
                    assert response_status.status_code == 400 and (response_status.json() == ResponseBody.NOT_ENOUGH_INGREDIENTS)

    @allure.title('Make order with invalid ingredients. Handle: /api/orders')
    def test_make_invalid_ingred_order(self):
        with allure.step("Подготовка данных для заказа с некорректными ингредиентами"):
            burger = OrderBurger.INVALID
            with allure.step("Отправка POST-запроса на создание заказа с некорректными ингредиентами"):
                response_status = requests.post(f'{Url.MAIN_URL}{Url.ORDER}', json=burger)
                with allure.step("Проверка статуса ошибки 500"):
                    assert response_status.status_code == 500

    @allure.title('Make order with incorrect ingredients. Handle: /api/orders')
    def test_make_incorrect_ingred_order(self):
        with allure.step("Подготовка данных для заказа с ошибочными ингредиентами"):
            burger = OrderBurger.INCORRECT
            with allure.step("Отправка POST-запроса на создание заказа с ошибочными ингредиентами"):
                response_status = requests.post(f'{Url.MAIN_URL}{Url.ORDER}', json=burger)
                with allure.step("Проверка статуса ошибки 400 и сообщения об ошибочных ингредиентах"):
                    assert response_status.status_code == 400 and (response_status.json() == ResponseBody.INCORRECT_INGREDIENT)