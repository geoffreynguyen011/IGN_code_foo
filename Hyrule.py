startDate = 0
duration = 0
rupees = 0
maxDays = 31

totalCurrDays = 0
startDateArray = [1, 2, 1, 3, 5, 3, 7, 12, 6, 19, 23, 14, 8, 20, 28, 10, 13, 25, 9, 16, 4, 11, 7, 2]
durationArray = [3, 2, 4, 8, 1, 4, 5, 3, 8, 2, 7, 4, 3, 7, 3, 4, 6, 4, 1, 10, 5, 3, 2, 23]
rupeesArray = [750, 500, 920, 1050, 200, 400, 1200, 370, 840, 165, 1520, 600, 430, 1100, 590, 900, 230, 1120, 460, 780, 410, 570, 1200, 2100]
arrayOfDays = []
i = 0

def questsToChoose():
    mostEfficientArray = [0] * len(durationArray)
    totalRupees = 0
    
    for i in range(len(durationArray)):
        mostEfficientArray[i] = rupeesArray[i] / durationArray[i]
    # most efficient array now has rupees per day
    
    
    for i in range(len(startDateArray)):
        dayAlreadyBusy = False
        val = 0
        index = 0
        for j in range(len(mostEfficientArray)):
            if (mostEfficientArray[j] > val):
                index = j
                val = mostEfficientArray[j]
        
        # highest value now found
        print(range(startDateArray[index], startDateArray[index] + durationArray[index] - 1))
        for k in range(startDateArray[index], startDateArray[index] + durationArray[index]):
            #print(k)
            if k in arrayOfDays:
                dayAlreadyBusy = True
        #print(totalRupees)
        print(dayAlreadyBusy)
        if dayAlreadyBusy == False:
            totalRupees += rupeesArray[index]
            for k in range(durationArray[index]):
                arrayOfDays.append(startDateArray[index] + k)
            #print("HELLO")
        #print("Array of days: ")
        #print(arrayOfDays)
        mostEfficientArray[index] = 0
        
    
    print(totalRupees)
    print(arrayOfDays)
    #print(mostEfficientArray)
    #print(val)

questsToChoose()



ranArray = [1, 2, 3, 4, 5, 6, 7, 8]

if (2, 3) not in ranArray:
    print("Hello")




