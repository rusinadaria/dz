# 3 4 1 5 2 5 4 1 5 1 1 3 5 1 4 1 5 2 2 2
import matplotlib.pyplot as plt
list = []

while len(list) < 20:
    try:
        inp = int(input())
        list.append(inp)
    except ValueError:
        print("Только числа, друг, давай не дури...")

zo = int()
ft_1 = sum(True for i in list if i == 1)
sd_2 = sum(True for i in list if i == 2)
td_3 = sum(True for i in list if i == 3)
fhd_4 = sum(True for i in list if i == 4)
fh_5 = sum(True for i in list if i == 5)
st_6 = sum(True for i in list if i == 6)


print(list)
print('--------ВАРИАЦИОННЫЙ РЯД--------')
print(ft_1, ' - 1')
print(sd_2, ' - 2')
print(td_3, ' - 3')
print(fhd_4, ' - 4')
print(fh_5, ' - 5')
print(st_6, ' - 6')



x = ('0', '1', '2', '3', '4', '5', '6')
y = (zo, ft_1, sd_2, td_3, fhd_4, fh_5, st_6)

# столбы
fig, ax = plt.subplots()
ax.bar(x, y)
plt.xlabel('Варианты')
plt.ylabel('Частота')
plt.show()

# точки
plt.axis([0, 7, 0, 7])
plt.xlabel('Варианты')
plt.ylabel('Частота')
plt.plot(x, y, 'ro')
plt.show()


l_s = sorted(list)
# Простая арифметика...
sum_chas = ft_1 + sd_2 + td_3 + fhd_4 + fh_5 + st_6
sr_qv = ((1 ** 2) * ft_1 + (2 ** 2) * sd_2 + (3 ** 2) * td_3 + (4 ** 2) * fhd_4 + (5 ** 2) * fh_5 + (6 ** 2) * st_6)/sum_chas
v_sr = (1 * ft_1 + 2 * sd_2 + 3 * td_3 + 4 * fhd_4 + 5 * fh_5 + 6 * st_6)/sum_chas
v_disp = (sr_qv - (v_sr ** 2)) * sum_chas / (sum_chas - 1)
st_otcl = v_disp ** 0.5
one_proc = st_otcl / 100
kf_v = (st_otcl * (one_proc * 100)) / v_sr
print('Сумма частот - ', sum_chas)
print('Выборочная средняя - ', v_sr)
print('Средняя квадратов - ', sr_qv)
print('Выборочная дисперсия (Dв) - ', v_disp)
print('Среднее отклонение -  ', st_otcl)
print('Коэффициент вариации - ', kf_v)
print('Медиана - ', (l_s[9] + l_s[10])/2)