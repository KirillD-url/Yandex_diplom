import configuration
import requests
import data

#Создаем заказ
def post_new_orders(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS_PATH,
                json=order_body,
                headers=data.headers)


#Сохраняем трек-номер заказа
def save_order_track():
    order_response = post_new_orders(data.order_body)
    return order_response.json()['track']

#Получаем заказ по трек-номеру
def get_order_by_track(track_number):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDERS_PATH + str(track_number))