#List-  shopping list
#milk, butter, bread, poha
#add item, remove item, update item, view item, exit

shopping_list = ["milk", "butter", "bread", "poha"]
print(shopping_list)
print(len(shopping_list))
print(shopping_list[0])
print(shopping_list[-1])

shopping_list.append("curd") #Add item in the end
print(shopping_list)
#shopping_list.insert(_index:1 , _object"jam")
#shopping_list.append("curd", "huh", "wwejgyy") #TypeError: list.append() takes exactly one argument (3 given)
#print(shopping_list)
shopping_list.insert(3, "Jam") #Add item in the middle
print(shopping_list)

shopping_list.extend(["chips", "salt"]) #Add multiple items in the end
print(shopping_list)

shopping_list.remove("bread") #Removes items
print(shopping_list.pop())
print(shopping_list.index("butter"))
shopping_list.reverse()
print(shopping_list)
shopping_list.sort()
print(shopping_list)
shopping_list[0]="Ruheen"
print(shopping_list)

#my_list = [1,2,3,4,True, 3.14, "Ruheen"]
#print(type(list)) #<class'list'>

