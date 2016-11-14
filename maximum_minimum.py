# First define a function called 'find_max_min' that takes a parameter 'm'
def find_max_min(m):
    # then an empty list is created and assigned to variable 'a'
    a = []
    # make the first element in the list be a minimum by assumption
    mini = m[0]
    # loop through 'm' which is a list of numbers
     for i in m:
        if i < mini:
            # Should i be less than the element preceding it, make it the minimum
            mini= i
    # Next step is to append the minimum value to the empty list created 'a'
    a.append(mini)
    ''' The next step is to make an assumption that the first element
     in the list is the maximumand assign it to variable "maxi"
    '''
    maxi = m[0]
    for j in m:
        if j > maxi:
            ''' After looping, if it should happen that the next 
            element is greater than maxi, then reassign the value of the 
            variable maxi to be that next element
            '''
            maxi = j
    a.append(maxi)
    ''' Check if the numbers are equal in the string provided, 
    In the case that they are all equal, return only one of them
    '''
    if a[0] == a[1]:
        a.remove(a[0])
    return a