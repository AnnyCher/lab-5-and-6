def Zadacha_1():
    numbers = [2, 5, 10, 7, 3]
    user_number = int(input("Введите число: "))

    if user_number in numbers:
        print("Поздравляю, Вы угадали число!")
    else:
        print("Нет такого числа!")

    print("Исходный список:", numbers)
    print("Число пользователя:", user_number)


def Zadacha_2():
    fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple']
    duplicates = []
    for item in fruits:
        if fruits.count(item) > 1 and item not in duplicates:
            duplicates.append(item)
    if len(duplicates) > 0:
        print("Найдены повторяющиеся элементы:", duplicates)
    else:
        print("Повторяющихся элементов нет")


def Zadacha_3():
    days_of_week = ("Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье")
    weekend_days = int(input("Сколько выходных дней на неделе вы хотите? "))
    your_weekend_days = days_of_week[-weekend_days:]
    your_working_days = days_of_week[:-weekend_days]
    print("Ваши выходные дни:", your_weekend_days)
    print("Ваши рабочие дни:", your_working_days)


def Zadacha_4():
    group1 = ["Алиева", "Ахмедова", "Балабан", "Бережная", "Боголюбова", "Власов", "Денисова", "Добродеева", "Ескина",
              "Зотова"]
    group2 = ["Гилязова", "Горбунов", "Думанов", "Епифанова", "Иванова", "Калинин", "Королева", "Криштал", "Крючкова",
              "Куклина"]
    team1 = tuple(group1[:5])
    team2 = tuple(group2[:5])
    combined_team = team1 + team2
    print("Группа 1:", group1)
    print("Группа 2:", group2)
    print("Спортивная команда:", combined_team)
    print("Длина команды:", len(combined_team))
    sorted_team = sorted(combined_team)
    print("Команда после сортировки:", sorted_team)
    student = "Иванов"
    print("Студент", student, "входит в команду:", student in combined_team)
    print("Количество повторений фамилии", student, "в команде:", combined_team.count(student))
