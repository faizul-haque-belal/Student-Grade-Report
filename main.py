"""
=================================================
Student Grade Report

Author : Md Faizul Haque Belal
Language : Python 3

Features
---------
- Student Information
- Grade Calculation
- Highest Marks
- Lowest Marks
- Average Marks
- Pass Count
- Fail Count
=================================================
"""
# Main function
def main():
    students=int(input("Enter the numbers of student: "))
    students_data=[]
    for student in range(students):
        name=input("Enter your Name: ")
       
        while True:
            marks=int(input("Enter your Marks: "))
            if 0<= marks <=100:
                break
            else:
                print("Invalid Marks! Please enter your correct marks:")
        grade=get_grade(marks)

        students_data.append({"Name": name, 
                              "Marks": marks, 
                              "Grade": grade})
    display_report(students_data)

    highest=get_highest(students_data)
    print(f"Highest:{highest}")

    lowest=get_lowest(students_data)
    print(f"Lowest:{lowest}")

    average=get_average(students_data)
    print(f"Average:{average}")

    pass_count=get_pass_count(students_data)
    print(f"Pass_count:{pass_count}")

    fail_count=get_fail_count(students_data)
    print(f"Fail_count:{fail_count}")

## Display all students

def display_report(students_data):
    print("-"*60)
    for student in students_data:
        print(student["Name"])
        print(student["Marks"])
        print(student["Grade"])
#Return highest marks student 
     
def get_highest(students_data):
    highest=students_data[0]

    for student in students_data:
        if student["Marks"] > highest["Marks"]:
            highest=student
    return highest

# Return lowest marks student  
def get_lowest(student_data):
    lowest=student_data[0]
    for student in student_data:
        if student["Marks"] < lowest["Marks"]:
            lowest=student
    return lowest
# Calculate average marks
def get_average(student_data):
    total=0
    for student in student_data:
        total +=student["Marks"]
    get_average=total/len(student_data)
    return get_average
# Count pass students  
def get_pass_count(students_data):
    count=0
    for student in students_data:
        if student["Marks"]>=33:
            count +=1
    return count
# Count fail students
def get_fail_count(students_data):
    count=0
    for student in students_data:
        if student["Marks"]<33:
            count +=1
    return count

def get_grade(marks):
    if marks >=80 :
        return "A+"
    elif marks >=70 :
        return "A"
    elif marks >=60 :
        return "A-"
    elif marks >=50 :
        return "B"
    elif marks >=40 :
        return "C"
    elif marks >=33 :
        return "D"
    else:
        return "F"
if __name__ == "__main__":
    main()

