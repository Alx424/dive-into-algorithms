# calculates the position of a ball using the equation y=vt+(at²)/2 
# where 'v' represents the starting speed of the ball and 'a' is the constant downward acceleration of the ball due to gravity

def gdc(x,y):
    larger = max(x,y)
    smaller = min(x,y)
    remainder = larger % smaller

    if(remainder == 0):
        return(smaller)
    if(remainder != 0):
        return(gdc(smaller,remainder))
    
print(gdc(105, 33))