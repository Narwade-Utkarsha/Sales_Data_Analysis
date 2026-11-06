import matplotlib.pyplot as plt

products = ["Laptop", "Mobile", "Keyboard", "Mouse"]
sales = [50, 80, 40, 30]

plt.bar(products, sales)

plt.title("Product Sales Analysis")
plt.xlabel("Products")
plt.ylabel("Sales")

plt.show()
