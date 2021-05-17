# Python functions that accepts a string and calculate the number of upper case letters and lower case letters.

def myfunction(mystring):
    num={"UPPER_CASE":0, "LOWER_CASE":0}
    for char in mystring:
        if char.isupper():
           num["UPPER_CASE"]+=1
        elif char.islower():
           num["LOWER_CASE"]+=1
        else:
           pass
    print ("My String : ", mystring)
    print ("# of Upper case Characters : ", num["UPPER_CASE"])
    print ("# of Lower case Characters : ", num["LOWER_CASE"])

myfunction('SailING Is FuNNy AT Times')