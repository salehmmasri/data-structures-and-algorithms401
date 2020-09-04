def multi_bracket_validation(input):
    """
    function to cheack if we have any extra  or missing Bracket or parenthesis or curly braces 
     
    """
    open_list = ["[","{","("]
    close_list = ["]","}",")"]
    stack = []
    for i in input:
        if i in open_list:
            stack.append(i)
            
        elif i in close_list:
            index_position = close_list.index(i)
            if ((len(stack) > 0) and (open_list[index_position] == stack[len(stack)-1])):
                stack.pop()
            else:
                return False
    if len(stack) == 0:
        # len stack == 0 then we don't have any extra Bracket or parenthesis or curly braces  
        return True
    else:
        return False
if __name__ == "__main__":
    # inp='{()[[Extra Characters]]}'
    print(multi_bracket_validation('}'))