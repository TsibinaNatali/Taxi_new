import random
from Taxi import *

class NoFreeTaxiError(Exception):
    pass
class Order:
    id = 0
    def __init__(self,depart:str,destination:str,user_id:int):
        free_taxi = get_free_taxi()
        if free_taxi is None:
            raise NoFreeTaxiError("Свободных машин нет!")
        self.id = Order.id
        Order.id += 1
        self.depart = depart
        self.destination = destination
        self.user_id = user_id
        self.taxi = free_taxi
        self.taxi.set_status(True)
        self.price = random.randint(200,1000)
        self.status = True

    def __str__(self):
        return (f"Ваш маршрут из {self.depart} до {self.destination} "
                f"это ваш {self.user_id} заказ, к вам подъедет {self.taxi.num} {self.taxi.color} цвета стоимость поездки = {self.price}")
