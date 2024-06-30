# Ввод данных
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# Создаём пустые списки
primes = []
not_primes = []
# Создаём цикл определения простого числа
for number in numbers:
    if number == 1:
        continue
    is_prime = True
    for i in range(2, number): # вложенный цикл
        if number % i == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(number)
    else:
        not_primes.append(number)
# Вывод результата
print("Primes:", primes)
print("Not Primes:", not_primes)