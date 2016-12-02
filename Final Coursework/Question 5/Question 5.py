###QUESTION 5###

"""

Addition Function:

FUNCTION matrixAddition(matrixB,matrixC):
        for I in 0 to order n:
            for J in 0 to order n:
                matrixA(I,J) = matrixB(I,J) + matrixC(I,J)
        OUTPUT matrixA


SUBTRACTION Function:

FUNCTION matrixSubtraction(matrixB,matrixC):
        for I in 0 to order n:
            for J in 0 to order n:
                matrixA(I,J) = matrixB(I,J) - matrixC(I,J)
        OUTPUT matrixA


MULTIPLICATION Function:

FUNCTION matrixMultiplication(matrixB,matrixC):
        for I in 0 to order n:
            for J in 0 to order n:
                matrixA = 0
                for K in 0 to order n:
                    matrixA(I,J) = matrixA(I,J) + matrixB(I,K) * matrixC(K,J)
        OUTPUT matrixA

COMPUTATION OF : A=B*C –2*(B+C)

D = matrixMultiplication(B,C) # For B*C
E = matrixAddition(B,C) # For (B+C)
F = matrixAddition(E,E) # For 2*(E)
A = matrixSubtraction(D,F) # For D–F

Big O Notation:
The big o notaion for this question would be 0(N^3). This is due to the
triple nested for loop in the matrixMultiplication.

"""
