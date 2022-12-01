
def read_file_num():
    f=open('input.txt', 'r')
    finallist = []
    templist = []
    k = 0
    for line in f:
        
        if line.strip():
            finallist.append(templist)
            #print(finallist)
            k +=1
            
        elif templist == []:
            templist[0] = int(line)
        else:
           templist.append(int(line))
            
            
    finallist.append(templist)
    
    return finallist



#print(read_file_num())

def sum (listOfLists):
    largest = 0
    for place in listOfLists:
        
        summ = 0
        if place is int:
            if place > largest:
                largest = place
                    
        else:
            
            for index in place:
                summ += index
                if summ > largest:
                    largest = summ
                    
    return largest
                    
print(sum(read_file_num()))