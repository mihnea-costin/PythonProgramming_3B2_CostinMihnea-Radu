import utils
import utils

def main():
    while True:
        x = input("Enter number: ")
        x = int(x)
        if x == "q":
            break
        else:
            print(utils.process_item(x))

if __name__ == '__main__':
    main()