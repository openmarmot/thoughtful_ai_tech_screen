
def sort(width, height, length, mass):
    '''sort a package of the specified dimensions'''
    
    # quick type check that we are receiving numbers
    if (isinstance(width, (int,float)) and 
    isinstance(height,(int,float)) and 
    isinstance(length,(int,float)) and 
    isinstance(mass,(int,float))):
        
        # default to standard
        sort='STANDARD'

        # check mass
        if mass >=20:
            sort='SPECIAL'

        # check dimensions 
        if (width*height*length>=1000000) or (width + height + length >150):

            # heavy and bulky get rejected
            if sort=='SPECIAL':
                sort='REJECTED'

            else:
                sort='SPECIAL'

        return sort
    else:
        raise TypeError('All parameters must be numbers')


# --- put your test case here ---

# this should be standard
print('Test 1: ',sort(10,10,10,5))

# this should be SPECIAL
print('Test 2: ',sort(10,10,10,20))

# this should be REJECTED
print('Test 3: ',sort(100,100,100,20))

# this should error out
#print('Test 4: ',sort(10,10,10,'bob'))