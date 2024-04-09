import sys
def logEq(growR, initPop):
    return growR * initPop * (1 - initPop)

def main():
    timeN=0
    initPop = float(sys.argv[1])
    growR = float(sys.argv[2])
    iterNum = float(sys.argv[3])
    outputFile =str(sys.argv[4])
    populations=[]
    if initPop<0 or initPop>1:
        print("Initial population number must be between 0 and 1")
        return
    
    if growR<0 or growR>4:
        print("Growth rate must be between 0 and 4")
        return
    
    if iterNum <0:
        print("Iteration number is negative.")
        return
    populations.append(initPop)
    while timeN<iterNum+1:
        popTotal = logEq(growR,initPop)
        initPop=popTotal
        populations.append(popTotal)
        timeN+=1 
    with open(outputFile, "w") as file:
        for population in populations:
            print(populations.index(population), f"{population:.3f}", file=file)
if __name__ == "__main__":
    main()