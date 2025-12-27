from models.product import Product
from services.inventory_service import InventoryService

service = InventoryService()

while True:
    print("\n1. ເພິ່ມສິນຄ້າ")
    print("2. ສະແດງສິນຄ້າ")
    print("3. ລຶບສິນຄ້າ")
    print("4. ອອກ")

    choice = input("Select: ")

    if choice == "1":
        name = input("Name: ")
        price = float(input("Price: "))
        qty = int(input("Quantity: "))
        product = Product(name, price, qty)
        service.add_product(product)
        print("Product added!")

    elif choice == "2":
        products = service.get_all_products()
        for p in products:
            print(p)

    elif choice == "3":
        pid = int(input("Product ID: "))
        service.delete_product(pid)
        print("Deleted!")

    elif choice == "4":
        break
