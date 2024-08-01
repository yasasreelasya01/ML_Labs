# Write a program that accepts two matrices A and B as input and returns their product AB.
#Check if A & B are multipliable; if not, return error message.

def mult(A, B):
    res = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                res[i][j] += A[i][k] * B[k][j]

    return res

def count(str):
    str = str.lower()
    vowel = 0
    cons = 0
    for s in str:
        if not s.isalpha():
            print('The string should contain only alphabets')
        elif s in ['a', 'e', 'i', 'o', 'u']:
            vowel = vowel + 1
        else:
            cons = cons + 1
    return vowel, cons

def common(A, B):
    count = 0
    for i in A:
        if i in B:
            count += 1

    return count

def transpose(A):
    transposed_matrix = [[0 for _ in range(len(A))] for _ in range(len(A[0]))]
    for i in range(0, len(A)):
        for j in range(len(A[0])):
            transposed_matrix[i][j] = A[j][i]

    return transposed_matrix

def main():

    string = input('Enter a string to count the number of vowels and consonants: ')
    a, b = count(string)
    print(f'The count of vowels is: {a} The count of consonants is: {b}')

    matA = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matB = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3]]
    res2 = mult(matA, matB)
    print('The multiplication of matrices is: ')
    for i in range(0, len(res2)):
        for j in range(0, len(res2[0])):
            print(f'{res2[i][j]} ', end='')
        print("")

    A3 = [1, 2, 3, 4, 5]
    B3 = [2, 3, 4]
    res3 = common(A3, B3)
    print(res3)


    A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    res4 = transpose(A)
    for i in range(0, len(res4)):
        for j in range(len(res4[0])):
            print(f'{res4[i][j]} ', end='')
        print("")

main()