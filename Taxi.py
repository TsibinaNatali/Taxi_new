#==========функция валидации номера такси
def validate_num(num:str):
    valid_alpha = 'etopakxcbm'
    if len(num) != 6: return False
    if (num[0] not in valid_alpha
        or num[4] not in valid_alpha
        or num[5] not in valid_alpha):
        return False
    if num[1].isdigit() and num[2].isdigit() and num[3].isdigit():
        return True
    return False
cars = set()

class Taxi:
    nums = set()
    def __init__(self,num,driver,color,model):
        if not validate_num(num):
            raise ValueError("не валидный гос. номер")
        if num in Taxi.nums:
            raise ValueError(f"номер {num} не уникален ")
        self.num = num
        self.driver = driver
        self.color = color
        self.model = model
        self.status = False
        Taxi.nums.add(num)
        cars.add(self)

    def set_status(self,status):
        self.status = status
    def __str__(self):
        return f"num: {self.num} | {self.driver} {self.color} {self.model} {self.status}"

def get_free_taxi():
    for i in cars:
        if not i.status:
            return i
    return None
def show_all_taxi():
    print("\n===АВТОПАРК===")
    if not cars:
        print("машин нет")
        return
    for car in cars:
        print(car)


