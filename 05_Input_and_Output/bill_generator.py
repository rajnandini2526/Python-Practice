# Build a bill generator using user input.


item = input("Enter item name: ")
price = float(input("Enter item price: "))
quantity = int(input("Enter quantity: "))

total = price * quantity
gst = total * 0.18
final_bill = total + gst

print("\n------ BILL ------")
print("Item      :", item)
print("Price     :", price)
print("Quantity  :", quantity)
print("Subtotal  :", total)
print("GST (18%) :", gst)
print("Total Bill:", final_bill)