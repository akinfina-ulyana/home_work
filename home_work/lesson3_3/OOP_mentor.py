import math


# Task: 1
class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance

    def deposit(self, amount):
        """Пополнение счёта на указанную сумму."""
        if amount > 0:
            self.__balance += amount
        else:
            raise ValueError("Сумма пополнения должна быть положительной")

    def withdraw(self, amount):
        """Снятие средств со счёта."""
        if amount <= 0:
            raise ValueError("Сумма снятия должна быть положительной")
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            raise ValueError("Недостаточно средств на счёте")

    def get_balance(self):
        """Получение текущего баланса."""
        return self.__balance


my_ac = BankAccount()
my_ac.deposit(2323)
print(my_ac.get_balance())
my_ac.withdraw(23)
print(my_ac.get_balance())

# Task: 2
from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    @abstractmethod
    def get_info(self):
        """Абстрактный метод, который должен быть реализован в подклассах."""
        pass


class Developer(Employee):
    def __init__(self, name, position, salary, programming_language):
        super().__init__(name, position, salary)
        self.programming_language = programming_language

    def get_info(self):
        return f"Имя: {self.name}, Должность: {self.position}, Зарплата: {self.salary}, Язык: {self.programming_language}"


class Manager(Employee):
    def __init__(self, name, position, salary, employees: list = None):
        super().__init__(name, position, salary)
        self.employees = employees if employees is not None else []

    def get_info(self):
        """Возвращает информацию о менеджере, включая количество подчинённых."""
        return f"Имя: {self.name}, Должность: {self.position}, Зарплата: {self.salary}, Подчинённых: {len(self.employees)}"


# Task: 3
class Shape:
    def area(self):
        return 0

    def perimeter(self):
        return 0


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Площадь круга: π * radius²."""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Периметр круга (длина окружности): 2π * radius."""
        return 2 * math.pi * self.radius


shapes = [
    Rectangle(4, 5),
    Circle(3),
    Rectangle(2, 6),
    Circle(1)
]

for shape in shapes:
    print(f"Фигура: {type(shape).__name__}")
    print(f"Площадь: {shape.area():.2f}")
    print(f"Периметр: {shape.perimeter():.2f}")
    print("-" * 20)


# Task: 4
class Transport(ABC):
    @abstractmethod
    def start_engine(self):
        """Абстрактный метод запуска двигателя"""
        pass

    @abstractmethod
    def stop_engine(self):
        """Абстрактный метод остановки двигателя"""
        pass

    @abstractmethod
    def move(self):
        """Абстрактный метод движения транспорта"""
        pass


class Car(Transport):
    def __init__(self, model):
        self.model = model
        self.engine_running = False

    def start_engine(self):
        if not self.engine_running:
            self.engine_running = True
            return f"Автомобиль {self.model}: двигатель запущен"
        return f"Автомобиль {self.model}: двигатель уже работает"

    def stop_engine(self):
        if self.engine_running:
            self.engine_running = False
            return f"Автомобиль {self.model}: двигатель остановлен"
        return f"Автомобиль {self.model}: двигатель уже выключен"

    def move(self):
        if self.engine_running:
            return f"Автомобиль {self.model}: едет по дороге"
        return f"Автомобиль {self.model}: не может ехать, двигатель выключен"


class Boat(Transport):
    def __init__(self, name):
        self.name = name
        self.engine_running = False

    def start_engine(self):
        if not self.engine_running:
            self.engine_running = True
            return f"Лодка {self.name}: двигатель запущен"
        return f"Лодка {self.name}: двигатель уже работает"

    def stop_engine(self):
        if self.engine_running:
            self.engine_running = False
            return f"Лодка {self.name}: двигатель остановлен"
        return f"Лодка {self.name}: двигатель уже выключен"

    def move(self):
        if self.engine_running:
            return f"Лодка {self.name}: плывет по воде"
        return f"Лодка {self.name}: не может плыть, двигатель выключен"

# Task: 5
class Flyable:
    def fly(self):
        print("I'm flying!")


class Swimmable:
    def swim(self):
        print("I'm swimming!")


class Duck(Flyable, Swimmable):
    def make_sound(self):
        print("Quack!")


def main():
    duck = Duck()
    print("Демонстрация возможностей утки:")
    duck.fly()
    duck.swim()
    duck.make_sound()


# if __name__ == "__main__":
#     main()

# Task: 6
class Animal(ABC):

    @abstractmethod
    def __init__(self, sound, moovement):
        self.sound = sound
        self.moovement = moovement

    @abstractmethod
    def speak(self):
        return self.sound

    @abstractmethod
    def move(self):
        return self.moovement


class Dog(Animal):
    def __init__(self, sound='Woof!', moovement='running'):
        super().__init__(sound, moovement)

    def speak(self):
        print('this is Dog sound')
        print(self.sound)

    def move(self):
        print('I\'m running')


class Bird(Animal, Flyable):
    def __init__(self, sound='Tweet!', moovement='flying'):
        super().__init__(sound, moovement)

    def speak(self):
        print("This is bird sound")
        print(self.sound)

    def move(self):
        self.fly()


class Fish(Animal, Swimmable):
    def __init__(self, sound='', moovement='flying'):
        super().__init__(sound, moovement)

    def speak(self):
        print("This is fish sound")
        print(self.sound)

    def move(self):
        self.swim()


def main2():
    animals = [Dog(), Bird(), Fish()]

    for animal in animals:
        animal.speak()
        animal.move()
        print("---")


if __name__ == "__main__":
    main2()

# Task: 1
# Singleton
class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.logs = []
        return cls._instance

    def log(self, message: str):
        self.logs.append(message)

    def get_logs(self):
        return self.logs.copy()


logger1 = Logger()
logger2 = Logger()

print(logger1 is logger2)

logger1.log("Сообщение 1")
logger2.log("Сообщение 2")

print(logger1.get_logs())


# КЛАССЫ ДЕЛАЮТ ТОЛЬКО ОДНУ ВЕЩЬ, НО ДЕЛАЮТ ЕЁ ХОРОШО!!!

# class Report:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content
#     def generate_pdf(self):
#         print("PDF generated")
#     def save_to_file(self, filename):
#         print(f"Saved {filename}")
# # Task: 2
class ReportData:
    """хранение данных"""

    def __init__(self, data):
        self.data = data


class PDFGenerator:
    def generate(self, report_data: ReportData):
        print(f'Генерация PDF из данных: {report_data.data}')
        return "PDF-документ"


class FileSaver:
    def save(self, content, path):
        print(f"Сохранение {content} по пути: {path}")


data = ReportData({"title": "Annual Report", "values": [1, 2, 3]})

pdf_generator = PDFGenerator()
pdf_content = pdf_generator.generate(data)

file_saver = FileSaver()
file_saver.save(pdf_content, "/reports/save.pdf")

from abc import ABC, abstractmethod

# Task: 3
class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, amount: float) -> bool:
        """Оплата указанной суммы. Возвращает True при успехе."""
        pass


class PayPalProcessor(PaymentProcessor):
    def pay(self, amount: float) -> bool:
        print(f"Оплата через PayPal: ${amount:.2f}")
        return True


class CreditCardProcessor(PaymentProcessor):
    def pay(self, amount: float) -> bool:
        print(f"Оплата картой: ${amount:.2f}")
        return True


class CryptoProcessor(PaymentProcessor):
    def pay(self, amount: float) -> bool:
        print(f"Оплата криптовалютой  ${amount:.2f}")
        return True


from abc import ABC, abstractmethod

# Task: 4
class Bird(ABC):
    @abstractmethod
    def fly(self) -> str:
        pass

    @abstractmethod
    def make_sound(self) -> str:
        pass


class Sparrow(Bird):
    def fly(self) -> str:
        return "I believe i can fly, i believe i can touch the skyyyyyy!"

    def make_sound(self) -> str:
        return "Chik-chirik"


class Penguin(Bird):
    def fly(self) -> str:
        return "I cant fly. I can walk! and swim"

    def make_sound(self) -> str:
        return "AAAAAA AAAAA AAAA!"

# Task: 5
class Flyable(ABC):
    @abstractmethod
    def fly(self):
        pass


class Runnable(ABC):
    @abstractmethod
    def run(self):
        pass


class Swimmable(ABC):
    @abstractmethod
    def swim(self):
        pass


class Lion(Runnable):  # разделяем ответственность и не мучаем себя реализацией ненужного
    def run(self):
        return "Бегу по саванне!"

# Task: 6
class Temperature:
    def __init__(self, celsius: float):
        self._celsius = celsius

    @classmethod
    def from_fahrenheit(cls, fahrenheit: float):
        """Создает объект Temperature из градусов Фаренгейта"""
        celsius = (fahrenheit - 32) * 5 / 9
        return cls(celsius)

    @property
    def kelvin(self) -> float:
        """Возвращает температуру в Кельвинах (вычисляемое свойство)"""
        return self._celsius + 273.15

    @staticmethod
    def is_freezing(celsius: float) -> bool:
        """Проверяет, является ли температура точкой замерзания воды"""
        return celsius <= 0

    @property
    def celsius(self) -> float:
        """Геттер для температуры в °C."""
        return self._celsius

    @celsius.setter
    def celsius(self, value: float):
        """Сеттер для температуры в °C."""
        self._celsius = value
