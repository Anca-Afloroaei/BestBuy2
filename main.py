from products import Product, NonStockedProduct, LimitedProduct
from promotions import SecondHalfPrice, ThirdOneFree, PercentDiscount
from store import Store


def start(store: Store):
    """
    Launches the interactive user interface for the store.
    """
    while True:
        print("\n--- Welcome to Best Buy ---")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            print("\nAvailable Products:")
            products = store.get_all_products()
            idx = 1
            for product in products:
                print(f"{idx}. {product.show()}")
                idx += 1

        elif choice == '2':
            print(f"\nTotal quantity in store: {store.get_total_quantity()}")

        elif choice == '3':
            shopping_list = []
            products = store.get_all_products()
            print("\nEnter product numbers and quantities (leave blank to finish):")

            idx = 1
            for product in products:
                print(f"{idx}. {product.show()}")
                idx += 1

            while True:
                product_input = input("Product number (or Enter to finish): ").strip()
                if not product_input:
                    break
                try:
                    product_index = int(product_input) - 1
                    if product_index < 0 or product_index >= len(products):
                        print("Invalid product number.")
                        continue
                    quantity_input = input("Quantity: ").strip()
                    quantity = int(quantity_input)
                    shopping_list.append((products[product_index], quantity))
                except ValueError:
                    print("Invalid input. Please enter numbers.")

            try:
                total = store.order(shopping_list)
                print(f"\n✅ Order successful! Total cost: ${total}")
            except Exception as e:
                print(f"\n❌ Order failed: {e}")

        elif choice == '4':
            print("Thank you for shopping with us. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 4.")


def main():
    """
    Initializes the default product inventory and starts the store UI.
    """

    # setup initial stock of inventory
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
        NonStockedProduct("Windows License", price=125),
        LimitedProduct("Shipping", price=10, quantity=250, maximum=1),
    ]

    # Create promo catalog
    second_half_price = SecondHalfPrice("Second Half price!")
    third_one_free = ThirdOneFree("Third One Free!")
    thirty_percent = PercentDiscount("30% off!", percent=30)

    # Add promotions to products
    product_list[0].set_promotion(second_half_price)
    product_list[1].set_promotion(third_one_free)
    product_list[3].set_promotion(thirty_percent)

    # Create the store
    best_buy = Store(product_list)

    # Start the menu UI
    start(best_buy)


if __name__ == "__main__":
    main()


