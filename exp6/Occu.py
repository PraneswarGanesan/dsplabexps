def count_substring(s, sub):
  return s.count(sub)
input_string = input("Enter the main string: ")
substring = input("Enter the substring: ")
occurrences = count_substring(input_string, substring)
print(f"The substring '{substring}' appears {occurrences} times.")
