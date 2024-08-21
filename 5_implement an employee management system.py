class Employee:
    def __init__(self, emp_id, name, pos, sal):
        self.emp_id, self.name, self.pos, self.sal = emp_id, name, pos, sal

    def display(self):
        print(f"ID: {self.emp_id} | Name: {self.name} | Pos: {self.pos} | Salary: ₹{self.sal:.2f}\n" + "-"*30)

class EMS:
    def __init__(self):
        self.emps = {}

    def add(self, emp_id, name, pos, sal):
        self.emps[emp_id] = Employee(emp_id, name, pos, sal)
        print(f"Added: {name}")

    def remove(self, emp_id):
        if self.emps.pop(emp_id, None):
            print(f"Removed ID: {emp_id}")
        else:
            print("ID not found")

    def display_all(self):
        if self.emps:
            for e in self.emps.values():
                e.display()
        else:
            print("No employees")

ems = EMS()
while True:
    c = input("\n1.Add 2.Remove 3.Display 4.Exit: ")
    if c == '1':
        emp_id = int(input("Enter Employee ID: "))
        name = input("Enter Name: ")
        position = input("Enter Position: ")
        salary = float(input("Enter Salary: "))
        ems.add_employee(emp_id, name, position, salary)

    elif c == '2':
        emp_id = int(input("Enter Employee ID to remove: "))
        ems.remove_employee(emp_id)

    elif c == '3':
        ems.display_all_employees()

    elif c == '4':
        print("Exiting Employee Management System. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a valid option.")