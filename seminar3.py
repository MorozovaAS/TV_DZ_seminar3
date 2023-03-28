import numpy as np
from math import factorial

# Даны значения зарплат из выборки выпускников: 100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150.
# Посчитать (желательно без использования статистических методов наподобие std, var, mean) среднее арифметическое,
# среднее квадратичное отклонение, смещенную и несмещенную оценки дисперсий для данной выборки.
average = 0
x = [100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150]
for i in range (len (x)):
    average = average + x[i]
print ("Задача 1:")
print ("")
print ("Среднее арифметическое =", average/len (x))

d = 0
for i in range (len (x)):
        d = d + ((x[i] - average/len (x))**2)
    
print ("Несмещенная дисперсий =", d/(len(x)-1))
print("Смещенная дисперсий =", d/(len(x)))
print("Среднее квадратичное отклонение =", np.sqrt(d/len(x)))


#В первом ящике находится 8 мячей, из которых 5 - белые.
# Во втором ящике - 12 мячей, из которых 5 белых.
# Из первого ящика вытаскивают случайным образом два мяча, из второго - 4.
# Какова вероятность того, что 3 мяча белые?

print ("")
print ("Задача 2:")
print ("")


first_combination = (factorial(5) / (factorial(2)*factorial(5-2))) * (factorial(5) / (factorial(1)*factorial(5-1))) * (factorial(7) / (factorial(3)*factorial(7-3))) \
    / ((factorial(8) / (factorial(2)*factorial(8-2))) * (factorial(12) / (factorial(4)*factorial(12-4))))


second_combination = (factorial(5) / (factorial(1)*factorial(5-1))) * (factorial(3) / (factorial(1)*factorial(3-1))) * (factorial(5) / (factorial(2)*factorial(5-2)))  \
    * (factorial(7) / (factorial(2)*factorial(7-2))) / ((factorial(8) / (factorial(2)*factorial(8-2))) * (factorial(12) / (factorial(4)*factorial(12-4))))

third_combination = (factorial(3) / (factorial(2)*factorial(3-2))) * (factorial(5) / (factorial(3)*factorial(5-3))) * (factorial(7) / (factorial(1)*factorial(7-1))) \
    / ((factorial(8) / (factorial(2)*factorial(8-2))) * (factorial(12) / (factorial(4)*factorial(12-4))))
print("Вероятность того, что 3 мяча белые =", round((first_combination+second_combination+third_combination)*100,2),"%")




# На соревновании по биатлону один из трех спортсменов стреляет и попадает в мишень. 
# Вероятность попадания для первого спортсмена равна 0.9, для второго — 0.8, для третьего — 0.6.
# Найти вероятность того, что выстрел произведен: a). первым спортсменом б). вторым спортсменом в). третьим спортсменом.

print ("")
print ("Задача 3:")
print ("")
one = 0.9
two = 0.8
three = 0.6

P = (1 / 3 * one) + (1 / 3 * two) +  (1 / 3 * three)

print("Вероятность того, что выстрел произведен первым спортсменом =", round(1/3*one/P*100, 2),"%")
print("Вероятность того, что выстрел произведен первым спортсменом =", round(1/3*two/P*100, 2),"%")
print("Вероятность того, что выстрел произведен первым спортсменом =", round(1/3*three/P*100, 2),"%")

#В университет на факультеты A и B поступило равное количество студентов, а на факультет C студентов поступило столько же,
# сколько на A и B вместе. Вероятность того, что студент факультета A сдаст первую сессию, равна 0.8.
# Для студента факультета B эта вероятность равна 0.7, а для студента факультета C - 0.9.
# Студент сдал первую сессию. Какова вероятность, что он учится: a). на факультете A б). на факультете B в). на факультете C?

print ("")
print ("Задача 4:")
print ("")

a = 0.8
b = 0.7
c = 0.9

Ptwo = (1 / 4 * a) + (1 / 4 * b) +  (2 / 4 * c)

print("Вероятность того, что студент, сдавший первую сессию, учился на факультете А =", round(1/4*a/Ptwo*100, 2),"%")
print("Вероятность того, что студент, сдавший первую сессию, учился на факультете В =", round(1/4*b/Ptwo*100, 2),"%")
print("Вероятность того, что студент, сдавший первую сессию, учился на факультете С =", round(2/4*c/Ptwo*100, 2),"%")

#Устройство состоит из трех деталей. Для первой детали вероятность выйти из строя в первый месяц равна 0.1, для второй - 0.2,
# для третьей - 0.25. Какова вероятность того, что в первый месяц выйдут из строя: а). все детали б). только две детали
# в). хотя бы одна деталь г). от одной до двух деталей?

print ("")
print ("Задача 5:")
print ("")

first_detail = 0.1
second_detail = 0.2
third_detail = 0.25

probability_a = first_detail*second_detail*third_detail
probability_b = ((1-first_detail)*second_detail*third_detail) + (first_detail*(1-second_detail)*third_detail) + (first_detail*second_detail*(1-third_detail))
probability_c = 1-(1-first_detail)*(1-second_detail)*(1-third_detail)
probability_d = probability_c - probability_a
print("Вероятность того, что в первый месяц выйдут из строя все детали =", round(probability_a, 4),"%")
print("Вероятность того, что в первый месяц выйдут из строя только две детали =", probability_b,"%")
print("Вероятность того, что в первый месяц выйдет из строя хотя бы одна деталь =", round(probability_c,4), "%")
print("Вероятность того, что в первый месяц выйдут из строя от одной до двух деталей =", round(probability_d,4), "%")
