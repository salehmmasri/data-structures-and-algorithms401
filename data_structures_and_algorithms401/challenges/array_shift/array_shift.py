import math

def insertShiftArray(inputArr,val):
    x=len(inputArr)
    if x % 2 ==0:
        x//=2
        inputArr.insert(x,val)
        print(x,inputArr)
    else:
        x/=2
        x=int(math.ceil(x))
        inputArr.insert(x,val)
        print(x,inputArr)
        
    # n = len(inputArr)
    # for i in range(n):
    #     for j in range(n):
    #         if  inputArr[i] < inputArr[j]:
    #             temp=inputArr[j]
    #             inputArr[j]=inputArr[i]
    #             inputArr[i]=temp
    return inputArr        
                    
print(insertShiftArray([4,8,15,23,42], 16))