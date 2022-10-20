#!/usr/bin/env python3

A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

B = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

X = [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]]

for i in range(len(A)):
  for j in range(len(B[0])):
    for k in range(len(B)):
      X[i][j] += A[i][k] * B[k][j]

for i in X:
  print(i)
