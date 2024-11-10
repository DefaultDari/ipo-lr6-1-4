# Написать программу, которая:
#- Запрашивает у пользователя строку для поиска.
#- Находит и выводит все строки, которые содержат искомую подстроку, а также их количество из следующего файла.
#- Сортирует найденные строки в порядке их длины (от самой короткой к самой длинной) и выводит их.

def find_and_sort_lines_with_substring(filename, substring):
    file =  open(filename, 'r', encoding='utf-8') # Открываем файл с учетом кодировки
    lines = file.readlines() # Читаем строки в файле
    substring = substring.lower() # Приводим подстроку к нижнему регистру для нечувствительности к регистру
    matching_lines = [line.strip() for line in lines if substring in line.lower()]  # Находим строки, содержащие подстроку, независимо от регистра
    print(f"\nКоличество строк, содержащих подстроку '{substring}': {len(matching_lines)}") #  Выводим количество найденных строк
    matching_lines.sort(key=len) # Сортируем строки по длине
    # Выводим отсортированные строки
    print("\nСтроки, содержащие подстроку, отсортированные по длине:")
    for line in matching_lines:
        print(line)
search_string = input("Введите строку для поиска: ") # Запрос строки для поиска
find_and_sort_lines_with_substring("C:\\Users\\agjjj\\Desktop\\text.txt", search_string) # Поиск и сортировка строк в указанном файле