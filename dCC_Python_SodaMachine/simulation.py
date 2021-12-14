from customer import Customer
from backpack import Backpack
from soda_machine import SodaMachine
import user_interface

class Simulation:
    def __init__(self):
        pass
        

    def run_simulation(self):
        """The central method called in main.py."""
        customer = Customer()
        soda_machine = SodaMachine()
        will_proceed = True
        while will_proceed == True:
            user_input = user_interface.simulation_main_menu()
            if user_input == 1:
                soda_machine.begin_transaction(customer)
            elif user_input == 2:
                customer.check_coins_in_wallet()
            elif user_input == 3:
                Customer.check_backpack()
            else:
                will_proceed = False
