#Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4
#bytes, write a method to rotate the image by 90 degrees. Can you do this in place?
 # Consider all squares one by one

        # Consider elements in group
        # of 4 in current square
def rotate90(matrix,N):
    # Creates a list containing 5 lists, each of 8 items, all set to 0

    #PRINTING BEFORE
    for x in range(N):
        for y in range(N):
            print(matrix[x][y],end=" ")
        print()

    matrix = matrix[::-1] #Reverse the matrix first or you can use matrix.reverse() too

    for x in range(N):
        for y in range(x):
            matrix[x][y],matrix[y][x] = matrix[y][x], matrix[x][y] #swap

    print()
    print()
    #PRINTING AFTER
    for x in range(N):
        for y in range(N):
            print(matrix[x][y],end="  ")
        print()


def main():
    arr = [[1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]

    rotate90(arr,4)

if __name__ == '__main__':
    main()
