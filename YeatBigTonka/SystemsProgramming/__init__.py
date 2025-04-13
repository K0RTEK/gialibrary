# Напишите класс со следующими условиями:
# Метод инициализации экземпляра создает для него поля num (натуральное число), solution (строка)
# Метод, выполняющий операцию «Посчитай и скажи» num раз по принципу:
# countAndSay(1) = "1"
# countAndSay(n) — это способ «произнести» строку цифр из countAndSay(n-1), которая затем преобразуется в другую строку цифр
# Метод печати по заданному образцу
from .count_and_say import Class

# Напишите класс со следующими условиями:
# Метод инициализации экземпляра создает для него поля nums (массив уникальных натуральных чисел), solution (массив)
# Метод обработки массива nums так, чтобы массив solution содержал все возможные перестановки. Вы можете вернуть ответ в любом порядке.
# Метод печати по заданному образцу
#
# Декорируйте класс методом вычисления медианы массива.
from .permutations_processor import Class

# Напишите класс со следующими условиями:
# Метод инициализации экземпляра создает для него поля nums (массив натуральных чисел, отсортированный в неубывающем порядке), solution (массив)
# Метод обработки массива nums в массив solution так, чтобы первые элементы массива solution содержали уникальные элементы в том порядке, в котором они присутствовали в nums изначально
# Метод печати по заданному образцу
#
# Декорируйте класс методом вычисления суммы элементов массива.
#
# Сложность решения: временная сложность - O(N), пространственная сложность - O(N) (N – длина массива)
from .remove_duplicates import Class

# Василий считает, что когда текст пишут в скобках (как вот тут, например), его читать не нужно. Вот и надумал он существенно укоротить время чтения, написав функцию, которая будет удалять все, что расположено внутри скобок. Помогите ленивому Васе разработать функцию, которая будет удалять все, что внутри скобок и сами эти скобки, возвращая очищенный текст (скобки могут быть вложенными).
from .remove_parentheses import remove_parentheses

# Напишите класс со следующими условиями:
# Метод инициализации экземпляра создает для него поля num (натуральное число), solution (строка)
# Метод, переводящий число в римскую систему счисления
# Метод печати по заданному образцу
#
# Декорируйте метод перевода числа функцией, кэширующей результат работы программы.
#
# Сложность решения: временная сложность - O(N), пространственная сложность - O(N) (N – длина числа)
from .roman import Class


__add__ = ['Class', 'remove_parentheses']