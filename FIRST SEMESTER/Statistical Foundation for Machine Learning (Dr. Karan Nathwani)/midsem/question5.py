# install sympy
#! pip install sympy
 
# import sympy
import sympy
 
# find the reduced row echelon form
print(sympy.Matrix([[0,1,4],[1,2,-1],[5,8,0]]).rref())
 
# find the rank of matrix
print("Rank of matrix :",sympy.Matrix([[0,1,4],[1,2,-1],[5,8,0]]).rank())