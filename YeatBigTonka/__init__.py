# Напишите функцию, которая принимает на вход бинарную кучу и новый элемент, который нужно вставить. Функция должна вставить элемент в кучу и вернуть измененную кучу.
from YeatBigTonka.Algorithms.insert_into_heap import insert_into_heap

# Напишите функцию, которая принимает на вход массив целых чисел и сортирует его методом слияния.
from YeatBigTonka.Algorithms.merge_sort import merge_sort

# Напишите программу, которая запрашивает у пользователя строку и выводит на экран долю гласных букв в этой строке.
from YeatBigTonka.Algorithms.vowel_fraction import vowel_fraction

# Напишите программу, которая запрашивает у пользователя два комплексных числа в формате a + i*b и выводит на экран их сумму, разность и произведение в виде кортежа. Для решения этой задачи НЕЛЬЗЯ :) использовать встроенный тип данных complex.
from YeatBigTonka.Algorithms.parse_complex import parse_complex

# Напишите функцию, которая принимает на вход односвязный список и индекс элемента, который нужно удалить. Функция должна удалить элемент с указанным индексом и вернуть измененный список.
from YeatBigTonka.Algorithms.remove_node_at_index import remove_node_at_index

# Напишите программу, которая получает число в двоичной системе и преобразует его в десятеричную и шестнадцатеричную системы счисления.
from YeatBigTonka.Algorithms.convert_binary_to_decimal_and_hex import convert_binary_to_decimal_and_hex

# Напишите класс со следующими условиями:
# Метод инициализации экземпляра создает для него поля nums (массив уникальных натуральных чисел), solution (массив)
# Метод обработки массива nums так, чтобы массив solution содержал все возможные перестановки. Вы можете вернуть ответ в любом порядке.
# Метод печати по заданному образцу
#
# Декорируйте класс методом вычисления медианы массива.
from YeatBigTonka.SystemsProgramming.permutations_processor import Class

# Напишите класс со следующими условиями:
# Метод инициализации экземпляра создает для него поля num (натуральное число), solution (строка)
# Метод, переводящий число в римскую систему счисления
# Метод печати по заданному образцу
#
# Декорируйте метод перевода числа функцией, кэширующей результат работы программы.
#
# Сложность решения: временная сложность - O(N), пространственная сложность - O(N) (N – длина числа)
from YeatBigTonka.SystemsProgramming.roman import Class

# Напишите класс со следующими условиями:
# Метод инициализации экземпляра создает для него поля num (натуральное число), solution (строка)
# Метод, выполняющий операцию «Посчитай и скажи» num раз по принципу:
# countAndSay(1) = "1"
# countAndSay(n) — это способ «произнести» строку цифр из countAndSay(n-1), которая затем преобразуется в другую строку цифр
# Метод печати по заданному образцу
from YeatBigTonka.SystemsProgramming.count_and_say import Class

# Василий считает, что когда текст пишут в скобках (как вот тут, например), его читать не нужно. Вот и надумал он существенно укоротить время чтения, написав функцию, которая будет удалять все, что расположено внутри скобок. Помогите ленивому Васе разработать функцию, которая будет удалять все, что внутри скобок и сами эти скобки, возвращая очищенный текст (скобки могут быть вложенными).
from YeatBigTonka.SystemsProgramming.remove_parentheses import remove_parentheses

# Напишите класс со следующими условиями:
# Метод инициализации экземпляра создает для него поля nums (массив натуральных чисел, отсортированный в неубывающем порядке), solution (массив)
# Метод обработки массива nums в массив solution так, чтобы первые элементы массива solution содержали уникальные элементы в том порядке, в котором они присутствовали в nums изначально
# Метод печати по заданному образцу
#
# Декорируйте класс методом вычисления суммы элементов массива.
#
# Сложность решения: временная сложность - O(N), пространственная сложность - O(N) (N – длина массива)
from YeatBigTonka.SystemsProgramming.remove_duplicates import Class

__all__ = ['insert_into_heap', 'merge_sort', 'vowel_fraction', 'parse_complex', 'remove_node_at_index',
           'convert_binary_to_decimal_and_hex']
