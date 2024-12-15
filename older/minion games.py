def minion_game(string):
    s = len(string)
    con, vow = 0, 0

    for i in range(s):
        if string[i] in 'AEIOU':
            vow = vow + (s-i)
        else:
            con = con + (s-i)
    
    if con>vow:
        print('Stuart', con)
    elif vow>con:
        print('Kevin', vow)
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)