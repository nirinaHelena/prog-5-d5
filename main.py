import logging
from enum import Enum

logging.basicConfig(level=logging.INFO)


class PaymentMethod(Enum):
    CARD = "card"
    TOKEN = "token"


class CoffeeType(Enum):
    ESPRESSO = "espresso"
    LATTE = "latte"
    CAPPUCCINO = "cappuccino"


class CoffeeMachineError(Exception):
    def __init__(self, message: str):
        self.message = message
        logging.error(f"[CoffeeMachineError] {message}")
        super().__init__(message)


class PaymentError(CoffeeMachineError):
    def __init__(self, message="Payment failed."):
        super().__init__(message)


class CoffeeNotAvailableError(CoffeeMachineError):
    def __init__(self, coffee_type: CoffeeType):
        message = f"{coffee_type.value.capitalize()} is not available."
        super().__init__(message)


class WaterError(CoffeeMachineError):
    def __init__(self):
        super().__init__("Insufficient water in the machine.")


class ElectricityError(CoffeeMachineError):
    def __init__(self):
        super().__init__("Electricity is unavailable. Please wait for Jirama.")


class PaymentService:
    def validate_payment(self, method: PaymentMethod, token: str = None) -> bool:
        if method == PaymentMethod.CARD:
            return self._validate_card()
        elif method == PaymentMethod.TOKEN:
            return self._validate_token(token)
        else:
            raise PaymentError("Unsupported payment method.")

    def _validate_card(self) -> bool:
        input("Insert your card and press Enter...")
        print("Card accepted.")
        return True 

    def _validate_token(self, token: str) -> bool:
        if token == "VALID_TOKEN":
            print("Subscription token accepted.")
            return True
        raise PaymentError("Invalid or expired token.")


class CoffeeMachine:
    def __init__(self):
        self.available_coffees = {
            CoffeeType.ESPRESSO: 3,
            CoffeeType.LATTE: 2,
            CoffeeType.CAPPUCCINO: 0
        }
        self.water_level = 100  # ml
        self.electricity_on = True

    def check_conditions(self, coffee_type: CoffeeType):
        if not self.electricity_on:
            raise ElectricityError()
        if self.water_level < 20:
            raise WaterError()
        if self.available_coffees.get(coffee_type, 0) <= 0:
            raise CoffeeNotAvailableError(coffee_type)

    def brew_coffee(self, coffee_type: CoffeeType) -> str:
        self.water_level -= 20
        self.available_coffees[coffee_type] -= 1
        return f"{coffee_type.value.capitalize()} is ready! ☕ Enjoy!"


class Main:
    def __init__(self):
        self.payment_service = PaymentService()
        self.machine = CoffeeMachine()

    def run(self):
        print("Welcome to the Automatic Coffee Machine!")
        while True:
            try:
                payment_method = self.ask_payment_method()
                token = None
                if payment_method == PaymentMethod.TOKEN:
                    token = input("Enter your subscription token: ")

                self.payment_service.validate_payment(payment_method, token)

                coffee_type = self.ask_coffee_type()
                self.machine.check_conditions(coffee_type)

                print("Preparing your coffee...")
                print(self.machine.brew_coffee(coffee_type))

            except CoffeeMachineError as e:
                print(f" {e.message}")

            again = input("\nDo you want another coffee? (y/n): ").strip().lower()
            if again != 'y':
                print("Thank you! Have a nice day!")
                break

    def ask_payment_method(self) -> PaymentMethod:
        print("\nPlease choose your payment method:")
        print("1. Card")
        print("2. Subscription Token")
        choice = input("Enter 1 or 2: ").strip()
        if choice == "1":
            return PaymentMethod.CARD
        elif choice == "2":
            return PaymentMethod.TOKEN
        else:
            raise PaymentError("Invalid payment method selected.")

    def ask_coffee_type(self) -> CoffeeType:
        print("\nAvailable coffees:")
        for i, c in enumerate(CoffeeType, 1):
            print(f"{i}. {c.value.capitalize()}")
        choice = input("Select your coffee: ").strip()
        mapping = {
            "1": CoffeeType.ESPRESSO,
            "2": CoffeeType.LATTE,
            "3": CoffeeType.CAPPUCCINO
        }
        return mapping.get(choice) or self.invalid_choice()

    def invalid_choice(self):
        raise CoffeeNotAvailableError(CoffeeType("invalid"))  
        
if __name__ == "__main__":
    Main().run()
