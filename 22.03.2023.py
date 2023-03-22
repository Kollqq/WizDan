class NaZakupy:

    def __init__(self, name_of_product, quantity, unit_of_measure, unit_price):
        self.name_of_product = name_of_product
        self.quantity = quantity
        self.unit_of_measure = unit_of_measure
        self.unit_price = unit_price

    def display_product(self):
        print(f"{self.name_of_product} {self.quantity} {self.unit_of_measure} {self.unit_price}")
    def product_quantity(self):
        print(f"{self.quantity}{self.unit_of_measure}")
    def how_much_costs(self):
        print(f"{int(self.quantity) * int(self.unit_price)} zl")


class ArithmeticSequences:

    def view_data(self):
        for i in range(0,e+1):
    def get_items(self):
        a = int(input("Enter item number: "))
        b = int(input("Enter the element value: "))
    def get_parameters(self):
        c = int(input("Enter a first element: "))
        d = int(input("Enter difference: "))
        e = int(input("Enter the number of string elements to generate: "))
    def count_sum(self):
        Sum =
    def count_elements(self):



def z1():
    list1 = [str(x * 2) for x in range(0, 31)]
    with open("Numbers.txt", "w") as file:
        for i in list1:
            file.write(i + " ")

def z2():
    with open("Numbers.txt", "r") as file:
        print(file.read())

def z3():
    with open("Text.txt", "w+") as file:
        file.write(3*"Hello\n")
    with open("Text.txt", "r") as file:
        print(file.read())

