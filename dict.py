
products = []
while True:
    selection = int(input("1.Add New Product\n2.Print Product Details"
                          "\n3.Buy Product"
                          "\n4.Delete Product"
                          "\n5.Exit"))
    if selection == 1:
        product_number = int(input("Enter Product Number :"))
        product_name = input("Enter Product Name :")
        product_price = input("Enter Product Price :")
        product_qty =  int(input("Enter Product Quantity :"))
        product = {
            "id" : product_number,
            "name" : product_name,
            "price" : product_price,
            "qty" : product_qty
        }
        products.append(product)
        print("Product Added Successfully")
    elif selection == 2:
        product_number = input("Enter product number :")
        for i in products:
            if i['id'] == product_number:
                print(i)
                break
    elif selection == 3:
      product_number = input("Enter Product Number :")
      quantity=int(input("Enter Quantity"))
      product_qty-=quantity
      print("remaining quantity=",product_qty)
    elif selection == 4:
        product_number = input("Enter Product Number :")

        for i in products:
         if i['id'] == product_number:
             products.remove(i)
             print("deleted")
    else:
        exit()