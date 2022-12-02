
def read_file_num():
    f=open('input.txt', 'r')
    inter  = f.readlines()
    finallist = []
    templist = []
    k = 0
    
    for line in inter:  
       
        if line == '\n':
            
            finallist.append(templist)
            k +=1
            templist = []
        elif templist == []:
            
            templist.append(int(line))
        else:
           
            templist.append(int(line))
            
            
    
    
    return finallist





def sum (listOfLists):
    largest = 0
    second = 0
    third = 0
    for place in listOfLists:
        print(third)
        print(second)
        print(largest)
        summ = 0
        if place is int:
            if place > largest:
                third = second 
                second = largest
                largest = place
                
            
            elif (place > second and place < largest):
                third = second 
                second = place
            
            elif (place > third and place < second):
                third = place
                    
        else:
            
            for index in place:
                summ += index
                if summ > largest:
                    third = second
                    second = largest
                    largest = summ
                elif (summ > second and summ < largest):
                    third = second 
                    second = summ
            
                elif (summ > third and summ < second):
                    third = summ
    total = (largest + second + third)               
    return total
                    
print(sum(read_file_num()))
