import sender_stand_request

# Дубровский Кирилл, 12-я когорта — Финальный проект. Инженер по тестированию плюс
#Автотест на проверку статуса заказа
def test_get_orders_by_track():
    track = sender_stand_request.save_order_track()
    response = sender_stand_request.get_order_by_track(track)
    assert response.status_code == 200

