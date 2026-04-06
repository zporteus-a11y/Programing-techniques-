#products is where you place the stock, price and item quantity
products = {
    "Rice": {"price": 100, "stock": 16},
    "Sugar": {"price": 120, "stock": 8},
    "Flour": {"price": 90, "stock": 12},
    "Milk": {"price": 208, "stock": 6},
    "Cheese": {"price": 300, "stock": 30},
    "Butter": {"price": 600, "stock": 4},
    "Bleach": {"price": 350, "stock": 7},
    "Soap": {"price": 120, "stock": 15},
    "Toothpaste": {"price": 180, "stock": 7},
    "Detergent": {"price": 500, "stock": 4}
}

cart = {}
"""these lines of code starting from 17-57 is for the display menu that has the that shows the products available in stock
also it has a built in alert for low stock as shown in like 23"""
def display_products():
    print("\nAvailable Products:")
    for item, details in products.items():
        print(f"{item} - ${details['price']} (Stock: {details['stock']})")
        if details['stock'] < 5:
            print(f"{item} LOW IN STOCK!")
"""the lines of codes starting from 25 is specifically for the cashier prompt, it verifies that there is stock for the items
and it updates the cart and reduces the available stock in the product catalog"""
def add_to_cart():
    display_products()
    item = input("Enter product name to add: ").title()
    if item in products:
        try:
            qty = int(input("Enter quantity: "))
            if qty <= products[item]["stock"]:
                cart[item] = cart.get(item, 0) + qty
                products[item]["stock"] -= qty
                print(f"{qty} {item}(s) added to cart.")
            else:
                print("Not enough stock available.")
        except ValueError:
            print("Invalid quantity. Please enter a number.")
    else:
        print("Product not found.")

def remove_from_cart():
    if not cart:
        print("Cart is empty.")
        return
    item = input("Enter product name to remove: ").title()
    if item in cart:
        qty = int(input("Enter quantity to remove: "))
        if qty >= cart[item]:
            products[item]["stock"] += cart[item]
            del cart[item]
            print(f"{item} removed from cart.")
        else:
            cart[item] -= qty
            products[item]["stock"] += qty
            print(f"{qty} {item}(s) removed from cart.")
    else:
        print("Item not in cart.")

def view_cart():
    if not cart:
        print("Cart is empty.")
        return
    print("\nShopping Cart:")
    subtotal = 0
    for item, qty in cart.items():
        price = products[item]["price"]
        total = price * qty
        subtotal += total
        print(f"{item} - Qty: {qty}, Unit Price: ${price}, Total: ${total}")
    print(f"Subtotal: ${subtotal}")
"""checkout is where the calculations for the 5% and discounts happen it makes sure that the amount entered is enough to pay
for the items in the cart after if verifies that then it clears the cart for the next customer"""
def checkout():
    if not cart:
        print("Cart is empty.")
        return
    subtotal = sum(products[item]["price"] * qty for item, qty in cart.items())
    tax = subtotal * 0.10
    total = subtotal + tax

    # Discount
    if total > 5000:
        discount = total * 0.05
        total -= discount
        print(f"Discount applied: ${discount:.2f}")

    print(f"\nSubtotal: ${subtotal:.2f}")
    print(f"Sales Tax (10%): ${tax:.2f}")
    print(f"Total Due: ${total:.2f}")

    try:
        payment = float(input("Enter amount received: "))
        if payment < total:
            print("Payment insufficient. Transaction cancelled.")
            return
        change = payment - total
        receipt(subtotal, tax, total, payment, change)
        cart.clear()
    except ValueError:
        print("Invalid payment input.")
"""the receipt part of the code is where the results of the checkout are printed on a a formatted paper with the store header
it will display the total, subtotal, tax, amount paid and change on the receipt then finally have a thank you message at the bottom"""
def receipt(subtotal, tax, total, payment, change):
    print("\n===== BEST BUY RETAIL STORE =====")
    print("Receipt")
    print("---------------------------------")
    for item, qty in cart.items():
        price = products[item]["price"]
        total_item = price * qty
        print(f"{item} - Qty: {qty}, Unit Price: ${price}, Total: ${total_item}")
    print("---------------------------------")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Sales Tax: ${tax:.2f}")
    print(f"Total Due: ${total:.2f}")
    print(f"Amount Paid: ${payment:.2f}")
    print(f"Change: ${change:.2f}")
    print("Thank You for Shopping with Us!")
    print("=================================\n")

#this is the main loop that keeps the POS system running
def main():
    while True:
        print("\n--- Point of Sale System ---")
        print("1. Display Products")
        print("2. Add to Cart")
        print("3. Remove from Cart")
        print("4. View Cart")
        print("5. Checkout")
        print("6. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            display_products()
        elif choice == "2":
            add_to_cart()
        elif choice == "3":
            remove_from_cart()
        elif choice == "4":
            view_cart()
        elif choice == "5":
            checkout()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid. Please try again.")


if __name__ == "__main__":
    main()