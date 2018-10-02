# Given a square matrix, calculate the absolute difference between the sums of its diagonals.
def diagonalDifference(arr):
    oneArr = []
    twoArr = []
    for i, j in zip(range(len(arr)), range(len(arr))):
        oneArr.append(arr[i][j])
    for i, j in zip(range(len(arr)), reversed(range(len(arr)))):
        twoArr.append(arr[i][j])
    return abs(sum(oneArr) - sum(twoArr))
