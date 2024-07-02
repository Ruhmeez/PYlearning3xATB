#example1

def allowed_to_attend_python_class(name, password):
    if name == "Ruheen":
        if password == "Yes":
            print("You are allowed to enter")
        else:
            print("Not allowed")

allowed_to_attend_python_class("Ruheen", "no")


#example2

def allowed_to_attend_python_class(name):
    match name:
        case "Dell":
            print("Dell is allowed")
        case "Shubham":
            print("Shubham is allowed")
        case "Pallavi":
            print("Pallavi is allowed")
        case _:
            print("Not allowed")
allowed_to_attend_python_class("Shubham")