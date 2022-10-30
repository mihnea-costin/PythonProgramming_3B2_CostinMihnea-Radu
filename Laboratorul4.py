import os

def all_extensions_list(director):
    lista = []
    for root, dirs, files in os.walk(director):
        for file in files:
            lista.append(os.path.splitext(file)[1])
    return lista

print(all_extensions_list(r'C:\Users\mihne\Desktop\PMP2022'))



