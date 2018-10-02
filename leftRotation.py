# Given an array  of  integers and a number, , perform  left rotations on the array. 
# Return the updated array to be printed as a single line of space-separated integers.
def rotLeft(a, d):
    newArr = []
    newArr.append(a[d])
    for i in range(d):
        newArr.append(a[i])
    for i in range(d + 1, len(arr)):
        newArr.append(a[i])
    return newArr
