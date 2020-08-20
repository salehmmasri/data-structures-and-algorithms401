def sum_arrays(any_array):

    list_of_sumation=[]
    for i in range(len(any_array)):
        sumation=0
        try:    
            for j in range(len(any_array[i])):
                sumation+=any_array[i][j]
                print(sumation)
        except:
            return "this is not array of arrayes"
        list_of_sumation.append(sumation)
    return list_of_sumation        
            


  



print(sum_arrays([1,2,3]))