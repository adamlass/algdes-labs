import json, sys

f = open("data/blosum.json")
blosum_file = json.load(f)

blosum = blosum_file["matrix"]
penalty = int(blosum_file["penalty"])

test_file_name = sys.argv[1]
test_name_1 = sys.argv[2]
test_name_2 = sys.argv[3]

f = open(test_file_name)

class Animal:
    string = ""

    def __init__(self, name):
        self.name = name

    def char(self, index):
        string[index]

class Cell:
    max_neighbour=None
    temp_val=None
    val=None
    i=None
    j=None

def build_matrix(string1, string2):
    matrix = []
    for i in range(len(string1) + 1):
        matrix.append([])
        for j in range(len(string2) + 1):
            
            cell = Cell()
            cell.i=i
            cell.j=j

            if(i == 0 and j == 0):
                cell.val = 0

            matrix[i].append(cell)

    return matrix

def build_species():
    species = {}
    cur_name = None
    for line in f.readlines():

        if(line[0] == ">"):
            name = line.split(" ")[0][1:]
            cur_name = name
            species[name] = Animal(name)
        else:
            species[cur_name].string += line.split("\n")[0]
    return species

def blosum_delta(char1, char2):
    return blosum[char1][char2]

species = build_species()

subject_1 = species[test_name_1]
subject_2 = species[test_name_2]

string1 = subject_1.string
string2 = subject_2.string

matrix = build_matrix(string1, string2)

for j in range(len(string2) + 1):
    for i in range(1 if j == 0 else 0, len(string1) + 1):
        neighbours = [] 
        if i > 0 and j > 0:
            cell = matrix[i - 1][j - 1]

            char1 = string1[i - 1]
            char2 = string2[j - 1]
            delta = blosum_delta(char1, char2)
            
            cell.tempval = cell.val + delta
            neighbours.append(cell)
        
        if i > 0:
            cell = matrix[i - 1][j]

            cell.tempval = cell.val + penalty
            neighbours.append(cell)

        if j > 0:
            cell = matrix[i][j - 1]
            
            cell.tempval = cell.val + penalty
            neighbours.append(cell)
        
        max_neighbour = max(neighbours,key=lambda x: x.tempval)
        cell = matrix[i][j]
        cell.val = max_neighbour.tempval
        cell.max_neighbour = max_neighbour

cell = matrix[-1][-1]

new_string1 = ""
new_string2 = ""
total = cell.val

while(True):
    if cell.i == 0 and cell.j == 0:
        break

    next_cell = cell.max_neighbour

    new_string1 = f"{'-' if cell.i == next_cell.i else string1[cell.i - 1]}{new_string1}"
    new_string2 = f"{'-' if cell.j == next_cell.j else string2[cell.j - 1]}{new_string2}"

    cell = next_cell
    
    
print(f"{subject_1.name}--{subject_2.name}: {total}")
print(new_string1)
print(new_string2)

            

