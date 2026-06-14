students = []
def store():
    name = input("Enter the name: ")
    roll = input("Enter the roll: ")
    std = input("Enter the class: ")
    students.append({
        'name': name,
        'roll': roll,
        'std': std
    })
    print("Student stored successfully!")

def search():
    roll = input("Enter roll to search: ")
    for student in students:
        if student['roll'] == roll:
            print(f"Student Roll: {student['roll']}, Student Name: {student['name']}, Class: {student['std']}")
            return
    print("Student not found")

def display():
    if not students:
        print("No students found")
        return
    for student in students:
        print(f"Roll: {student['roll']}, Name: {student['name']}, Class: {student['std']}")

def remove():
    roll = input("Enter roll to delete: ")
    for student in students:
        if student['roll'] == roll:
            students.remove(student)
            print("Student removed successfully!")
            return
    print("Student not found")

def calculator():
    operator = input("Choose the opeator(+,-,*,%,/): ")
    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))
    if operator == "+":
        print("Operator: Addition")
        print("Output:", a + b)

    elif operator == "-":
        print("Operator: Minus")
        print("Output:", a - b)

    elif operator == "*":
        print("Operator: Multiplication")
        print("Output:", a * b)

    elif operator == "%":
        print("Operator: Remainder")
        print("Output:", a % b)

    elif operator == "/":
        print("Operator: Divided")
        print("Output:", a / b)

    else:
        print("Invalid operator")

lists = []
def to_do_list():
    task = input("Enter task: ")
    lists.append(task)
    print("Task added")
    print(lists)
 

while True:
    print("------------------Student Mangement System---------------------------")
    print("1.Registraion, 2.calculator, 3.To do list ")
    Mangement = input("Choose Any one Mangement: ")
    if Mangement=="1":
        print("-----------Registration-----------")
        print("\nChoose any : a.Store  b.Search  c.Display  d.Delete e.Exit: ")
        choice = input("Enter the Registration choice(a,b,c,d,e): ")
        if choice=="a":
          store()

        elif choice=="b":
          search()

        elif choice=="c":
          display()

        elif choice=="d": 
         remove()

        elif choice=="e":
         print("Exit")
         break
    elif Mangement=="2":
       print("---------Calculator--------------")
       calculator()

    elif Mangement=="3":
       print("-------------To do list-------------")
       to_do_list()
    else:
        print("Invalid Choice")