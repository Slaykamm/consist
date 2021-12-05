#рекурсивно. 

import sys
sys.setrecursionlimit(4000001)

bugs = int(input("NUmber of BUGS: "))

stones = int(input("NUmber of Stones: "))


reserveStone = 0   # запонимаем откинутый отрезок ##
stones1 = 0
stones2 = 0


def bugs_recursive(bugs, stones, reserveStone, stones1, stones2):


    if bugs != 0:
        if stones < reserveStone:
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
        return bugs_recursive(bugs-1, stones, reserveStone, stones1, stones2)


    else:
        return stones1, stones2
    


stoneLeft, stoneRight = bugs_recursive(bugs, stones, reserveStone, stones1, stones2)

print("слева камней: ", stoneLeft, "справа камней: ", stoneRight)



    

