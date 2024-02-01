try:
    dividend=(int(input('dividend: \n')))
except:
    print('ERROR: inputs are not valid. are you trying to ruin my life?')
try:
    divisor=(int(input('divisor: \n')))
except:
    print('ERROR: inputs are not valid. are you trying to ruin my life?')
    

calcFloat=(dividend/divisor)    
calcInteger=(dividend//divisor)
print('This is the result in a float: ', calcFloat)
print('This is the result in an integer:', calcInteger)