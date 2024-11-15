from Labs.CompMat_1.lab10.t06 import multiply


def readMatrix(filename):
    try:
        matrix = []
        with open(filename, 'r') as f:
            columns = -1
            for line in f:
                row = list(map(float, line.split()))
                if columns == -1:
                    columns = len(row)
                else:
                    assert columns == len(row), "Matrix has wrong number of columns"
                matrix.append(row)
        return matrix
    except FileNotFoundError:
        return None  # якщо файл не існує, то повертаємо None
    except ValueError:
        print("Error: file contains prohibited characters")
        return None
    except AssertionError as e:
        print(e)
        return None

def writeMatrix(M, filename):
    with open(filename, 'w') as f:
        for i in range(len(M)):
            for j in range(len(M[0])):
                print(M[i][j], end=" ", file=f)
            print(file=f)

if __name__ == '__main__':
    A = readMatrix('matrix_A.txt')
    B = readMatrix('matrix_B.txt')
    try:
        assert A !=None and B != None, "Read from file error"
        assert len(A[0]) == len(B), "Matrix has wrong number of columns"
        M = multiply(A, B)
        print(M)
        writeMatrix(M, 'matrix_out.txt')
    except AssertionError as e:
        print(e)
