
def readMatrix(filename):

    try:
        matrix = []
        with open(filename, 'r') as f:
            for line in f:
                row = list(map(float, line.split()))
                matrix.append(row)
        return matrix
    except FileNotFoundError:
        return None  # якщо файл не існує, то повертаємо None

def writeMatrix(M, filename):
    with open(filename, 'w') as f:
        for i in range(len(M)):
            for j in range(len(M[0])):
                print(M[i][j], end=" ", file=f)
            print(file=f)

if __name__ == '__main__':
    M = readMatrix('matrix.txt')
    print(M)
    writeMatrix(M, 'matrix_out.txt')
