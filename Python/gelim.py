#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 15:06:41 2024

@author: 55093290
"""
import sympy as sp


def gelimPP(A):
    m, n = A.shape;
    
    # Set pivot row to 1
    k = 0
    
    # Loop through columns
    for j in range(n):
        
        # Find the pivot row
        max_pivot = k
        for i in range(k + 1, m):
            if abs(A[i,j]) > abs(A[max_pivot,k]):
                max_pivot = i
        
        i = max_pivot
        
        # No pivot in column j so move to next column
        if A[i,j] == 0:
            continue
        
        # Swap rows i and k
        A[i,:], A[k,:] = A[k,:], A[i,:]
        
        # Eliminate element below pivot
        for i in range (k + 1, m):
            A[i,:] = A[i,:] - A[i,j] / A[k,j] * A[k,:]
            
        k += 1
            
    return A


def augmented_latex(A):
    m, n = A.shape
    string = f"       \\left( \\begin{{array}}{{{'c'*(n-1)}|c}} \n"
    for i in range(m - 1):
        string += "           "
        for j in range(n - 1):
            string += f"{sp.latex(A[i,j])} & "
        
        string += f"{sp.latex(A[i,j+1])}"
        string += " \\\ \n"

    string += "           "
    for j in range(n - 1):
        string += f"{sp.latex(A[i+1,j])} & "
    
    string += f"{sp.latex(A[i+1,j+1])}"
    string += " \n"
    string += f"       \\end{{array}} \\right) \n"
    return string

def row_swap(A, row1, row2):
    m = A.shape[0]
    string = "       \\begin{matrix} \n"
    for i in range(row1 - 1):
        string += "\\phantom{x} \\\ \n"
    
    string += f"           R_{{{row1 + 1}}} \leftrightarrow R_{{{row2 + 1}}} \\\ \n"
    for i in range(row1+1, m):
        string += "           \\pantom{x} \\\ \n"
        
    string += "       \\end{matrix} \n"
    return string
    

def gelimPP_latex(A):
    m, n = A.shape;
    
    # Set pivot row to 1
    k = 0
    
    # Output preamble
    string = "$$ \\begin{align*} \n"
    string += augmented_latex(A)
    
    # Loop through columns
    for j in range(n):
        
        # Find the pivot row
        max_pivot = k
        for i in range(k + 1, m):
            if abs(A[i,j]) > abs(A[max_pivot,k]):
                max_pivot = i
        
        i = max_pivot
        
        # No pivot in column j so move to next column
        if A[i,j] == 0:
            continue
        
        # Swap rows i and k
        A[i,:], A[k,:] = A[k,:], A[i,:]
        string += row_swap(A, k, i)
        
        # Eliminate element below pivot
        for i in range (k + 1, m):
            A[i,:] = A[i,:] - A[i,j] / A[k,j] * A[k,:]
            
        k += 1
            
    return string


A = sp.Matrix([[ 1, -1, 3],
              [ 4, -2, 1], 
              [-3, -1, 4]])
b = sp.Matrix([[13],[15],[8]])

Ab = A.row_join(b)


string = gelimPP_latex(A)

print(string)