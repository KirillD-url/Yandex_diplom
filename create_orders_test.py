import sender_stand_request

# Дубровский Кирилл, 12-я когорта — Финальный проект. Инженер по тестированию плюс
#Автотест на проверку статуса заказа
def test_get_orders_by_track():
    respons = sender_stand_request.get_new_orders()
    assert respons.status_code == 200

