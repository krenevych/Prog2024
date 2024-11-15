
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


if __name__ == '__main__':
    M = readMatrix('matrix.txt')
    print(M)
