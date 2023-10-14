total_cost = float(input("Please enter the total cost of your shopping cart: $"))
if total_cost >= 50:
    discount = 0.1 * total_cost
    discounted_cost = total_cost - discount
    print(f"Original total cost: ${total_cost:.2f}")
    print(f"Discounted total cost (10% off): ${discounted_cost:.2f}")
else:
    print(f"Original total cost: ${total_cost:.2f}")
    print("No discount applied.")
