#strings
#inbuilt functions
#function -> repeat a task - you can use a func
# print(), input(), type(), min, max, sum(), avg()

#strings
name="Amit" # 0 to 3
#0,1,2,3
# A, m, i, t
print(name)
print(type(name))
print(id(name)) #id-> memory address where it is stored
print(len(name)) #length of string(1)
name=name.upper()
name=name.lower()
a=name.count('A')
print(a)

a=name.count('A')
print(a)
print(name[2]) #name[4] string index out of range

#python - immutable - that cant be changed
name[0]="P" #'str' objectdoes not support item assignment