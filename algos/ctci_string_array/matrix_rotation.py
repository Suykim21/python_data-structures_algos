# Given an image represented by an NxN matrix, wrtie a method to rotate the image by 90 degrees.
# Time Complexity - O(n^2) - 2 for loops lopping through the entire input matrix for each element

from copy import deepcopy

def rotateMatrix(matrix, n):
    res = deepcopy(matrix) # res will be our original matrix rotated 90 degrees
    for x in range(0, n):
        for y in range(n-1, -1, -1):
            res[x][n-y-1] = matrix[y][x]
    return res

n = 3
matrix = [[1,2,3], [4,5,6], [7,8,9]]
#  res = [[_,_,_], [_,_,_], [_,_,_]]
print("Original Matrix: " + str(matrix))
print("Rotated Matrix: " + str(rotateMatrix(matrix, n)))


# CTCI formal approach without python modules:
def rotate_matrix(matrix):
    '''rotates a matrix 90 degrees clockwise'''
    n = len(matrix)

    for layer in range(n // 2):
        print(n)
        first, last = layer, n - layer - 1

        for i in range(first, last):
            # save top
            top = matrix[layer][i]

            # left -> top
            matrix[layer][i] = matrix[-i - 1][layer]

            # bottom -> left
            matrix[-i - 1][layer] = matrix[-layer - 1][-i - 1]

            # right -> bottom
            matrix[-layer - 1][-i - 1] = matrix[i][- layer - 1]

            # top -> right
            matrix[i][- layer - 1] = top
    return matrix

print(rotate_matrix([[3,4,5],[6,7,4],[1,3,4]]))

"""By Kelly O'Shaughnessy
Rotate nxn matrix by 90 degrees"""
# review this code later
def rotate(matrix):
    if matrix is None or len(matrix)<1:
        return
    else:
        if len(matrix)==1:
            return matrix
        else:
            #solution matrix
            soln = [row[:] for row in matrix]
            #size of matrix
            m = len(matrix[0])
                    
            for x in range(0,m):
                for j in range(0,m):
                    soln[j][m-1-x] = matrix[x][j]
            return soln

if __name__=="__main__":
    six = [["a","b","c"],
          [1,2,3],
          ["x","y","z"]]
    print "%s" % rotate(six)