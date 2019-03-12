#Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0.

def make_all_zero(matrix,M,N):

#PRINT BEFORE
    for i in range(M):
        for y in range(N):
            print(matrix[i][y],end="")
        print()
    print()
    print()
    # size of matrix n x m
    logMatrix = [ [ 0 for i in range(N) ] for j in range(M) ]

    for i in range(M):
        for y in range(N):
            if matrix[i][y] == 0:
                logMatrix[i][y]= 1 #First I nee to mark the logMatrix that which elemets are zero to not make all matrix zero

    for i in range(M):
        for y in range(N):
            if logMatrix[i][y]==1:
                for a in range(M):
                    matrix[a][y] = 0 # zeroes out column i
                for b in range(N):
                    matrix[i][b] = 0 # zeroes out row i
#PRINT AFTER
    for i in range(M):
        for y in range(N):
            print(matrix[i][y],end="")
        print()

def main():
    matrix = [[1,2,3],[2,4,5],[0,8,0]]
    make_all_zero(matrix ,3,3)

if __name__ == "__main__":
    main()
