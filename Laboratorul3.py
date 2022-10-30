# 1) 

# def a_and_b_operations(a, b):
#     c = set(a)
#     d = set(b)
#     intersection = c.intersection(d)
#     union = c.union(d)
#     a_minus_b = c.difference(d)
#     b_minus_a = d.difference(c)
#     return [intersection, union, a_minus_b, b_minus_a]

# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# b = [31,54,22,43,2,3,4,5]

# print(a_and_b_operations(a, b))

# 2) 

# def dictionary_counter(s):
#     d = {}
#     for i in range(len(s)):
#         if s[i] in d:
#             d[s[i]] += 1
#         else:
#             d[s[i]] = 1
#     return d

# print(dictionary_counter("Ana has apples."))

# 3) gata de refacut recursiv

# def dict_compare(d1, d2):
#     if len(d1) != len(d2):
#         return False
#     for i in d1:
#         if i not in d2:
#             return False
#         if d1[i] != d2[i]:
#             return False
#     return True

# d1 = {1: 2, 3: 4, 5: 6}
# d2 = {1: 2, 3: 4, 5: 6}

# print(dict_compare(d1, d2))

# 4) de modificat cu ghilimele, si varianta cu 2 apostrof si ghilimele inauntru

# def build_xml_element(tag, content, **kwargs):
#     xml = "<" + tag
#     for key, value in kwargs.items():
#         xml += ' " ' + key + '=\ \" ' + value
#     xml += '>' + content + '</ \" ' + tag + '>
#     return xml

# print(build_xml_element("a", "Hello there", href =" http://python.org ", _class =" my-link ", id= " someid "))

# 5) 

# def validate_dict(s, d):
#     for key, prefix, middle, suffix in s:
#         if key in d:
#             if prefix != "":
#                 if d[key].startswith(prefix) == False:
#                     return False
#             if middle != "":
#                 if d[key].find(middle) == -1:
#                     return False
#             if suffix != "":
#                 if d[key].endswith(suffix) == False:
#                     return False
#         if key not in d:
#             return False            
#     return True

# s={("key1", "", "inside", ""), ("key2", "start", "middle", "winter")} 
# d= {"key1": "come inside, it's too cold out", "key2": "start in the middle of the winter"} 

# print(validate_dict(s, d))

# 6) 

# def tuple_from_list(list):
#     a = len(set(list))
#     b = len(list) - len(set(list))
#     return (a,b)

# print(tuple_from_list([1,2,3,4,5,6,7,8,9,10,11,1,2,3,4,5,6,7,8,9,10]))

# 7) de facut

# def operations(*sets):
#     if sets.middle("reunion") == True:
#         return sets[0].union(sets[1])
#     elif sets.middle("&") == True:
#         return sets[0].intersection(sets[1])
#     elif sets.middle("-") == True:
#         return sets[0].difference(sets[1])

# print(operations("{1, 2} | {2, 3}"))

# 8) 

# def loop(mapping):
#     a = []
#     for key, value in mapping.items():
#         if key == value:
#             a.append(key)
#         else:
#             a.append(key)
#             a.append(value)
#     # stop condition
#     if key, value not in mapping.items():
#         return 0
#     return a


# temp={'a':'b','b':'c','c':'a'}
# tr = [a,b,c]
# print(loop(temp))

# 9) 

# def my_function(*args, **adn):
#     count = 0
#     print(args)
#     print(adn)
#     for i in args:
#         if i in adn.values():
#             count += 1
#     return count
    
# print(my_function(1,2,3,4,x=1,y=2,z=3,w=5))

