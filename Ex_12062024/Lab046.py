# Write a program that calculates and displays the letter
# given numerical score (e.g., A, B, C, D or F)
# based on the following grading scale:
# input score - 89
# output - B
# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: 0-59

# Multiple conditions - if, elif, esle

# Step 1# Logic building
# Input ?
# input is score -> int
score = int(input("Enter the score\n"))

# output - String -> A,B,C,D,F

# Step 2#
# Write a rough logic and convert to real one

# score >=90 and score<=100 -> A
# score >=80 and score<=89 -> B
# score >=70 and score<=79 -> C
# score >=60 and score<=69 -> D
# score >=0 and score<=59 -> F

if score >=90 and score <=100:
    print("A")
elif score >=80 and score<=89:
    print("B")
elif score >=70 and score<=79:
    print("C")
elif score >=60 and score<=69:
    print("D")
elif score >=0 and score<=59:
    print("F")
else:
    print("Invalid score")

# For
# While
# If else
# If elif else





















