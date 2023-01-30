from csv import DictWriter

items = {'Name': ['Petrol', 'Sand', 'Rope'],
         'Quantity': [140, 87, 432],
         'Unit': ['l', 't', 'm'],
         'Unit Price (PLN)': [7, 15, 4]
         }


def export_items_to_csv(dict):
    with open('storage.csv', 'w', newline='') as csvfile:
        fieldnames = dict.keys()
        writer = DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(dict)


export_items_to_csv(items)
