import sys

def sort(list):
    for i in range(0, len(list)):
        for j in range(i+1, len(list)):
            if list[i] >= list[j]:
                list[i], list[j] = list[j], list[i]
    return list

def mean(list):
    sumList = sum(list)
    length = len(list)
    avg = sumList / length
    print("Average:", avg)
    return avg

def minimum(list):
    minNum = float('inf')
    for num in list:
        if num < minNum:
            minNum = num
    print("Min:", minNum)
    return minNum

def maximum(list):
    maxNum = -float('inf')
    for num in list:
        if num > maxNum:
            maxNum = num
    return(maxNum)
course_data = []

def main():
    with open(r'C:\Users\babyc\OneDrive\Documents\GitHub\pythonpractice\otherfiles\input.csv', 'r') as file:
        for line in file:
            values = line.strip().split(',')
            course_data.append(values)
    with open(r'C:\Users\babyc\OneDrive\Documents\GitHub\pythonpractice\otherfiles\output.csv','w') as outputFile:
        for course in course_data[1:]:
            course_grades = [int(grade) for grade in course[1:]]
            maxGrade=maximum(course_grades)
            minGrade=minimum(course_grades)
            avgGrade=mean(course_grades)
            outputFile.write(f"course: {course[0]}\n")
            outputFile.write(f"maximum:{maxGrade}\n")
            outputFile.write(f"minimum:{minGrade}\n")
            outputFile.write(f"mean; {avgGrade}\n")
            sortedGrade=sort(course_grades)
            outputFile.write(f"sorted grades:{sortedGrade}\n")
            
            

if __name__ == "__main__":
    main()
