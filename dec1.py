
def read_file_num():
    f=open('dec1', 'a')
    finallist = []
    templist = []
    k = 0
    for line in f:
        if (line == '\n'):
            finallist.append(templist)
            k +=1
        else:
            templist.append()
    
    return finallist



print(read_file_num)

def sum (listOfLists):
    for place in listOfLists:
        for index in place:
            if place.is_integer():
                if index > largest:
                    largest = index
            else:
                summ += index
                if summ > largest:
                    largest = summ
                    
print(sum(read_file_num))