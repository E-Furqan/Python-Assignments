def VowelCounter(input):
    counter=0
    for i in input:
        if i.lower() in 'aeiou':
            counter +=1 
    
    return counter


def main():
    input_string = str(input("Please enter a string to count the number of vowels: "))
    output = VowelCounter(input_string)
    print(f"Number of vowels in '{input_string}': {output}")


if __name__ == "__main__":
    main()