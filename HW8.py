#description: For this project, I'm creating two classes, one that keeps track of the items to purchase
#and the other for the shopping cart. I'm then adding items to the cart and changing the quantity to see
#what the item/total cost is. 

#this is a class for the items to purchase 
class ItemToPurchase:
    def __init__(self, name, price, quantity):
        """
        initializing the object attributes when it's created. Sets the objects so we can use them througout the code.      

        :param self, name, price, quantity: for classes, we always use self so that we can access the info throughout the code. name gives
        us the name of the item, price tells us what the price of the item is, and quantity tells us what the quantity of the item. 
        :return: doesn't return anything, just sets the initial state of the object
        :if statements: none
        """
        #setting initial state of the object
        self.name = name
        self.price = price
        self.__quantity = quantity 

    def __str__(self):
        """
        this def returns us the readable code when we input the information in.      

        :param self: for classes, we always use self so that we can access the info throughout the code. 
        :return: it's returning the readable line of the code when we run it. for example, after inputing the item name, price, and quantity
        it prints the following statement out. 
        :if statements: none
        """
        totalPrice = self.__quantity * self.price
        return f'{self.name}: {self.__quantity} @ ${self.price:.2f} = ${totalPrice:.2f}'

    def get_quantity(self):
        """
        this def returns us quantity of the item.   

        :param self: for classes, we always use self so that we can access the info throughout the code. 
        :return: it's returning quantity of the object. 
        :if statements: none
        """
        return self.__quantity

    def set_quantity(self, quantity):
        """
        this def allows us to set the quantity of the object and change it if needed.      

        :param self: for classes, we always use self so that we can access the info throughout the code. 
        :return: It's not returning anything, but it sets the quantity of the object
        :if statements: none
        """
        self.__quantity = quantity



#class of the shopping cart and items in it
class ShoppingCart:
    def __init__(self, customer_ID):
        """
        initializing the object attributes when it's created. Sets the objects so we can use them througout the code.      

        :param self, customer_ID: for classes, we always use self so that we can access the info throughout the code. The customer_ID
        sets inputs the customer_ID number in the shopping receipt when printing the code. 
        :return: doesn't return anything
        :if statements: none
        """
        self.customer_ID = customer_ID

        #creating an empty list here to add the cart_items
        self.cart_items = []

    def add_item(self, item):
        """
        This adds items to the cart_item list we created above.      

        :param self, item: for classes, we always use self so that we can access the info throughout the code. The item
        takes in the value of the items given and adds them to the cart_item list. 
        :return: doesn't return anything, just adds the items to the list
        :if statements: none
        """
        self.cart_items.append(item) #adding items to the list

    def remove_item(self, item):
        """
        This removes items from the cart_item list we created above.      

        :param self, item: for classes, we always use self so that we can access the info throughout the code. The item
        takes in the value of the items given and removes them from the cart_item list. 
        :return: doesn't return anything
        :if statements: none
        """
        self.cart_items.remove(item) #removing item from the list       

    def change_quantity(self, name, new_quantity):
        """
        This allows us to change the quantity of the item and returns the new value. I'm doing a for loop to go through the items in the
        cart.item list, and changing its quantity to the new one. 

        :param self, name, new_quantity: self is always there. name takes in the string of the item (name), and new_quantity returns us
        the new value of the quantity 
        :return: returns us the new quantity of the item after looking through it in the list. 
        :if statements: doing a loop that looks for the item in the cart.item list, and setting its quantity to a new one
        """

        #loop to look for the item in cart.items list, and then changing its quantity 
        for item in self.cart_items:
            if item.name == name:
                item.set_quantity(new_quantity)
                return       #returning new-quantity of the item

    def print_cart(self):
        """
        we are printing the customer ID, and then making a loop to go through the items in the cart.items list and finding the total price
        by multiplying its price with the quantity . 

        :param self: self is always there to access info throughout the code
        :return: doesn't return but it's printing out the customer ID and the total price based on the quantity and price of the item. 
        :if statements: none
        """

        #setting total price to 0
        total_price = 0

        #customer ID
        print(f'Shopping Cart for Customer: {self.customer_ID}')

        #loop to check items in the cart.item list, and then finding the total price by multiplying the quantity with the price
        for item in self.cart_items:
            print(item)
            total_price += item.get_quantity() * item.price

        #printing total price
        print(f"TOTAL: ${total_price:.2f}")
       

def main():
    """
        This is where we are creating the items to purchase which includes the name, price, and quantity. This is also where we are changing
        the quantity and removing items based on the given instructions. Basically, this is where everything is being told to happen

        :param : none
        :return: printing out all the given info. 
        :if statements: none
        """
    #creating items to purchase (including name, price, and quantity
    potato_chips = ItemToPurchase('Potato Chips', 3.49, 1)
    potato_chips.set_quantity(2)         #change quantity to 2

    #new item to purchase
    soda = ItemToPurchase('Soda', 1.50, 1)
    
   # print(potato_chips)
   # print(soda)

    #creating customer ID
    shopping_cart = ShoppingCart('987654')
   
    shopping_cart.add_item(potato_chips)     #remove chips
    shopping_cart.add_item(soda)             #add soda to the list of items

    #printing out current cart
    shopping_cart.print_cart()
    
    #removing potato chips
    shopping_cart.remove_item(potato_chips)

    print()

    #printing out only 1 can of soda 
    shopping_cart.print_cart()

    print()

    #chaning quantity of soda to 3, and printing out new cart info
    soda.set_quantity(3)
    shopping_cart.print_cart()

if __name__ == '__main__':
    main()

