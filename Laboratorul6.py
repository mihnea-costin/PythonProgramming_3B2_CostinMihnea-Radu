import re
import os

# 1)

def extract_words(text):
    return re.findall(r'\w+', text)

print("Exercitiul 1")	
print(extract_words("Hello, how are you?"))
print("***************")

# 2)

def long_length_x_substrings_matching_the_regex(regex,text,x):
    words = re.findall(r'\w+', text)
    rez = []
    for word in words:
        if len(word) == x and re.match(regex, word):
            rez.append(word)
    return rez

print("Exercitiul 2")
print(long_length_x_substrings_matching_the_regex(r'^[a-z]+$', "Hello, how are you?", 3))
print("***************")

# 3)

def function(strings_list,regex_list):
    rez = []
    for string in strings_list:
        for regex in regex_list:
            if re.search(regex,string):
                rez = rez + [string]
                break
    return rez

print("Exercitiul 3")
print(function(["Hello","how","are","you?"],["[w-z]+"]))
print("***************")

# 4)

def function_verify_xml_dict(xml_doc_path, attrs):
    rez = []
    with open(xml_doc_path,"r") as f:
        for el in re.findall("<\w+.*?>",f.read()):
            if(all([re.search(item[0]+"\s*=\s*\""+item[1] + "\"",el,flags=re.I) for item in attrs.items()])):
                rez+=[el]
    return rez

print("Exercitiul 4")
print(function_verify_xml_dict("C:\\Users\\mihne\\Desktop\\python_proiecte.xml",{"class": "url", "name": "url-form", "data-id": "item"}))
print("***************")

# 5)

def function_verify_xml_dict_key_value(xml_doc_path, attrs):
    rez = []
    file = open(xml_doc_path, "r")
    xml_doc_data = file.read()

    for key, value in attrs.items():
        verify = r"(<(\w+) [^>]*(" + r"|".join("{key}=\"{value}\"".format(key=key, value=value))
    verify += r")[^>]*>[^(<\2>)]*</\2>)"

    for elem in re.findall(verify, xml_doc_data):
        rez.append(elem[0])
    return rez

print("Exercitiul 5")
print(function_verify_xml_dict_key_value("C:\\Users\\mihne\\Desktop\\python_proiecte.xml",{"class": "url", "name": "url-form", "data-id": "item"}))
print("***************")

# 6) 

def word_censorship(text):
    words = re.findall(r'\w+', text)
    rez = []
    for word in words:
        if re.match(r'^[aeiouAEIOU].*[aeiouAEIOU]$', word):
            rez.append("*" * len(word))
        else:
            rez.append(word)
    return rez

print("Exercitiul 6")
print(word_censorship("Ana are mere"))
print("***************")


# 7) 

def valid_cnp(cnp):
    if re.match(r"^[1-9]\d{2}(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])(0[1-9]|[1-4]\d|5[0-2]|99)(00[1-9]|0[1-9]\d|[1-9]\d\d)\d$",cnp) != None:
        return "Este corect"
    else:
        return "Nu este corect"

print("Exercitiul 7")
print(valid_cnp("5001215171709"))
print("***************")


# 8)

def dir_files_matching_with_regex(dir_path,regex):
    rez = []
    for root,dirs,files in os.walk(dir_path):
        for f in files:
            file_name = os.path.join(root,f)            
            if re.search(regex,f) != None:
                rez += [f]
            try:
                with open(file_name, "r") as fd:
                        string = fd.read()
                        if (re.search(regex, string)):
                            if re.search(regex,f) != None:
                                rez[-1] = "<<" + rez[-1]
                            else:
                                rez = rez + [f]
            except:
                pass
    return rez

print("Exercitiul 8")
print(dir_files_matching_with_regex("C:\\Users\\mihne\\Desktop\\photoshop",r'\.psd$'))
print("***************")
