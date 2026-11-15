from Taxi import *
from User import *
from Order import *
from file import *
def find_user(user_id:int):
    for user in users:
        if user.id == user_id:
            return user
    return None
def main():
    taxi_db = File("taxi.csv")
    cars_lines = taxi_db.get_lines()
    for i in range(1,len(cars_lines)):
        car = cars_lines[i].strip().split(",")
        if len(car) == 5:
            new_taxi = Taxi(car[4],car[0],car[1],car[2])
            if car.lower() == "true":
                new_taxi.set_status(True)


    user_db = File("user.csv")
    user_lines = user_db.get_lines()
    for i in range(1,len(user_lines)):
        user_row = user_lines[i].strip().split(",")
        if user_row[0]:
            User(user_row[0])



    User("vlad")
    Taxi("a678po", "Alex", "red", "Opel")
    Taxi("a678oo", "Pol", "red", "Opel")
    Taxi("a678om", "Pol", "red", "Opel")
    show_all_users()
    show_all_taxi()
    while True:
        print("\n=== МЕНЮ УПРАВЛЕНИЯ ЗАКАЗАМИ ===")
        print("1. Создать заказ пользователю")
        print("2. Завершить активный заказ пользователя")
        print("3. Показать все такси")
        print("4. Показать всех пользователей")
        print("5. Добавить нового пользователя")
        print("0. Выход")
        choice = input("Выберите пункт меню: ")
        if choice == "1":
            show_all_users()
            try:
                user_id = int(input("Введите ID пользователя"))
                surrent_user = find_user(user_id)
                if not surrent_user:
                    print(f"Пользователь с таким {user_id} не найден")
                    continue
                depart = input("откуда").strip()
                destination = input("куда").strip()
                surrent_user.create_order(depart,destination)
            except ValueError:
                print("должно быть число")
            except NoFreeTaxiError as e:
                print(f"не удалось создать заказ {e}")
        elif choice == "2":
            show_all_users()
            try:
                user_id = int(input("Введите ID пользователя"))
                surrent_user = find_user(user_id)
                if not surrent_user:
                    print(f"Пользователь не найден")
                    continue
                surrent_user.finish_order()
            except ValueError:
                print("Ошибка: ID должен быть числом.")
        elif choice == "3":
            show_all_taxi()
        elif choice == "4":
            show_all_users()
        elif choice == "5":
            name = input("Введите имя нового пользователя")
            new_user = User(name)
            print(f"Добавлен {new_user}")
        elif choice == "0":
            print("Пока")
            break
        else:
            print("Неверный пункт меню, попробуйте снова.")

if __name__ == "__main__":
    main()