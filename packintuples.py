def packing(all_info, student):
    file_path = r"C:\Users\babyc\OneDrive\Documents\GitHub\pythonpractice\textfiles\gpa-3.csv"
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            student_info = tuple(parts)
            all_info.append(student_info)

        #there's probably a sleeker way to do this, but i'm tired. 
        alex_data = all_info[1]
        peter_data = all_info[2]
        yoon_data = all_info[3]
        zack_data = all_info[4]
        susan_data = all_info[5]
        if int(input_num) == 101:
            student.append(alex_data)
            student = tuple(student)
            print(student)
        elif int(input_num) == 102:
            student.append(peter_data)
            student = tuple(student)
            print(student)
        elif int(input_num) == 103:
            student.append(yoon_data)
            student = tuple(student)
            print(student)
        elif int(input_num) == 104:
            student.append(zack_data)
            student = tuple(student)
            print(student)
        elif int(input_num) == 105:
            student.append(susan_data)
            student = tuple(student)
            print(student)
    return all_info, student

def unpacking(student):
    for item in student:
        
            print("Student ID =", item[0])
            print("Student Name=", item[1])
            print("Age=", item[2])
            print("GPA=",item[3],item[4],item[5],item[6],item[7])

input_num = input("Input a number: ")
all_info = []
student = []
all_info, student = packing(all_info, student)
unpacking(student)
