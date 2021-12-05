#итеравивно

bugs = int(input("NUmber of BUGS: "))

stones = int(input("NUmber of Stones: "))


reserveStone = 0   # запонимаем откинутый отрезок ##
i = 0
while i<bugs:
    if stones < reserveStone:   # проверяем не длиннее ли откинутая часть.
        reserveStone, stones = stones, reserveStone
# проверяем куда ставим
    stones1 = stones//2 
    stones2 = stones - stones//2 
#ставим 
    if stones1 >= stones2:
        stones1 = (stones1 - 1)
    else:
        stones2 = stones2 - 1
#проверяем после установки жука какой отрезок левый или правый берем дальше, а второй сохраняем на будущее для будущего сравнения.
    if stones1 >= stones2:
        stones = stones1
        if reserveStone < stones2:
            reserveStone = stones2
    else:
        stones = stones2
        if reserveStone < stones1:
            reserveStone = stones1
    i+=1
print("слева камней", stones1, "справа камней", stones2)
    




    

    

