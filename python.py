name = "Иван"
age = 18

tools = [
    "Калькулятор",
    "Поиск файлов",
    "База данных",
]

tool = {
    "name": "Калькулятор",
    "purpose": "Выполнение расчётов",
}

if age >= 18:
    print("Возраст 18 или больше")
else:
    print("Возраст меньше 18")

for item in tools:
    print(item)

def add(a, b):
    return a + b

result = add(10, 5)
print("Результат:", result)