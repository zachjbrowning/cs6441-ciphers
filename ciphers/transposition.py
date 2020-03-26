import string
import math as m

def bestMatrix(length):
    square = m.ceil(m.sqrt(length))
    if square * (square - 1) >= length:
        return square, square - 1
    else:
        return square, square

def makeMatrix(message):
    rows, columns = bestMatrix(len(message))
    message += ' ' * (rows * columns - len(message))
    msgMatrix = []
    for i in range(rows):
        msgMatrix.append(list(message[i * columns : (i + 1) * columns]))

    return msgMatrix, rows, columns

def makeOrder(key, rows, columns):
    for letter in key:
        if not letter.isalpha():
            raise KeyError("Key must be alphabetic only!")
    rowkey = list((key * m.ceil(rows / len(key)))[:rows])
    rowkey.reverse()
    uniqueRowkey = []
    for i in range(len(rowkey)):
        uniqueRowkey.insert(0, rowkey.pop() + str(i))
    colkey = list((key * m.ceil(columns / len(key)))[:columns])
    uniqueColkey = []
    for i in range(len(colkey)):
        uniqueColkey.insert(0, colkey.pop() + str(i))

    ordColkey = sorted([x for x in uniqueColkey])
    ordRowkey = sorted([x for x in uniqueRowkey])
    colorder = []
    for item in ordColkey:
        colorder.append(uniqueColkey.index(item))
    roworder = []
    for item in ordRowkey:
        roworder.append(uniqueRowkey.index(item))
    return roworder, colorder

#decode is of type bool, if true matrix is decoded
def matrixSwap(matrix, roworder, colorder, decode): 
    index_max = len(colorder) * len(roworder)
    new_matrix = [['' for x in range(len(colorder))] for y in range(len(roworder))]
        
    for k in range(index_max):
        i = k // len(colorder)
        j = k % len(colorder)
        if decode:
            new_matrix[i][j] += matrix[roworder[i]][colorder[j]]
        else:
            new_matrix[roworder[i]][colorder[j]] += matrix[i][j]
    return new_matrix

def transpositionCiphering(key, message, decode):
    matrix, rows, columns = makeMatrix(message)
    roworder, colorder = makeOrder(key, rows, columns)
    codedMatrix = matrixSwap(matrix, roworder, colorder, decode)
    codedMessage = ''
    for row in codedMatrix:
        codedMessage += ''.join(row)
    
    return codedMessage



class transposition:

    def encode(key, message):
        return transpositionCiphering(key, message, False)

    def decode(key, message):
        return transpositionCiphering(key, message, True)
