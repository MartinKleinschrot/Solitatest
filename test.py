#A retail calculator

def GetOrderValue():
    orderValue = 0
    while input("New item?(Yes|no) ") == 'Yes':    
        amountofItems = input("How many items: ")
        while not amountofItems.isdigit():
            print("Error: Amount of items has to be a number!")
            amountofItems = input("How many items: ")
        while True:
            try:
                priceperItem = input("Price per item: ")
                priceperItem = float(priceperItem)
                break
            except ValueError:
                print("Error: Price of items has to be a number!")
        orderValue = orderValue + float(priceperItem) * int(amountofItems)
        print("")
    print("")
    return orderValue

def GetTaxPercentage():
    taxpercentage = 0
    while True:
        taxcode = input("Tax code: ")
        if taxcode == "TX":
            taxpercentage = 6.25
            break
        elif taxcode == "NV":
            taxpercentage = 8
            break
        elif taxcode == "CA":
            taxpercentage = 8.25
            break
        elif taxcode == "UT":
            taxpercentage = 6.85
            break
        elif taxcode == "AL":
            taxpercentage = 4
            break
        else:
            print("Error: " + taxcode + " is not a valid taxcode!")
    return taxpercentage

def GetDiscount(orderValue):
    if orderValue >= 50000:
        discountRate = 1.15
        discountAmount = orderValue - (orderValue * discountRate)
    elif orderValue >= 10000:
        discountRate = 1.10
        discountAmount = orderValue - (orderValue * discountRate)
    elif orderValue >= 7000:
        discountRate = 1.07
        discountAmount = orderValue - (orderValue * discountRate)
    elif orderValue >= 5000:
        discountRate = 1.05
        discountAmount = orderValue - (orderValue * discountRate)
    elif orderValue >= 1000:
        discountRate = 1.03
        discountAmount = orderValue - (orderValue * discountRate)
    else:
        discountAmount = 0
    return discountAmount

def main():
    orderValue = GetOrderValue()
    discountAmount = GetDiscount(orderValue)
    totalprice = orderValue + discountAmount

    if totalprice == 0:
        print("Order Volume is 0$! Start buying from us now!")
    else:
        taxpercentage = GetTaxPercentage()

        #tax adding
        totalprice = (orderValue + discountAmount)*(1+(taxpercentage/100)) 
  
        print("")
        print("Order value: " + str(round(orderValue,2)) + "$")
        print("Discount: " + str(round(discountAmount,2)) + "$")
        print("Order value after discount: " + str(round(orderValue + discountAmount,2)) + "$")
        print("Tax: " + str(round((orderValue + discountAmount)*((taxpercentage/100)),2)) + "$")
        print("Total price with " +str(taxpercentage)+ "% tax: " + str(round(totalprice,2)) + "$")

    
# This name == main is just a best practise to use if you possibly plan to use the functions in this file in onther scripts.
if __name__ == '__main__':
    main()