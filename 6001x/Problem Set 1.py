#Assume s is a string of lower case characters.
#Write a program that counts up the number of vowels contained in the string s.
#Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:
#Number of vowels: 5

s = "azcbobobegghakl"

vowels_counter = 0
for x in s:
    if x == "a" or x == "e" or x == "i" or x == "o" or x == "u":
        vowels_counter += 1
print("Number of vowels: " + str(vowels_counter))

########################################################################################################################

#Assume s is a string of lower case characters.
#Write a program that prints the number of times
#the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl',
#then your program should print
#Number of times bob occurs is: 2

s = 'azcbobobegbobghakbobobl'

counter = 0
index = 0
while index < len(s):
    index = s.find("bob", index)
    if index == -1:
        break
    counter += 1
    index += 1
print("Number of times bob occurs is:", counter)

########################################################################################################################

# Assume s is a string of lower case characters.
# Write a program that prints the longest substring of s in which the letters occur in alphabetical order.
# For example, if s = 'azcbobobegghakl', then your program should print
# Longest substring in alphabetical order is: beggh
# In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print
# Longest substring in alphabetical order is: abc
# Note: This problem may be challenging. We encourage you to work smart.
# If you('ve spent more than a few hours on this problem, we suggest that you move on to a different part of the course.
# If you have time, come back to this problem after you')ve had a break and cleared your head.

s = 'azcbobobegghabcdefghkl'

def longest_alphabetical_substring(s):
    longest = current = s[0]

    for i in range(1, len(s)):
        if s[i] >= s[i-1]:
            current += s[i]
            if len(current) > len(longest):
                longest = current
        else:
            current = s[i]

    return longest

print("Longest substring in alphabetical order is:", longest_alphabetical_substring(s))