#Ternary operator
ruheen_marks = 90
firdos_marks = 80

#check if x>y -> do something("ruheen")
# else x<y -> do something else("firdos")

print("ruheen is winner" if ruheen_marks > firdos_marks  else "firdos is winner")

#above code is reducing the lines from below code - python - advantage
if ruheen_marks > firdos_marks:
    print("ruheen is the winner")
else:
    print("firdos is the winner")