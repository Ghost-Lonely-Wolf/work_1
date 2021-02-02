profit = int(input('Введите свою прибыль '))
costs = int(input('Введите свои издержки '))
if profit < costs:
    print('Ваша прибыль меньше издержек')
elif profit > costs:
    print('Ваша прибыль больше издержек')
    proceeds = int(input('Введите свою выручку '))
    staff = int(input('Введите численность сотрудников фирмы '))
    profitability = profit / proceeds * 100
    worker = profit / staff
    print('рентабельность выручки ', profitability)
    print('прибыль фирмы в расчете на одного сотрудника ', worker)
