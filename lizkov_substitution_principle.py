"""
This code is adapted from the example in this youtube video:
    "SOLID Design in Python - Liskov Substitution Principle #3" by user "Coding w/ da Best"
    https://www.youtube.com/watch?v=ZSAXFDNPcIg&t=7s

The Liskov Substitution Principle is:
    "Subtypes must be substitutable for their base types"
"""


# this code violates the Liskov Substitution Principle #
class KitchenAppliance:
    def on(self) -> None:
        print("appliance switched on")

    def off(self) -> None:
        print("appliance switched off")

    def set_temp(self, temp: int) -> None:
        print(f"temperature set to {temp}")


class Toaster(KitchenAppliance):
    pass


class Juicer(KitchenAppliance):
    def set_temp(self, temp: int) -> None:
        raise NotImplementedError("cannot set temperature on appliance Juicer()")


# code refactor to adhere to the principle #
class KitchenAppliance:
    def on(self) -> None:
        print("appliance switched on")

    def off(self) -> None:
        print("appliance switched off")


class KitchenApplianceWithTemp(KitchenAppliance):
    def set_temp(self, temp: int) -> None:
        print(f"temperature set to {temp}")


class Toaster(KitchenApplianceWithTemp):
    pass


class Juicer(KitchenAppliance):
    pass
