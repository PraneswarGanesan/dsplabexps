def remove_spaces(s):
  return s.replace(" ", "")
input_string = input("Enter a string: ")
string_without_spaces = remove_spaces(input_string)
print("String without spaces:", string_without_spaces)
