def process_item(x):
    x = x + 1
    while any([x % element == 0 for element in range(2, int(x**(1/2)) + 1)]):
        x = x + 1
    return x

def main():
    print(process_item(int(input("Enter the value for x:"))))

