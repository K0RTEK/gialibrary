#Задание 5

#Напишите программу, которая запрашивает у пользователя два комплексных числа в формате a + i*b и выводит на экран их сумму, 
# разность и произведение в виде кортежа. Для решения этой задачи НЕЛЬЗЯ :) использовать встроенный тип данных complex

a1, b1 = map(int, input("Введите первое комплексное число (a i*b): ").split())
a2, b2 = map(int, input("Введите второе комплексное число (a i*b): ").split())

sum_ = (a1 + a2, b1 + b2)
diff = (a1 - a2, b1 - b2)
prod = (a1 * a2 - b1 * b2, a1 * b2 + a2 * b1)

print("Сумма, разность, произведение:", sum_, diff, prod)