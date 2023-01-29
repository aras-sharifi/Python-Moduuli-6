def parittomat_luvut(list):
    newlist = []
    for i in list:
        if i % 2 == 0:
            newlist.append(i)
    return newlist





list = [1,2,3,4,5,6,7,8,9,10]
result = parittomat_luvut(list)
print(list)
print(result)