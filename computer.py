class Computer:
    #attributes:
    description: str
    processor_type: str
    hard_drive_capacity: str
    operating_system: str
    year_made: str
    price: int

    # constructor takes the necessary attributes for functions to run smoothly
    def __init__(self, description: str, pt: str, hdc: int, os: str, year_made: int, price: int):
        self.description=description
        self.operating_system=os
        self.year_made=year_made
        self.processor_type=pt
        self.hard_drive_capacity=hdc
        self.price=price



    # print the description and operating system of the computer
    def print_details(self):
        print(self.description)
        print("-", self.operating_system)
    
    #update the price and operating system of the computer
    def refurbish(self, new_os):
        if (self.year_made < 2000):
            self.price = 0 # too old to sell, donation only
        elif (self.year_made < 2012):
            self.price = 250 # heavily-discounted price on machines 10+ years old
        elif (self.year_made < 2018):
            self.price = 550 # discounted price on machines 4-to-10 year old machines
        else:
            self.price = 1000 # recent stuff

        if new_os is not None:
            self.operating_system = new_os # update details after installing new OS
        print("Item refurbished!")

    #updates price
    def update_price(self, new_price: int):
        self.price=new_price

