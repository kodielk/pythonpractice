allStudentInfo =[]
lines =[]
for l2 in lines:
    studentInfo = l2.replace('\n','').split(',')
    t1 =(studentInfo[0], studentInfo[1], int(studentInfo[2]))
    allStudentInfo.append(t1)
#^^ make it go to 5 and muck about with the int conversion
#search
inputUser=101
for singlestuInfo in allStudentInfo:
    if inputUser == singlestuInfo[0]:
        print(singlestuInfo)
        '''now give up just give up :3'''