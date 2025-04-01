try:
    with open ("b_wordcount.txt", "r") as file:
        word = file.read().split()

    word_count = len(word)
    print(f"The number of words in this file is: {word_count}")

except Exception as e:
    print(f"Error occured:{e} ")