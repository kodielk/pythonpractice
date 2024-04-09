#put the file name in here l8r

lineInfo=[]
with open ('ALG.txt','r') as fRead:
    count = 0
    for line in fRead.readlines:
        if count ==10:
            break
        [content, lineNumber] = line.replace('\n','').split('|')
        lineInfo.append((int(lineNumber),len(content),content))
        count+=1
    lineInfo.sort()
    print(lineInfo)
#avg
lengthList=[]    
for item in lineInfo:
        _, length, _ =item
        lengthList.append(lengthList)
print(sum(tuple(lengthList)))/len(lineInfo)
#print(sum/len(lineInfo))
'''   
     _
    ('=   _     _     _     _     _
    /_)  >')   >')   >')   >')   >')
   /||  <(_)> <(_)> <(_)> <(_)> <(_)>
   '''
