def binary_search(my_list, lowest, r, x): 
  
    while lowest <= r: 
  
        mid = lowest + (r - lowest) // 2; 
          
        if my_list[mid] == x: 
            return mid 
  
        elif my_list[mid] < x: 
            lowest = mid + 1
  
        else: 
            r = mid - 1
      
    return -1
  
my_list = [ 10, 20, 30, 40, 50 , 60, 70, 80 ] 
search_for = 100
  
result = binary_search(my_list, 0, len(my_list)-1, search_for) 
  
if result != -1: 
    print (f"Element is present at index {result}") 
else: 
    print ("Element is not present in array") 