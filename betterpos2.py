menu = {"shawarma Sandwich": 5.00, 
        "drink": 1.00,
        "iran yougurt": 2.00,
        "fries": 3.00,
        "shawarma meal": 7.00,
        "super meal":10.00,
        "double meal":12.00}
user_cart={}
# code organization could be much better, look for ways to improve organization 
def printMenu():
    i=1
    for key in menu.keys():# you can eliminate the .keys to make the code more condesned and easy to read 
        print ("{0}. {1} - ${2}".format(i,key,menu[key]))
        i=i+1
def printCart():
    for key in user_cart.keys():
        print(user_cart[key],"{0} - {1}".format(key,menu[key]))


while True:
    print("1. Add to order, 2. Remove from order, 3. View your order, 0. Complete Checkout")
    user_selection= int(input("what would you like to do "))
    if user_selection==1:#add to order 
        printMenu()
        user_selection= int(input("what would you like to order? "))-1
        add_quantity= int(input("how many? "))
        key=list(menu.keys())[user_selection]
        if user_cart.get (key) == None: #if key not in user_cart 
            user_cart[key]=add_quantity
        else: 
            user_cart[key]+=add_quantity
        print ("we added",add_quantity, key)
        for food_name in user_cart.keys():
            print (" {0} - {1}".format (food_name , menu[food_name]))
            quantity = user_cart[food_name]
            price= menu[food_name]
            subtotal=price*quantity    
            print ("item's subtotal is : ",subtotal)
   
    elif user_selection==2:#remove from order 
        printCart()
        change_selection= (input("select the item you would like to change. ")).lower()
        if change_selection in user_cart.keys(): 
            change = (input('would you like to change the quantity? Y/N  ')).lower() 
            if change == "y" :
                quantity_change1= int(input("how many do you want ?"))
                if quantity_change1>= 1:
                    user_cart[change_selection]=quantity_change1
                elif quantity_change1 == 0 : 
                    user_cart.pop(change_selection)
                    
            else:#user input is N , user does not want to change the quantity.  
                print ("you must enter a valid Item !")
        else :# if the item is not in the cart 
            print ("you must enter a valid Item!")
    elif user_selection == 3 :# print cart 
        subtotal= 0
        for food_name in user_cart.keys():
            print (user_cart[food_name] , "{0}  - {1}".format(food_name,menu[food_name]))
            subtotal+= float((user_cart[food_name]*menu[food_name])) 
            print ('your subtotal today is :', subtotal)
        tax = float(subtotal)*0.075
        print ('your taxes are: ', tax)
        total= 0
        total = float(subtotal + tax)
        print ('your total is : ' , total)
    elif user_selection == 0:# break
        print("Time to checkout")
        break
    elif user_selection == 4: # print user cart 
        print (user_cart)


# to do list 
#1 cosmotics 
#2 add menu items 
# 3 do the remove items... 
# Download thonny and run code 
# 





