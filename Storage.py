from tabulate import tabulate
import logging

logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(message)s', filename='logfile.log')


items = {'Name': ['Petrol', 'Sand', 'Rope'],
         'Quantity': [140, 87, 432],
         'Unit': ['l', 't', 'm'],
         'Unit Price (PLN)': [7, 15, 4]
         }


def select_operation(listOfOperation):
    while True:
        print('\n')
        for index, operation in enumerate(listOfOperation):
            print(index, operation)

        try:
            index = int(input("What would you like to do ?"))

            if index <= len(listOfOperation) - 1:
                return index

            else:
                logging.info("Number not in range ")
                continue

        except ValueError:
            logging.info("Wrong type of input")
            continue


def get_items():
    print(tabulate(items, headers='keys', tablefmt='fancy_grid', missingval='N/A'))


def add_item():
    while True:
        name = input('Item name:')
        quantity = input('Quantity:')
    pass


operations = ['Exit', 'Show your storage', 'Add new item']


if __name__ == "__main__":

    while True:
        index = select_operation(operations)

        if index == 0:
            print("Exiting...Bye!")
            exit(1)
        elif index == 1:
            get_items()

        elif index == 2:
            print('Adding to storage...')
            add_item()
