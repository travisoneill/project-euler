with open('067.txt', 'r') as f:
    array = []
    for line in f:
        array.append( list(map(int, line.split(' '))) )

    for row in reversed(range(len(array) - 1)):
        print(array[row])
        for n in range(len(array[row])):
            array[row][n] += max(array[row+1][n], array[row+1][n+1])
        print(array[row])

    print(array[0][0])
