import os
import sys

# 1) 

def all_unique_extensions_sorted_list(director):
    lista = []
    for root, dirs, files in os.walk(director):
        for file in files:
            lista.append(os.path.splitext(file)[1])
    return sorted(set(lista))

import sys

# 2)

def abs_paths_print_to_file(director, fisier):
    with open(fisier,"w") as f:
        for fis in os.listdir(director):
            nume = os.path.join(director,fis)
            if os.path.isfile(nume) and fis.startswith("A"):
                print(repr(os.path.abspath(nume)+os.linesep))
                f.write(os.path.abspath(nume)+os.linesep)

# 3) 

def last_20_or_list(my_path):
    if os.path.isfile(my_path):
        with open(my_path,"rb") as f:
            file_size = os.path.getsize(my_path)
            f.seek(file_size-20)                          	
            return f.read()
    elif os.path.isdir(my_path):
        list = {}
        for files in os.walk(my_path):
            for file in files:
                extension = os.path.splitext(file)[1]
                if extension in list:
                    list[extension] += 1
                else:
                    list[extension] = 1
        list = list.items()
        return sorted(list,key=lambda el:el[1],reverse=True)

print(last_20_or_list("C:\\Users\\mihne\\Desktop\\PMP2022"))


# 4) 

def all_unique_extensions_sorted_list_dir_on_command_line():
    lista = []
    if len(sys.argv) == 2:
        director = sys.argv[1]
        if os.path.isdir(director):
            for files in os.walk(director):
                for file in files:
                    lista.append(os.path.splitext(file)[1])
            return sorted(set(lista))
        else:
            print("Path is not a directory")
    else:
        print("Wrong number of arguments")

# 5) 

def list_of_file_which_contains_pattern(directory,pattern):
    lista = []
    if os.path.isdir(directory):
        for files in os.walk(directory):
            for file in files:
                if pattern in file:
                    lista.append(file)
        return lista
    else:
        print("Path is not a directory")

# 6) 

def callback_function(e):
    print(str(e))

def function6(target, to_search, callback):
    try:
        return list_of_file_which_contains_pattern(target,to_search)
    except Exception as e:
        callback_function(e)
        return []    

# 7) 

def file_infos_to_dict(cale_fisier):
    assert(os.path.isfile(cale_fisier)),"The parameter needs to be a file path"
    full_path=os.path.abspath(cale_fisier)
    file_size=os.path.getsize(cale_fisier)
    file_extension=os.path.splitext(cale_fisier)[1]
    can_read=os.access(cale_fisier,os.R_OK)
    can_write=os.access(cale_fisier,os.W_OK)
    return {"full_path":full_path,"file_size":file_size,
            "file_extension":file_extension,
            "can_read":can_read,
            "can_write":can_write}

# 8) 

def abs_paths_to_directory(dir_path):
    return [os.path.abspath(os.path.join(dir_path,el)) for el in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path,el))]


if __name__ == '__main__':
    exercitiu = 0
    while exercitiu != -99:
        exercitiu = int(input("Alege un exercitiu"))
        if exercitiu == 1:
            print(all_unique_extensions_sorted_list(r'C:\Users\mihne\Desktop\PMP2022'))
        elif exercitiu == 2:
            print(abs_paths_print_to_file("C:\\Users\\mihne\\Desktop\\PMP2022","ex.py"))
        elif exercitiu == 3:
            print(last_20_or_list("C:\\Users\\mihne\\Desktop\\PMP2022"))
        elif exercitiu == 4:
            all_unique_extensions_sorted_list_dir_on_command_line()
        elif exercitiu == 5:
            print(list_of_file_which_contains_pattern("C:\\Users\\mihne\\Desktop","clasa"))        
        elif exercitiu == 6:
            print(function6("C:\\Users\\mihne\\Desktop","clasa",callback_function))
        elif exercitiu == 7:
            print(file_infos_to_dict("C:\\Users\\mihne\\Desktop\\PMP2022\\Laboratorul4.py"))
        elif exercitiu == 8:
            print(abs_paths_to_directory("C:\\Users\\mihne\\Desktop\\PMP2022"))
        else:
            break