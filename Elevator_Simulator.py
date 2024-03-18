import sys
def elevator(floors, constant):
    result = 0
    for curr in range(len(floors) - 1):
        diff = abs(floors[curr] - floors[curr+1])
        result += diff
    total_time = result * constant
    return total_time

#put in floors manually into list
# floors = [12, 2, 9, 1, 32]
# program_Constant = 10

#User input
floors = []
start_floor = input("Start Floor: ")
floors.append(int(start_floor))
listOfFloors = input("List floors in order seperated with a space: ")
floors.extend([int(num) for num in listOfFloors.split()])
program_Constant = int(input("Program Constant: "))



print(elevator(floors, program_Constant), floors)

