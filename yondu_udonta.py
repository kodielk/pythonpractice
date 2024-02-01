
#this gets the two inputs we need from the user: number of crewmembers and units.
crewNumber=(int(input('How many pirates:\n')))
portUnits=(int(input('How many units:\n')))

#crew's initial share calculations
crewRemaining=crewNumber - 2
crewShare=crewRemaining*3
remainingUnits=portUnits-crewShare

#calculating yondu's and quill's share (before their "crew share")
yonduShare=((remainingUnits*0.13))
remainingUnits=(remainingUnits-yonduShare)
remainingUnits=round(remainingUnits,2)

#quill's share
quillShare=(remainingUnits*0.11)
remainingUnits=(remainingUnits-quillShare)
remainingUnits=round(remainingUnits,2)

#calculating the crew's residual share
crewShare=(remainingUnits/crewNumber)
crewShare=(round(crewShare,2))

#final yondu and quill share calculations
yonduShare=(yonduShare+crewShare)
yonduShare=round(yonduShare,2)

#quill's share calculations
quillShare=(quillShare+crewShare)
quillShare=round(quillShare,2)

#3 more units for the original units given 
crewShare=(crewShare+3)

#bing bang boom the final print
print("Yondu's share: \n"+ (str(yonduShare)))
print("Peter's share: \n" + (str(quillShare)))
print("Crew's share: \n"+(str(crewShare)))


'''i honestly do not know why the crew units needs an extra +3 at the end when they were already multiplied by 3 
at the beginning. it works, and that what matters, but i'm still confused.
'''






