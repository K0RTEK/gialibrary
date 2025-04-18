#Задание 4
# Напишите программу, которая запрашивает у пользователя строку и выводит на экран долю гласных букв в этой строке.
def vowel_fraction(input_str: str) -> float:
    vowels = set("aeiouAEIOU")
    # vowels = set("аеёиоуыэюяАЕЁИОУЫЭЮЯ")
    total_length = len(input_str)
    if total_length == 0:
        return 0.0
    vowel_count = sum(1 for ch in input_str if ch in vowels)
    return (vowel_count / total_length) * 100  # Процент
result = vowel_fraction("aeaaa")
print(result)