'''Задача 2. Счетчик бракованных батончиков'''

good= 0       # Хороший батончик
bad= 0        # Плохой батончик


while True:
    mass = int(input())     # масса батончика
    if mass == 0:
        break

    if 40 <= mass <= 50:
        print('GOOD')
        good += 1

    if mass <= 39 or mass >= 51:
        print('BAD')
        bad += 1

result = round(float((bad/(good+bad))), 2)

print('Коэффициент брака:', result,'%')