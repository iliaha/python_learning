class Storage:
    eqipment_collection = {
        'printer': [],
        'scanner': [],
        'monitor': [],
    }


class OfficeEquipment:
    def __init__(self, name, price, count, *args):
        self.count = count
        self.price = price
        self.name = name


class Printer(OfficeEquipment):
    def __init__(self, name, price, count, color):
        OfficeEquipment.__init__(self, name, price, count)
        self.color = color
        try:
            try_count = int(count)
        except ValueError:
            print(f'{self.count} не число! Нельзя добавить')
            try_count = None
        new_list = [name, price, try_count, color]
        Storage.eqipment_collection['printer'].append(new_list)

    def __str__(self):
        return f'{self.name} {self.price} {self.count} {self.color}'


class Scanner(OfficeEquipment):
    def __init__(self, name, price, count, type_scan):
        OfficeEquipment.__init__(self, name, price, count)
        self.type_scan = type_scan
        try:
            try_price = int(price)
        except ValueError:
            print(f'{self.price} не число! Нельзя добавить!')
            try_price = None
        new_list = [name, try_price, count, type_scan]
        Storage.eqipment_collection['scanner'].append(new_list)

    def __str__(self):
        return f'{self.name} {self.price} {self.count} {self.type_scan}'


class Monitor(OfficeEquipment):
    def __init__(self, name, price, count, color_monitor):
        OfficeEquipment.__init__(self, name, price, count)
        self.color_monitor = color_monitor
        try:
            count1 = int(count)
        except ValueError:
            print(f'{self.count} не число! Нельзя добавить!')
            count1 = None
        new_list = [name, price, count1, color_monitor]
        Storage.eqipment_collection['monitor'].append(new_list)

    def __str__(self):
        return f'{self.name} {self.price} {self.count} {self.color_monitor}'


office_printer = Printer('Canon', 12500, 12, 'белый')
office_scanner1 = Scanner('Canon', 10520, 5, 'сканер')
office_scanner2 = Scanner('HP', 'many', 8, 'сканер')
office_monitor = Monitor('Lenovo', 5200, 2, 'цветной')
print(office_printer)
print(office_scanner1)
print(office_monitor)
print(Storage.eqipment_collection)
