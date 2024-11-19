import string
import os

def WordFrequencyCounter(filepath):
    wordCount = {}
    print(filepath)
    with open(filepath, 'r') as file:
        text = file.read().lower()
        text = text.translate(str.maketrans('', '', string.punctuation))
        
        words = text.split()
        
        for word in words:
            wordCount[word] = wordCount.get(word, 0) + 1
    
    return wordCount


def main():
    relative_path = 'example.txt'
    absolute_path = os.path.abspath(relative_path)
    
    result=WordFrequencyCounter(absolute_path)
    print(f"Word Frequency: {result}",)


if __name__=="__main__":
    main()