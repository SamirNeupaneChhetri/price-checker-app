import csv


# Initialize an empty dictionary to store items and prices
items = {}

# read CSV file 
def ReadCsv() -> None:
    with open('/Users/samirneupanechhetri/Documents/PYTHON/PythonBasic/fileHandling/P/supermarket.csv','r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            items[row['Item']] = float(row['Price'])

def showItem() -> None:
    for item,price in items.items():
        print(f"{item} : {price}")



def UserSelect_Items() -> list[str]:
    cart: list[str] = []


    pass

def totalCost() ->None:
    pass

def Options() ->None:
    print('Options')
    print('1 - Show Items')
    print('2 - Select Items')
    print('3 - Total Coast')
    print('0 - Exit')

def askChoice() -> int:
    choice = -1
    feed = input("Select The Options: ")
    if feed.isdigit():
        choice = int(feed)
    return choice


def main() -> None:
    print()
    print('---------Welcome To Op Market------------')
    print()
    while True:
        Options()
        print()
        choice = askChoice()
        print()
        if choice == 1:
            ReadCsv()
            showItem()
            print()
        elif choice == 2:
            UserSelect_Items()
        elif choice == 3:
            totalCost()
        elif choice == 0:
            break
        else:
            print('Oops You chose Wroung options!! Please try Again....')
            print()

    print("---------Thanks for Shopping-----------")
    print()



if __name__ == "__main__":
    main()

    