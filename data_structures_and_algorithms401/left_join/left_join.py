def left_join(dec1,dec2):
    """
    Function takes tow dictionaries and return new dictionary 
    with joining the values for the same key in these tow dictionaries as a list of values
    """
    
    new_dect = {}

    for k in dec1:
        new_dect[k] = [dec1[k]]
        val = None
        if k in dec2:
            val= dec2[k]
        new_dect[k].append(val)
    return new_dect    

