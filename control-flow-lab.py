# exercise-01 Vowel or Consonant

# Write the code that:
# 1. Prompts the user to enter a letter in the alphabet:
#      Please enter a letter from the alphabet (a-z or A-Z): 
# 2. Write the code that determines whether the letter entered is a vowel
# 3. Print one of following messages (substituting the letter for x):
#      - The letter x is a vowel
#      - The letter x is a consonant

# Hints:  Use the in operator to check if a character is in another string
#         For example, if some_char in 'abc':

alpha = input(' Please enter a letter from the alphabet ').lower()
if alpha in ("a", "e", "i", "o", "u", "y"):
    print(f"The letter {alpha} is a vowel")
else:
    print(f"The letter {alpha} is a consonant")

# exercise-02 Length of Phrase

# Write the code that:
# 1. Prompts the user to enter a phrase:
#      Please enter a word or phrase: 
# 2. Print the following message:
#      - What you entered is xx characters long
# 3. Return to step 1, unless the word 'quit' was entered.

phrase = input("Enter a phrase or quit: ")
while phrase != "quit":
    print(f"what you entered is {len(phrase)} characters long")
    phrase = input("Enter a phrase or quit: ")
else:
    print("goodbye!")
    
# exercise-03 Calculate Dog Years

# Write the code that:
# 1. Prompts the user to enter a dog's age in human years like this:
#      Input a dog's age in human years: 
# 2. Calculates the equivalent dog years, where:
#      - The first two years count as 10 years each
#      - Any remaining years count as 7 years each
# 3. Prints the answer in the following format:
#      The dog's age in dog years is xx

# Hint:  Use the int() function to convert the string returned from input() into an integer

dog_years = int(input("Input your dog's age: "))
if dog_years <= 2:
    dog_age = dog_years*10
elif dog_years >= 3:
    dog_age = dog_years*7+6
print(f"The dog's age in years is {dog_age}")

  
# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a: 
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equalateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle

print("Enter the lenghts of a triangle: ")
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
if a == b == c:
    print("This triangle is equalateral")
elif a != b != c: 
    print("This triangle is a scalene")
else: 
    print("this triangle is isosceles")


# exercise-04 What kind of Triangle?

# exercise-05 Fibonacci sequence for first 50 terms

# Write the code that:
# 1. Calculates and prints the first 50 terms of the fibonacci sequence.
# 2. Print each term and number as follows:
#      term: 0 / number: 0
#      term: 1 / number: 1
#      term: 2 / number: 1
#      term: 3 / number: 2
#      term: 4 / number: 3
#      term: 5 / number: 5
#      etc.

# Hint: The next number is found by adding the two numbers before it

a, b = 0, 1
number = 0
while number  < 50:
    c = a + b
    a = b
    b = c
    number += 1
    print(f"Term {number} / number: {c}")

# exercise-06 What's the  Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the year (Jan - Dec):
# 2. Then prompts the user to enter the day of the month: 
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 

# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
# if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.


month = input("Enter a month of the year(Jan-Dec): ").lower()
day = int(input("Day of the Month: "))
if month in ('jan', 'feb', 'mar'):
	season = 'winter'
elif month in ('apr', 'may', 'jun'):
	season = 'spring'
elif month in ('jul', 'aug', 'sep'):
	season = 'summer'
else:
	season = 'autumn'

if (month == 'mar') and (day >= 20):
	season = 'spring'
elif (month == 'jun') and (day >= 21):
	season = 'summer'
elif (month == 'sep') and (day >= 22):
	season = 'autumn'
elif (month == 'dec') and (day >= 21):
	season = 'winter'

print(f"{month} and {day} is in {season}")