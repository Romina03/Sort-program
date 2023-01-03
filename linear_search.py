the_list = []

def introduction():
    print("This program reads numbers from a file called input.txt, and sorts the numbers from smallest to largest.")

def sort(li):
    def min(start):
        tempMin = start
        i = start + 1
        for a in range(i, len(li)):
            if li[a] < li[tempMin]:
                tempMin = a
        min = tempMin
        return min

    for val in range(len(li)):
        minimum_val = min(val)
        li[val], li[minimum_val] = li[minimum_val], li[val]
    return li
        
    


def read_input():
    file = open("input.txt")
    for line in file:
        the_list.append(float(line))
    file.close()

def display(li):
    for number in li:
        print(number)


introduction()
read_input()
sort(the_list)
print("Sorted numbers are: ")
display(the_list)









