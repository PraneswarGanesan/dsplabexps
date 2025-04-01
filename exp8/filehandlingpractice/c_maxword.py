try:
    with open ("b_wordcount.txt", "r") as file:
        word = file.read().split()
    
    maxWord = max(word,key=len)
    print("The longestword in the file is: ",maxWord)

except Exception as e:
    print(f"Error Occured: {e}")