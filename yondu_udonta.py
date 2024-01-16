'''
    this gets the two inputs we need from the user: number of crewmembers and units.
'''
crewNumber=(int(input('enter number of crew')))
portUnits=(int(input('enter number of units recieved at the port')))

#crew's initial share calculations
crewShare=crewNumber*3
crewRemaining=crewNumber - 2
remainingUnits=portUnits-crewShare

#calculating yondu's and quill's share (before their "crew share")
yonduShare=((remainingUnits*0.13))
remainingUnits=(remainingUnits-yonduShare)
quillShare=(remainingUnits*0.11)
remainingUnits=(remainingUnits-quillShare)

#calculating the crew's residual share
crewShare=(remainingUnits/crewNumber)

#final yondu and quill share calc
yonduShare=(yonduShare+crewShare)
quillShare=(quillShare+crewShare)
#crew share calc
crewShare=(crewShare+3)

#arguably a smarter, future elise will put the rounding everywhere!!

#bing bang boom the final print
print("Yondu's Share: "+ (str(yonduShare)))
print("Quill's Share:" + (str(quillShare)))
print("Crew's Share: "+(str(crewShare)))









