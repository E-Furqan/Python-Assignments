def Sum(myList):
    total=0
    
    for i in myList:
        total += i
        
    return total

def Average(myList):
    sum= Sum(myList)
    average= sum/len(myList)
    
    return average

def MaximumValue(myList):
    if len(myList) > 0:
        maxValue= max(myList)
    else:
        maxValue=0
        
    return maxValue

def ReverseList(myList):
    return myList[::-1]

def ListOperations(numbers):
    totalSum = Sum(numbers)
    average = Average(numbers)
    maximum = MaximumValue(numbers)
    
    return totalSum,average,maximum
    
    
def main():
    numbers = [1, 5, 3, 8, 2]
    total_sum, average, maximum = ListOperations(numbers)
    print(f"Sum: {total_sum}")
    print(f"Average: {average}")
    print(f"Maximum: {maximum}")

    my_list = ['a', 'b', 'c']
    reversed_list = ReverseList(my_list)
    print(f"Reversed List: {reversed_list}")
    
    
if __name__ == "__main__":
    main()