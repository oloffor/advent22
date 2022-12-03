
def read_file():
	data = open(input3.txt).readlines()
	return data


print(read_file())

def compute_value (string):
    if  string.istitle:
        return ord(string) - 38
    return ord(string) - 96


def find_duplicates():
    inter = read_file()
    duplicates = []
    for line in inter:
        for letter in line/2:
            if letter == line[line.index(letter)]:
                duplicates.append(letter)
    return duplicates
                

#print(find_duplicates())