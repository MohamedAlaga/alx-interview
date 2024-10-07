def pascal_triangle(n):
    if (n <= 0):
        return []
    totalList = []
    for i in range(n) :
        x = str(pow(11,i))
        totalList.append(list(x))
    return totalList
