class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

class EmployeeDatabase:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def search_by_age(self, operator, value):
        results = []
        for employee in self.employees:
            if operator == ">" and employee.age > value:
                results.append(employee)
            elif operator == "<" and employee.age < value:
                results.append(employee)
            elif operator == ">=" and employee.age >= value:
                results.append(employee)
            elif operator == "<=" and employee.age <= value:
                results.append(employee)
        return results

    def search_by_salary(self, operator, value):
        results = []
        for employee in self.employees:
            if operator == ">" and employee.salary > value:
                results.append(employee)
            elif operator == "<" and employee.salary < value:
                results.append(employee)
            elif operator == ">=" and employee.salary >= value:
                results.append(employee)
            elif operator == "<=" and employee.salary <= value:
                results.append(employee)
        return results

    def search_by_employee_id(self, emp_id):
        results = []
        for employee in self.employees:
            if employee.emp_id == emp_id:
                results.append(employee)
        return results

def main():
    database = EmployeeDatabase()
    
    database.add_employee(Employee("161E90", "Raman", 41, 56000))
    database.add_employee(Employee("161F91", "Himadri", 38, 67500))
    database.add_employee(Employee("161F99", "Jaya", 51, 82100))
    database.add_employee(Employee("171E20", "Tejas", 30, 55000))
    database.add_employee(Employee("171G30", "Ajay", 45, 44000))

    while True:
        print("\nMenu:")
        print("1. Search by Age")
        print("2. Search by Salary")
        print("3. Search by Employee ID")
        print("4. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            operator = input("Enter operator (>, <, <=, >=): ")
            value = int(input("Enter age value: "))
            results = database.search_by_age(operator, value)
        elif choice == "2":
            operator = input("Enter operator (>, <, <=, >=): ")
            value = int(input("Enter salary value: "))
            results = database.search_by_salary(operator, value)
        elif choice == "3":
            emp_id = input("Enter Employee ID: ")
            results = database.search_by_employee_id(emp_id)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")
            continue

        if not results:
            print("No matching records found.")
        else:
            print("\nMatching Records:")
            for employee in results:
                print(f"Employee ID: {employee.emp_id}, Name: {employee.name}, Age: {employee.age}, Salary: {employee.salary}")

if __name__ == "__main__":
    main()
