#import methods from computer class
from computer import *

class ResaleShop:
    #attributes:
    name: str
    inventory: list
    #constructor
    def __init__(self):
        self.inventory=[]
        self.name="my store"

    # buy a new computer
    def buy(self,comp:Computer):
        self.inventory.append(comp)
        print("Item bought!")

    # sell a computer in the inventory
    def sell(self,comp:Computer):
        if (comp in self.inventory):
            self.inventory.remove(comp)
            print("Item sold!")
        else:
            print("Item not found. Please select another item to sell.")
    
    #print the details of each computer in the inventory
    def print_inventory (self):
        for c in (self.inventory):
            c.print_details()
