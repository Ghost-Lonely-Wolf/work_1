km = int(input('В первый день спортсмен пробежал км '))
day = int(input('За сколько дней он пробежит км '))
days = 1
while day - km > 0:
    km = km + (km * 0.1)
    days += 1
print('Он побежит за ', days, 'дней')
