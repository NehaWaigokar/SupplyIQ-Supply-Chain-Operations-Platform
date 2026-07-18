from fetch_data import get_all_products
from add_data import add_new_product
from update_data import update_stock
from delete_data import delete_product


def main():
    while True:
        print("\n--- SupplyIQ Management System ---")
        print("1. View All Products")
        print("2. Add New Product")
        print("3. Update Product Stock")
        print("4. Delete Product")
        print("5. Exit")

        choice = input("Select an option (1-5): ")

        if choice == "1":
            get_all_products()

        elif choice == "2":
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            add_new_product(name, price)

        elif choice == "3":
            pid = input("Enter Product ID to update: ")
            qty = input("Enter new stock quantity: ")
            update_stock(pid, qty)

        elif choice == "4":
            pid = input("Enter Product ID to delete: ")
            delete_product(pid)

        elif choice == "5":
            print("Exiting system. Goodbye!")
            break

        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()