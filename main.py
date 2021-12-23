import random

cm_in_meter = 100
meter_in_km = 1000
pink_floyd = ["fatima" , " ali" , "asmaa"]

def get_file_ext(filename) :
    return filename[filename.index(".") + 1 : ]


def roll dice(num):
    return random.randint(1,num):

#[Forwarded from Mohammed Abdulrasool]
names = [['m', 'o', 'h', 'a', 'm', 'm', 'e', 'd', ' ', ' ', ' ', ' '],
         ['n', 'o', 'o', 'r', 'a', 'l', 'h', 'u', 'd', 'a', ' ', ' '],
         ['z', 'a', 'h', 'r', 'a', 'a', ' ', ' ', ' ', ' ', ' ', ' '],
         ['f', 'a', 't', 'i', 'm', 'a', ' ', ' ', ' ', ' ', ' ', ' '],
         ['n', 'o', 'o', 'r', 'a', 'l', 'z', 'a', 'h', 'r', 'a', 'a']]
# loop to print all elements in array
for name in range(len(names)):
    for x in names[name]:
        if x == " ":
            continue
        print(x, end="")
    print()

'''
#to insert element
names.insert(3,['A','l','i',' ',' ',' ',' ',' ',' ',' ',' ',' '])
print(names)
'''

'''
#to update element
names[0]=[['A','l','i',' ',' ',' ',' ',' ',' ',' ',' ',' ']]
print(names)
'''
'''
#to remove element
#names.remove(names[0])
print(names)
'''
