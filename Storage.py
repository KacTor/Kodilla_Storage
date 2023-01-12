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
            index = int(input("\nWhat would you like to do ?"))

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
        unit = input('Unit name:')
        unitPrice = input('Unit Price (PLN):')

        print(
            f'You wont to add {name},{quantity},{unit},{unitPrice}.')
        answer = input('Are these details correct? (y/n) ')

        if answer in ['yes', 'y', 'YES', 'Y']:

            listOfInput = [name, quantity, unit, unitPrice]
            i = 0

            for dict in items:
                items[dict].append(listOfInput[i])
                i += 1
            print('Successfully added to storage. Current status:')
            get_items()
            break
        else:
            print('Item has not been added.')
            logging.debug("Incorrect item")
            break


def sell_item():
    while True:
        try:
            name = input('Item name:')
            listOfName = items['Name']
            index = listOfName.index(name)

            if name in listOfName:
                quantity = int(input('The quantity you want to sell:'))
                maxQuantity = items['Quantity'][index]
                unit = items['Unit'][index]

                if items['Quantity'][index] - quantity < 0:
                    logging.info(f'Not enough {name}')
                    answer = input(
                        f'Are you want to sell maximum of {name} - {maxQuantity}? (y/n) ')

                    if answer in ['yes', 'y', 'YES', 'Y']:
                        zeroQuantity = items['Quantity'][index]
                        print(
                            f'Successfully sold {zeroQuantity} {unit} of {name}')
                        items['Quantity'][index] = 0
                        get_items()
                        break

                else:
                    items['Quantity'][index] -= quantity
                    print(
                        f'Successfully sold {quantity} {unit} of {name}')
                    get_items()
                break

        except ValueError:
            print('Wrong name of product')
            logging.debug('Wrong name of product')
            break


operations = ['Exit', 'Show your storage', 'Add new item', 'Sell item']


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

        elif index == 3:
            print('Selling item...')
            sell_item()
