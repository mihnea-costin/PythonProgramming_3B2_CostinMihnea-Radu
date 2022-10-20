# 1) 

# def fibonacci(n):
#     if n == 0:
#         return [0]
#     elif n == 1:
#         return [0, 1]
#     else:
#         list = fibonacci(n-1)
#         list.append(list[-1] + list[-2])
#         return list

# print(fibonacci(100))

# 2)

# def is_prime(n):
#   for i in range(2,n):
#     if (n%i) == 0:
#       return False
#   return True

# prime_list = []
# def list_of_prime(list):
#     for num in list:
#         if is_prime(num) == 1:
#             prime_list.append(num)

# list_of_prime([2,3,4,5,6,7])
# print(prime_list)

# 3)

# def list_operations(a,b,option):
#     intersection = [value for value in a if value in b]
#     # difference = a - b

#     if option == 1:
#         return intersection
#     elif option == 2:
#         return a.extend(b)
#     elif option == 3:  
#         c = []
#         for element in a:
#             if element not in b:
#                 c.append(element)
#         return c


# print(list_operations([2,3,4],[3,4,5],3))

# 5)

# def matrix_with_0_diagonal(matrix,m,n):
#      for i in range(m):
#         for j in range(n):
#             # right and left diagonal condition
#             if (i == j or (i + j + 1) == m):
#                 matrix[i][j] = 0
#      print(matrix)

# print(matrix_with_0_diagonal([[1,2,3],[4,5,6],[7,8,9]],3,3))

# 7) 

# def palindrome(a):
    
#     max = 0
#     nr = 0
#     list = []
#     for numar in a:
#         ogl = 0
#         copie = numar
#         while numar > 0:
#             uc = numar % 10
#             ogl = ogl * 10 + uc
#             numar = numar // 10

#         if ogl > max:
#             max = ogl
        
#         if copie == ogl:
#             nr = nr + 1
    
#     first = nr
#     second = max
#     list.append(first)
#     list.append(second)
#     return tuple(i for i in list)

# a = [121,233,331,454,5]
# print(palindrome(a))

# 8)

# def function(x,list,flag):
#     another_list = []
#     for string in list:
#         new_list = []
#         for ch in string:
#             if ord(ch) % x == 0 & flag == 1:
#                 new_list.append(ch)
#             elif ord(ch) % x != 0 & flag == 0:
#                 new_list.append(ch)
#         another_list.append(new_list)    
#     return another_list

# list = ["test", "hello", "lab002"]
# print(function(3,list,0))

# 10)

# def function(*args,n):
#     new_list = []
#     for i in n:
#         list = []
#         list.append(args[i])
#         new_list.append(list)
#     return new_list

# print(function([1,2,3],[4,5,6],n))


# def o_f(a,b) 
# o_f(1,2)
# o_f(a=1,b=2)
# o_f(b=2,a=1)
#    (a,b=2)
#    (1)
#    (1,b=2)
#    (b=2,1) -> gresit

# def o_f(*args,**kwargs)

# 12)

# def group_by_rhyme(words):
#     new_list = sorted(words,key = lambda x:x[-2:]) 
#     return new_list

# print(group_by_rhyme(['ana', 'banana', 'carte', 'arme', 'parte']))
