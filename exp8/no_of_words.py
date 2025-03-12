
with open("book.txt", "r") as file:
   
    words = file.read().split()

word_count = len(words)


print("Number of words in the file:", word_count)
