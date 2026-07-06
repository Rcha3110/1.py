# # Multiples of 3:

# # Write a for loop that prints all multiples of 3 between 1 and 30.
for i in range (1,31):
    if i%3 == 0:
        print(i)
print("Printed multiples of 3")

# # Sum of First 10 Numbers:
# # Write a program using a for loop that calculates the sum of numbers from 1 to 10.
i = 0
for x in range(1,11):
    i += x
print(i)
# # Print Your Name Letter by Letter:
# # Write a program that takes your name as input and prints each letter of your name using a for loop.
name = input("Write your name: ")
for letter in name:
    print(letter, end="")
# # Count Vowels in a String:
# # Write a program that counts how many vowels are in a given string using a for loop.
# word = input("\n Write a word: ")
# vovelCount = 0

# for lett in word:
#     if lett.lower() == "a":
#         vovelCount +=1
#         print(vovelCount)
#     elif lett.lower() == "e":
#         vovelCount +=1
#         print(vovelCount)
#     elif lett.lower() == "i":
#         vovelCount +=1
#         print(vovelCount)
#     elif lett.lower() == "o":
#         vovelCount +=1
#         print(vovelCount)
#     elif lett.lower() == "u":
#         vovelCount +=1
#         print(vovelCount)
#     # elif lett == "A":
#     #     vovelCount +=1
#     #     print(vovelCount)
#     # elif lett == "E":
#     #     vovelCount +=1
#     #     print(vovelCount)
#     # elif lett == "I":
#     #     vovelCount +=1
#     #     print(vovelCount)
#     # elif lett == "O":
#     #     vovelCount +=1
#     #     print(vovelCount)
#     # elif lett == "U":
#     #     vovelCount +=1
#     #     print(vovelCount)
#     else:
#         print(f"It's a consonant {lett}")
    
# print("Total vovels are: ", vovelCount)

word = input("Write a word: ")
vowelCount = 0
vowels = "aeiou"
for lett in word:
    if lett.lower() in vowels:
        vowelCount +=1
print(vowelCount)