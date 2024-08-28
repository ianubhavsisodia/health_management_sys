#health management system
# 3 clients - Harry, Rohan, Hammad
import datetime

def getdate():
    return datetime.datetime.now()

def select_name():
    name = {1:"Harry", 2:"Rohan", 3:"Hammad"}
    data = {1:"Diet", 2:"Exercise"}
    for key, value in name.items():
        print("press", key, "for", value, "\n", end="")
    n = int(input("\nSelect Name:\n"))
    if n>3:
        print("Error, select 1 or 2 !")
        exit()
    else:
        return n

def select_file_action():
    a = {1:"Log", 2:"Retrieve"}
    for key, value in a.items():
        print("Press", key, "for", value, "\n", end="")

    x= int(input("Select Action:\n"))
    if x>2:
        print("Error, select 1 or 2 !")
        exit()
    else:
        return x

def select_task():
    b = {1:"Food", 2:"Exercise"}
    for key, value in b.items():
        print("Press", key, "for", value, "\n", end="")

    y = int(input("Select task:\n"))
    if y>2:
        print("Error, select 1 or 2 !")
        exit()
    else:
        return y  

def action(n, x, y):
    
    # condition no 1
    if n == 1 and x == 1 and y == 1:
        value = input("type here\n")
  
        with open("Harry_diet.txt", "a") as Harry_diet:
  
            # printing date and time
            Harry_diet.write(str([str(getdate())]) + ": " + value + "\n")
            print("successfully written")
  
    # condition no 2
    elif n == 1 and x == 1 and y == 2:
        value = input("type here\n")
  
        # printing date and time
        with open("Harry_exercise.txt", "a") as Harry_exercise:
  
            # printing date and time
            Harry_exercise.write(str([str(getdate())]) + ": " + value + "\n")
            print("successfully written")
  
    # condition 3
    elif n == 2 and x == 1 and y == 1:
        value = input("type here\n")
  
        # printing date and time
        with open("Rohan_diet.txt", "a") as Rohan_diet:
  
            # printing date and time
            Rohan_diet.write(str([str(getdate())]) + ": " + value + "\n")
            print("successfully written")
  
    # condition 4
    elif n == 2 and x == 1 and y == 2:
        value = input("type here\n")
  
        # printing date and time
        with open("Rohan_exercise.txt", "a") as Rohan_exercise:
  
            # printing date and time
            Rohan_exercise.write(str([str(getdate())]) + ": " + value + "\n")
            print("successfully written")
  
    # condition 5
    elif n == 1 and x == 2 and y == 1:
  
        # printing date and time
        with open("Harry_diet.txt", "r") as Harry_diet:
            a = Harry_diet.read()
            print(a)
  
    # condition no 6
    elif n == 1 and x == 2 and y == 2:
  
        # printing date and time
        with open("Harry_exercise.txt", "r") as Harry_exercise:
            a = Harry_exercise.read()
            print(a)
  
    # condition no 7
    elif n == 2 and x == 2 and y == 1:
  
        # printing date and time
        with open("Rohan_diet.txt", "r") as Rohan_diet:
            a = Rohan_diet.read()
            print(a)
  
    # condition no 8
    elif n == 2 and x == 2 and y == 2:
  
        # printing date and time
        with open("Rohan_exercise.txt", "r") as Rohan_exercise:
            a = Rohan_exercise.read()
            print(a)

n = select_name()
x = select_file_action()
y = select_task()
action(n, x, y)
       


