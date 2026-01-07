"""
OOP - Synthesis Practical Task
Inventory management system for a Nike warehouse.

This program allows store managers to:
- Read shoe data from a file
- Capture new shoe data
- View all shoes
- Restock shoes with low quantity
- Search for shoes by code
- Calculate value per item
- Identify the shoe with the highest quantity
"""

# Absolute file path to inventory.txt
INVENTORY_FILE = (
    r"C:\Users\Pauli\OneDrive\Documents\Data Science Bootcamp"
    r"\Level 1 - Python for Data Science"
    r"\Task 23 - OOP - Synthesis"
    r"\inventory.txt"
)


# ========= Shoe Class =========
class Shoe:
    """
    Represents a shoe item in the inventory.
    """

    def __init__(self, country, code, product, cost, quantity):
        """
        Initialise the Shoe object with required attributes.
        """
        self.country = country
        self.code = code
        self.product = product
        self.cost = int(cost)
        self.quantity = int(quantity)

    def get_cost(self):
        """
        Returns the cost of the shoe.
        """
        return self.cost

    def get_quantity(self):
        """
        Returns the quantity of the shoe.
        """
        return self.quantity

    def __str__(self):
        """
        Returns a user-friendly string representation of the shoe object.
        """
        return (
            f"Country: {self.country} | "
            f"Code: {self.code} | "
            f"Product: {self.product} | "
            f"Cost: R{self.cost} | "
            f"Quantity: {self.quantity}"
        )


# ========= Shoe List =========
# This list stores all Shoe objects
shoe_list = []


# ========= Functions =========
def read_shoes_data():
    """
    Reads shoe data from inventory.txt and populates the shoe list.
    Uses exception handling to prevent runtime errors.
    """
    try:
        with open(INVENTORY_FILE, "r") as file:
            lines = file.readlines()[1:]  # Skip header line

            for line in lines:
                data = line.strip().split(",")
                shoe = Shoe(
                    data[0],
                    data[1],
                    data[2],
                    data[3],
                    data[4]
                )
                shoe_list.append(shoe)

    except FileNotFoundError:
        print("Error: inventory.txt file not found.")
    except Exception as error:
        print(f"An unexpected error occurred: {error}")


def capture_shoes():
    """
    Allows the user to capture new shoe data and add it to the shoe list.
    """
    try:
        country = input("Enter country: ")
        code = input("Enter shoe code: ")
        product = input("Enter product name: ")
        cost = int(input("Enter cost: "))
        quantity = int(input("Enter quantity: "))

        new_shoe = Shoe(country, code, product, cost, quantity)
        shoe_list.append(new_shoe)

        print("Shoe successfully added.")

    except ValueError:
        print("Invalid input. Cost and quantity must be numbers.")


def view_all():
    """
    Displays all shoes in the inventory.
    """
    for shoe in shoe_list:
        print(shoe)


def re_stock():
    """
    Finds the shoe with the lowest quantity and allows the user to restock it.
    Updates the inventory.txt file accordingly.
    """
    lowest_shoe = min(shoe_list, key=lambda shoe: shoe.quantity)

    print("\nLowest stock item:")
    print(lowest_shoe)

    try:
        add_quantity = int(input("Enter quantity to add: "))
        lowest_shoe.quantity += add_quantity

        # Rewrite inventory file with updated quantities
        with open(INVENTORY_FILE, "w") as file:
            file.write("Country,Code,Product,Cost,Quantity\n")
            for shoe in shoe_list:
                file.write(
                    f"{shoe.country},{shoe.code},{shoe.product},"
                    f"{shoe.cost},{shoe.quantity}\n"
                )

        print("Stock updated successfully.")

    except ValueError:
        print("Invalid quantity entered.")


def search_shoe():
    """
    Searches for a shoe by its code and prints the result.
    """
    search_code = input("Enter shoe code to search: ")

    for shoe in shoe_list:
        if shoe.code == search_code:
            print("Shoe found:")
            print(shoe)
            return

    print("Shoe not found.")


def value_per_item():
    """
    Calculates and displays the total value of each shoe.
    Formula: value = cost * quantity
    """
    for shoe in shoe_list:
        value = shoe.cost * shoe.quantity
        print(f"{shoe.product} value: R{value}")


def highest_qty():
    """
    Identifies and displays the shoe with the highest quantity.
    """
    highest_shoe = max(shoe_list, key=lambda shoe: shoe.quantity)
    print("Shoe with highest quantity (FOR SALE):")
    print(highest_shoe)


# ========= Main Menu =========
def main():
    """
    Displays the main menu and executes user-selected options.
    """
    read_shoes_data()

    while True:
        print(
            "\nNike Inventory Management System\n"
            "1. View all shoes\n"
            "2. Capture new shoe\n"
            "3. Restock lowest quantity shoe\n"
            "4. Search shoe by code\n"
            "5. Calculate value per item\n"
            "6. Show highest quantity shoe\n"
            "7. Exit"
        )

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            view_all()
        elif choice == "2":
            capture_shoes()
        elif choice == "3":
            re_stock()
        elif choice == "4":
            search_shoe()
        elif choice == "5":
            value_per_item()
        elif choice == "6":
            highest_qty()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


# Run the program
if __name__ == "__main__":
    main()
