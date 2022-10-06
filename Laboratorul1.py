#ex.1
#pentru mai multe numere

# def gcd(a, b):

#      if(b == 0):
#          return abs(a)
#      else:
#          return gcd(b, a % b)

# n1= int(input("Introduceti primul numar:\n"))
# n2= int(input("Introduceti cel de-al doilea numar:\n"))

# print(gcd(n1,n2))

#ex.2
  
# sir = str(input("Introduceti sirul:\n"))  

# def nrvocale(sir):

#     nr = 0
#     for i in range(0,len(sir)):    
#         if sir[i] in ('a',"e","i","o","u","A","E","I","O","U"):  
#             nr += 1
#     return nr

# print(nrvocale(sir)) 

# ex.3

firststring = str(input("Introduceti primul sir:\n"))
secondstring = str(input("Introduceti cel de-al doilea sir:\n"))

print(secondstring.count(firststring))

