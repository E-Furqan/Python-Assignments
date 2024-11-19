
def FibonacciSequence(number):
    FibonacciSequence=[]
    number1, number2 = 0, 1
    for _ in range(number):
        FibonacciSequence.append(number1)
        number1, number2 = number2, number1+number2
    
    return FibonacciSequence


def main():
    number1=int(input("Enter number: "))
    print(f"Fibonacci Sequence of number {number1} = ",FibonacciSequence(number1))


if __name__=="__main__":
    main()