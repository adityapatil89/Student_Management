students = {}
student_ids = []

def add_record(std_id, std_name, std_age, std_grade):
    students[std_id] = (std_name, std_age, std_grade)
    student_ids.append(std_id)
    print("Record Inserted Successfully!")

def view_records():
    if not students:
        print("No records found.")
        return
    print("Student Id\tName\tAge\tGrade")
    for std_id in student_ids:
        view_name, view_age, view_grade = students[std_id]
        print(f"{std_id}\t\t{view_name}\t{view_age}\t{view_grade}")

def search_record(std_id):
    search_result = students.get(std_id)
    if search_result:
        search_name, search_age, search_grade = search_result
        print(f"Search Result - ID: {std_id}, Name: {search_name}, Age: {search_age}, Grade: {search_grade}")
    else:
        print(f"Error: Student ID {std_id} not found.")

def update_record(std_id, std_name, std_age, std_grade):
    if std_id in students:
        students[std_id] = (std_name, std_age, std_grade)
        print("Record Updated Successfully!")
    else:
        print("Error: Student ID not found.")

def delete_record(std_id):
    if std_id in students:
        del students[std_id]
        student_ids.remove(std_id)
        print("Record Deleted Successfully!")
    else:
        print("Error: Student ID not found.")

while True:
    try:
        num = int(input("\n    1. Add Student Record\n    2. View All Students\n    3. Search Student\n    4. Update Student Information\n    5. Delete Student Record\n    6. Exit\n==> "))
        
        if num == 1:
            std_id = int(input("Enter the student's id: "))
            std_name = input("Enter the student's name: ")
            std_age = int(input("Enter the student's age: "))
            std_grade = input("Enter the student's grade: ")
            add_record(std_id, std_name, std_age, std_grade)

        elif num == 2:
            view_records()

        elif num == 3:
            std_id = int(input("Enter the id to be searched: "))
            search_record(std_id)

        elif num == 4:
            std_id = int(input("Enter the student's id: "))
            std_name = input("Enter the student's name: ")
            std_age = int(input("Enter the student's age: "))
            std_grade = input("Enter the student's grade: ")
            update_record(std_id, std_name, std_age, std_grade)

        elif num == 5:
            std_id = int(input("Enter the id to be deleted: "))
            delete_record(std_id)

        elif num == 6:
            print("Exiting the program...")
            break

        else:
            print("Invalid option! Please enter a number between 1 and 6.")
    
    except ValueError:
        print("Error: Please enter valid numerical values where required.")
