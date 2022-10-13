#ex.1

def gcd(a, b):

     if(b == 0):
         return abs(a)
     else:
         return gcd(b, a % b)

list = []

n=int(input("List size is: "))
for i in range(0,n):
    list.append(int(input("Introduceti elementul:\n")))

firstgcd = gcd(list[0],list[1])
for i in range(2, len(list)):
    finalgcd = gcd(firstgcd, list[i])

print(finalgcd)

#ex.2
  
sir = str(input("Introduceti sirul:\n"))  

def nrvocale(sir):

    nr = 0
    for i in range(0,len(sir)):    
        if sir[i] in ('a',"e","i","o","u","A","E","I","O","U"):  
            nr += 1
    return nr

print(nrvocale(sir)) 

# ex.3

firststring = str(input("Introduceti primul sir:\n"))
secondstring = str(input("Introduceti cel de-al doilea sir:\n"))

print(secondstring.count(firststring))

# ex.4

string = str(input("Introduceti sirul:\n"))

string = ' '.join(cuv.lower() for cuv in string.split('_'))
print(string)

#ex.6

def palindrome(number):

    ogl=0
    copie=number

    while number > 0:
        uc = number % 10
        ogl = ogl * 10 + uc
        number = number // 10

    if copie == ogl:
        print("Is palindrome")
    else:
        print("Isn't palindrome")

print(palindrome(int(input("Introduceti numarul:\n"))))

#ex.7

def number_from_text(string):

    extracted = ""
    for ch in string:
        if ch.isdigit():
            extracted = extracted + ch
    return extracted

string = str(input("Introduceti sirul:\n"))       
print(number_from_text(string)) 

#ex.8

def number_to_binary(number):
    
    binary = bin(number)
    return binary

number=int(input("Introduceti numarul:\n"))

print("The number of bits with value 1 of the given number is:")
print(number_to_binary(number).count('1'))

#ex.9

def most_common_letter(string):
    nr = {}
    max = 0
    for ch in set(string):
       nr[ch] = string.count(ch)
    values = nr.values()
    max = max(values)
    return max

string = str(input("Introduceti sirul:\n")) 
print(most_common_letter(string.lower()))

#ex.10

def word_counter(string):
    count = len(string.split())
    return count

string = str(input("Introduceti sirul:\n"))
print(word_counter(string))