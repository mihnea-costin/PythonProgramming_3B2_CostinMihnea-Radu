# 2) 

# def my_function(*args, **kwargs):
#     sum = 0
#     for arg in kwargs.keys():
#         sum += int(kwargs[arg])

#     return sum

# anonymous_function = lambda *args, **kwargs: sum([value for value in kwargs.values()])

# print(my_function(1, 2, c=3, d=4))
# print(anonymous_function(1, 2, c=3, d=4))

# 3) 

# def all_vowels_comprehension(string):
#     return [ch for ch in string if ch.lower() in "aeiou"]

# all_vowels_anonymous_function = lambda string: [ch for ch in string if ch.lower() in "aeiou"]

# def all_vowels_filter(string):    
#     filter_list = list(filter(lambda ch: ch.lower() in "aeiou", string))
#     return filter_list

# print(all_vowels_comprehension("Programming in Python is fun"))
# print(all_vowels_anonymous_function("Programming in Python is fun"))
# print(all_vowels_filter("Programming in Python is fun"))


# 4)

# def dict_list(*args, **kwargs):
#     list = []

#     for a in args:
#         if type(a) == dict:
#             if len(a.keys()) >= 2 and any([True if type(key) == str and len(key) >= 3 else False
#                                              for key in a.keys()]):
#                 list.append(a)

#     for kwa in kwargs.keys():
#         if type(kwargs[kwa]) == dict:
#             if len(kwargs[kwa].keys()) >= 2 and any([True if type(key) == str and len(key) >= 3 else False
#                                              for key in kwargs[kwa].keys()]):
#                 list.append(kwargs[kwa])

#     return list    

# print(dict_list( {1: 2, 3: 4, 5: 6}, 

#  {'a': 5, 'b': 7, 'c': 'e'}, 

#  {2: 3}, 

#  [1, 2, 3],

#  {'abc': 4, 'def': 5},

#  3764,

#  dictionar={'ab': 4, 'ac': 'abcde', 'fg': 'abc'},

#  test={1: 1, 'test': True}))

# 5) 

# def new_list_with_numbers_from_given_list(list):
#     list2 = []
#     for element in list:
#         if type(element) in [int, float, complex]:
#             list2.append(element)
#     return list2
# print(new_list_with_numbers_from_given_list([1, "2", {"3": "a"}, {4, 5}, 5, 6, 3.0]))

# 6)

# def pairs_of_odd_and_even(initial_list)
#     return list(zip([i for i in initial_list if i % 2 == 0], [i for i in initial_list if i % 2 != 0]))

# 7) 

# def process(**kwargs):
#     def fibonacci(n):
#         if n == 0:
#             return 0
#         elif n == 1:
#             return 1
#         else:
#             return fibonacci(n-1) + fibonacci(n-2)
#     list = fibonacci(1000)
#     if "filters" in kwargs.keys():
#         list = [flt for flt in list if all([p(flt) for p in kwargs["filters"]])]
#     if "limit" in kwargs.keys():
#         list = list[:kwargs["limit"]]
#     if "offset" in kwargs.keys():
#         list = list[kwargs["offset"]:]
#     return list   

# def sum_digits(x):
#     return sum(map(int, str(x)))

# print(process(filters=[lambda item: item % 2 == 0, lambda item: item == 2 or 4 <= sum_digits(item) <= 20], limit=2, offset=2))

# 8) a) 

# def print_arguments(function):
#     def new_function(*args, **kwargs):
#         print(args, kwargs)
#         return function(*args, **kwargs)
#     return new_function

# def multiply_by_two(x):
#     return x * 2

# def add_numbers(a,b):
#     return a + b

# augmented_multiply_by_two = print_arguments(multiply_by_two)

# x = augmented_multiply_by_two(10) 

# print(x)

# b) 

# def multiply_output(function):
#     def new_function(*args, **kwargs):
#         return function(*args, **kwargs) * 2
#     return new_function

# def multiply_by_three(x):
#     return x * 3

# augmented_multiply_by_three = multiply_output(multiply_by_three)

# x = augmented_multiply_by_three(10)

# print(x)

# c)

# def augment_function(function,decorators):
#     def new_function(*args,**kwargs):
#         res = function
#         for d in decorators:
#             res = d(res)
#         return res(*args, **kwargs)
#     return new_function

# def add_numbers(a, b):
#     return a + b

# decorated_function = augment_function(add_numbers, [print_arguments, multiply_output]) 

# x = decorated_function(3, 4) 

# print(x)

# 9) 

# def f9(pairs):
#     return [{"sum": pair[0] + pair[1],"prod": pair[0]*pair[1],"pow": pair[0]**pair[1]} for pair in pairs]

# print(f9(pairs = [(5, 2), (19, 1), (30, 6), (2, 2)]))  