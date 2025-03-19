# Triangle Star Pyramid
def triangle_pyramid(rows):
    print("\nTriangle Star Pyramid:")
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "* " * i)

'''
Output:
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
'''

# Inverted Star Pyramid
def inverted_pyramid(rows):
    print("\nInverted Star Pyramid:")
    for i in range(rows, 0, -1):
        print(" " * (rows - i) + "* " * i)

'''
Output:
* * * * * 
 * * * * 
  * * * 
   * * 
    * 
'''

# Pascal's Triangle
def pascal_triangle(n):
    print("\nPascal's Triangle:")
    for i in range(n):
        num = 1
        print(" " * (n - i), end="")
        for j in range(i + 1):
            print(num, end=" ")
            num = num * (i - j) // (j + 1)
        print()

'''
Output:
     1 
    1 1 
   1 2 1 
  1 3 3 1 
 1 4 6 4 1 
'''

# Inverted Pascal’s Triangle
def inverted_pascal(n):
    print("\nInverted Pascal's Triangle:")
    for i in range(n, 0, -1):
        num = 1
        print(" " * (n - i), end="")
        for j in range(i):
            print(num, end=" ")
            num = num * (i - j - 1) // (j + 1)
        print()

'''
Output:
1 4 6 4 1 
 1 3 3 1 
  1 2 1 
   1 1 
    1 
'''

# Alphabet Pyramid
def alphabet_pyramid(rows):
    print("\nAlphabet Pyramid:")
    for i in range(1, rows + 1):
        print("".join(chr(96 + j) for j in range(1, i + 1)))

'''
Output:
a
ab
abc
abcd
'''

# Inverted Alphabet Pyramid
def inverted_alphabet_pyramid(rows):
    print("\nInverted Alphabet Pyramid:")
    for i in range(rows, 0, -1):
        print("".join(chr(96 + j) for j in range(1, i + 1)))

'''
Output:
abcd
abc
ab
a
'''

# Alphabet Step Pattern
def alphabet_step(word):
    print("\nAlphabet Step Pattern:")
    for i in range(len(word)):
        print(word[i:])

'''
Output:
abcd
bcd
cd
d
'''

# Number Pyramid
def number_pyramid(rows):
    print("\nNumber Pyramid:")
    for i in range(1, rows + 1):
        print(" " * (rows - i), end="")
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

'''
Output:
    1 
   1 2 
  1 2 3 
 1 2 3 4 
1 2 3 4 5 
'''

# Inverted Number Pyramid
def inverted_number_pyramid(rows):
    print("\nInverted Number Pyramid:")
    for i in range(rows, 0, -1):
        print(" " * (rows - i), end="")
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

'''
Output:
1 2 3 4 5 
 1 2 3 4 
  1 2 3 
   1 2 
    1 
'''

# Floyd's Triangle
def floyds_triangle(rows):
    print("\nFloyd's Triangle:")
    num = 1
    for i in range(1, rows + 1):
        for j in range(i):
            print(num, end=" ")
            num += 1
        print()

'''
Output:
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15 
'''

# Hollow Pyramid
def hollow_pyramid(rows):
    print("\nHollow Pyramid:")
    for i in range(1, rows + 1):
        for j in range(rows - i):
            print(" ", end="")
        for j in range(2 * i - 1):
            if j == 0 or j == 2 * i - 2 or i == rows:
                print("*", end="")
            else:
                print(" ", end="")
        print()

'''
Output:
    *    
   * *   
  *   *  
 *     * 
*********
'''

# Diamond Pattern
def diamond_pattern(rows):
    print("\nDiamond Pattern:")
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "* " * i)
    for i in range(rows - 1, 0, -1):
        print(" " * (rows - i) + "* " * i)

'''
Output:
   * 
  * * 
 * * * 
* * * * 
 * * * 
  * * 
   * 
'''

# Alphabet Diamond
def alphabet_diamond(rows):
    print("\nAlphabet Diamond:")
    for i in range(1, rows + 1):
        print(" " * (rows - i), end="")
        for j in range(1, i + 1):
            print(chr(96 + j), end=" ")
        print()
    for i in range(rows - 1, 0, -1):
        print(" " * (rows - i), end="")
        for j in range(1, i + 1):
            print(chr(96 + j), end=" ")
        print()

'''
Output:
   a 
  a b 
 a b c 
a b c d 
 a b c 
  a b 
   a 
'''

# X Pattern
def x_pattern(rows):
    print("\nX Pattern:")
    for i in range(rows):
        for j in range(rows):
            if i == j or i + j == rows - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()

'''
Output:
*   * 
 * *  
  *   
 * *  
*   * 
'''

# Call all functions with sample inputs
rows = 5
triangle_pyramid(rows)
inverted_pyramid(rows)
pascal_triangle(rows)
inverted_pascal(rows)
alphabet_pyramid(4)
inverted_alphabet_pyramid(4)
alphabet_step("abcd")
number_pyramid(rows)
inverted_number_pyramid(rows)
floyds_triangle(rows)
hollow_pyramid(rows)
diamond_pattern(4)
alphabet_diamond(4)
x_pattern(rows)
