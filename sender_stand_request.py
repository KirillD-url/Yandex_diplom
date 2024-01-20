import configuration
import requests
import data

#Создаем заказ
def post_new_orders(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS_PATH,
                json=order_body,
                headers=data.headers)


#Сохраняем трек номер
def track_orders():
    response = post_new_orders(data.order_body)
    track = response.json()['track']
    return track


#Получаем заказ но трек номеру
def get_new_orders():
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDERS_PATH + str(track_orders()))