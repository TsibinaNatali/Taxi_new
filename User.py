from Order import *
from Taxi import Taxi

users = set()
class User:
    __user_count = 1
    def __init__(self,name:str):
        self.id = User.__user_count
        self.name = name
        self.__count_orders = 1
        self.order = None
        User.__user_count += 1
        users.add(self)
    def __str__(self):
        return f"пользователь {self.id}: {self.name} делает {self.__count_orders} заказ"

    @staticmethod
    def get_user_count():
        return User.__user_count - 1

    def create_order(self,depart:str,destination:str):
         if not self.order:
            self.order = Order(depart,destination,self.id)
            self.__count_orders += 1
            print(self.order)

    def finish_order(self):
        if self.order is None:
            print("у вас нет активного заказа")
            return
        self.order.taxi.set_status(False)
        self.order.status = False
        self.order = None
        print("поездка завершина")
def show_all_users():
    print("===Все пользователи===")
    if not users:
        print("пользователей нет")
        return
    for user in users:
        print(user)

