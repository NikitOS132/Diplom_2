class Url:
    MAIN_URL = 'https://stellarburgers.education-services.ru/'
    AUTH_REG = 'api/auth/register'
    AUTH_LOG = 'api/auth/login'
    ORDER = 'api/orders'
    DEL_USER = 'api/auth/user'

class OrderBurger:
    MY_BURGER = {"ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa71"]}
    ANOTHER_BURGER = {"ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa70"]}
    EMPTY = {"ingredients": []}
    INVALID = {"ingredients": ["61c0c5a71d1f82001bdaaa6d", "aaah"]}
    INCORRECT = {"ingredients": ["60d3b41abdacab0026a733c6", "609646e4dc916e00276b2870"]}

class ResponseBody:
    EXISTING_USER = {'success': False, 'message': 'User already exists'}
    NOT_ENOUGH_DATA = {'success': False, 'message': 'Email, password and name are required fields'}
    INCORRECT_EMAIL_OR_PASSWORD = {'success': False, 'message': 'email or password are incorrect'}
    NOT_ENOUGH_INGREDIENTS = {'success': False, 'message': 'Ingredient ids must be provided'}
    INCORRECT_INGREDIENT = {'success': False, 'message': 'One or more ids provided are incorrect'}