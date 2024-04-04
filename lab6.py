def Zadacha_1():
    countries_capitals = {
        "Россия": "Москва",
        "Франция": "Париж",
        "Германия": "Берлин",
        "Италия": "Рим",
        "Великобритания": "Лондон"
    }

    # Выведите на экран все пары ключ-значение
    for country, capital in countries_capitals.items():
        print(country, ":", capital)

    # Выведите на экран столицу для определенной страны
    country = "Россия"
    capital = countries_capitals[country]
    print("Столица", country, ":", capital)

    # Отсортируйте и выведите на экран содержимое словаря
    sorted_countries_capitals = sorted(countries_capitals)
    for country in sorted_countries_capitals:
        capital = countries_capitals[country]
        print(country, ":", capital)


def Zadacha_2():
    letter_values = {
        "А": 1, "В": 1, "Е": 1, "И": 1, "Н": 1, "О": 1, "Р": 1, "С": 1, "Т": 1,
        "Д": 2, "К": 2, "Л": 2, "М": 2, "П": 2, "У": 2,
        "Б": 3, "Г": 3, "Ё": 3, "Ь": 3, "Я": 3,
        "Й": 4, "Ы": 4,
        "Ж": 5, "З": 5, "Х": 5, "Ц": 5, "Ч": 5,
        "Ш": 8, "Э": 8, "Ю": 8,
        "Ф": 10, "Щ": 10, "Ъ": 10
    }

    word = input("Введите слово: ").upper()
    score = 0
    for letter in word:
        score += letter_values.get(letter, 0)
    print("Стоимость слова", word, ":", score, "очков")


