from tabulate import tabulate
from csv import DictWriter
import logging

logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(message)s', filename='logfile.log')


items = {'Name': ['Petrol', 'Sand', 'Rope'],
         'Quantity': [140, 87, 432],
         'Unit': ['l', 't', 'm'],
         'Unit Price (PLN)': [7, 15, 4]
         }


soldItems = {'Name': [],
             'Quantity': [],
             'Unit': [],
             'Unit Price (PLN)': []
             }


def select_operation(listOfOperation):
    while True:

        for index, operation in enumerate(listOfOperation):
            print(index, operation)

        try:
            index = int(input("\nWhat would you like to do ?"))
            print('\n')

            if index <= len(listOfOperation) - 1:
                return index

            else:
                logging.info("Number not in range ")
                continue

        except ValueError:
            logging.info("Wrong type of input")
            continue


def add_to_soldItems(name, quantity, unit, unitPrice):
    listOfName = soldItems['Name']

    if name not in listOfName:
        soldItems['Name'].append(name)
        soldItems['Quantity'].append(quantity)
        soldItems['Unit'].append(unit)
        soldItems['Unit Price (PLN)'].append(unitPrice)
    else:
        index = listOfName.index(name)
        soldItems['Quantity'][index] += quantity


def get_items(listOfItems):
    print(tabulate(listOfItems, headers='keys',
          tablefmt='fancy_grid', missingval='N/A'))


def get_costs_income(listOfItems):
    '''if len(listOfItems['Quantity']) != len(listOfItems['Unit Price (PLN)']):
        logging.debug('Wrong table, Quantity != Unit Price')
        print('Check the table, different amount of values')

    else:'''
    sumOfIndividualProducts = [listOfItems['Quantity'][i] * listOfItems['Unit Price (PLN)'][i]
                               for i in range(len(listOfItems['Name']))
                               ]
    finalSum = sum(sumOfIndividualProducts)
    return round(finalSum, 2)


def show_revenue(costs, income):
    finalCosts = get_costs_income(costs)
    finalIncome = get_costs_income(income)
    revenue = finalIncome - finalCosts

    print(f'''Income: {finalIncome}
Costs: {finalCosts}
---------------
Revenue: {revenue} PLN''')


def add_item():
    while True:
        nameByUser = input('Item name:')
        name = nameByUser.lower()

        # compare only small letters
        compName = []
        for label in items['Name']:
            compName.append((label.lower()))

        if name in compName:
            quantity = int(input('Quantity:'))
            index = compName.index(name)
            items['Quantity'][index] += quantity
            print(
                f'Successfully added to {name.capitalize()}. Current status:')
            get_items(items)
            break

        else:
            quantity = int(input('Quantity:'))
            unit = input('Unit name:')
            unitPrice = int(input('Unit Price (PLN):'))
            print(
                f'You wont to add {name.capitalize()},{quantity},{unit},{unitPrice}.')
            answer = input('Are these details correct? (y/n) ')

            if answer in ['yes', 'y', 'YES', 'Y']:

                listOfInput = [name.capitalize(), quantity, unit, unitPrice]
                i = 0

                for dict in items:
                    items[dict].append(listOfInput[i])
                    i += 1
                print('Successfully added to storage. Current status:')
                get_items(items)
                break

            else:
                print('Item has not been added.')
                logging.debug("Incorrect item")
                break


def sell_item():
    while True:
        try:
            nameByUser = input('Item name:')
            name = nameByUser.lower()

            # compare only small letters
            compName = []
            for label in items['Name']:
                compName.append((label.lower()))

            if name in compName:
                index = compName.index(name)
                quantity = int(input('The quantity you want to sell:'))
                logging.debug('Wrong type of input')

                maxQuantity = items['Quantity'][index]
                unit = items['Unit'][index]
                unitPrice = items['Unit Price (PLN)'][index]

                if int(items['Quantity'][index]) - quantity < 0:
                    logging.info(f'Not enough {name.capitalize()}')
                    answer = input(
                        f'Are you want to sell maximum of {name.capitalize()} - {maxQuantity}? (y/n) ')

                    if answer in ['yes', 'y', 'YES', 'Y']:
                        zeroQuantity = items['Quantity'][index]
                        print(
                            f'Successfully sold {zeroQuantity} {unit} of {name.capitalize()}')
                        items['Quantity'][index] = 0
                        get_items(items)
                        add_to_soldItems(name.capitalize(),
                                         quantity, unit, unitPrice)
                        break

                else:
                    items['Quantity'][index] -= quantity
                    print(
                        f'Successfully sold {quantity} {unit} of {name.capitalize()}')
                    get_items(items)
                    add_to_soldItems(name.capitalize(),
                                     quantity, unit, unitPrice)

                break

        except ValueError:
            logging.debug('Wrong name of product')
            break


def export_items_to_csv(dict):
    with open('storage.csv', 'w', newline='') as csvfile:
        fieldnames = ['sss', 'ddsd', '\n']
        writer = DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerows(dict)
    


operations = ['Exit', 'Show your storage',
              'Add new item', 'Sell item', 'Show revenue', 'Save']


if __name__ == "__main__":

    while True:
        print('\n')
        index = select_operation(operations)

        if index == 0:
            print("Exiting...Bye!")
            exit(1)
        elif index == 1:
            get_items(items)

        elif index == 2:
            print('Adding to storage...')
            add_item()

        elif index == 3:
            print('Selling item...')
            sell_item()

        elif index == 4:
            print('Revenue breakdown (PLN)...')
            show_revenue(items, soldItems)

        elif index == 5:
            print('...')
            export_items_to_csv(items)
