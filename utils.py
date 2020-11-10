# Функция принимает на вход диапазон a-b и на выходе перечисление через запятую
def str_between(diapazon: str) -> str:
    defis = diapazon.find('-', 0, len(diapazon))
    b_str = diapazon[0:defis]
    e_str = diapazon[int(defis)+1:len(diapazon)]
    return list(range(int(b_str), int(e_str)+1, 1))

# Функция принимает на входе строку перечисления неформатированную и форматирует ее
def str_format(s: str) -> str:
    sps = s.split(',')
    for i in range(len(sps)):
        elem = sps[i].find('-', 0, len(sps[i]))
        if elem != -1:
            sps[i] = ','.join(map(str_between(sps[i])))
    return ','.join(sps)