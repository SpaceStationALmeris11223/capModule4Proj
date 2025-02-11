"""The DunnDelivery class demonstrates core OOP concepts:
-Encapsulation: Data (menu and Prices) are bundled in the class
-Abstraction: Complex delivery logic is hidden behind simple method calls."""

class DunnDelivery:
    #Constructor method creates new instance of a delivery
    def __init__(self):#self is the object your currently creating
        #class atributes demonstrate encapsulation
        #by keeping related data together

    
        #Menu Attribute  - menu of items you can oder to be delivered
        self.menu = {
            "Energy Drinks": ["Monster", "Rockstar"],
            "Coffee Drinks": ["Latte", "Cappuchino", "Ho ho mocha", "Spooky campfire mocha", "Gingerbread mocha"],
            "Breakfast": ["Bagel", "Muffin", "Scone"],
            "Lunch": ["Flafael wrap", "Hummus and Pita", "Chicken Wrap"]
        }

        #prices are also encapuslated
        self.prices = {
            "Monster": 3.99, "Rockstar": 3.99,
            "Latte": 4.99, "Cappuchino": 4.99, "Ho ho mocha": 4.99, "Spooky campfire mocha":4.99, "Gingerbread mocha":4.99,
            "Bagel": 2.99, "Muffin": 2.99, "Scone": 2.99,
            "Flafael wrap": 8.99, "Hummus and Pita": 7.99, "Chicken Wrap": 8.99
        }
        #holds delivery location and number of minutes it takes to deliver to that location
        self.delivery_location = {
            "Library": 10,
            "Academic Success Center": 8,
            "ITEC Computer Lab": 5
        }
        #Shows the menu of items avialabe for delivery
        
    def priority_order(self):
            #Reduces delivery time by 3
            step_on_it = False
            Priority = input("Is this a priority order? (yes/no)    ").upper()
            if (Priority == "YES"):
                step_on_it = True
            return step_on_it

    def show_menu(self, category=None):
            if category:#Below ises 
                print(f"\n=== {category} ===")
                #loop through items in specified category
                #and display them to the user
                for item in self.menu[category]:
                    print(f"{item}: ${self.prices[item]:.2f}")
            else:
                #show the entire menu
                for category in self.menu:# first show categroy name
                    print(f"==={category}===")
                    #Second show the items in the category
                    for item in self.menu[category]:
                        print(f"{item}: ${self.prices[item]:.2f}")
    def price_range_search(self):
        """Allows the user to search for items within their price range"""
        while True:
            try:
                min_price = float(input("Please enter a minimum price: $"))
                max_price = float(input("Please enter a maximum price: $"))

                if min_price <0 or max_price < 0:
                        print("Prices can't be negative silly. Please enter a valid number")
                        continue
                if min_price > max_price:
                        print("Minimum price cannot exceed maximum price. Please enter a number smaller than the Maximum price")
                        continue
                break # loop exits if input is valud
            except ValueError:
                   print("Please enter a valid number.")     

        items_in_range = {item: price for item, price in self.prices.items() if min_price <= price <= max_price}
        
        if items_in_range:
            print("\nItems available in your price range: ")
            for item, price in items_in_range.items():
                 print(f"- {item}: ${price:.2f}")
        else:
            print("no items within the sepcifed price range. Sorry")    


    def Review_Us(self):
        """Allows the user to leave a review"""
        while True:
            try:
                review_us = input("Would you like to sumbit a review of your delivery? (yes or no) ").lower()
                if(review_us == "yes"):
                    while True:#Keeps asking until they give valid input
                        try:
                            review = int(input("How would you rate your Delivery 1-10   "  ))
                            if  1 <= review <= 10:
                                break#I just found out I don't need to keep if in parantheiss like C#
                            else:
                                print("Please enter a number between 1 and 10   ")
                        except ValueError:
                            print("Please enter a number between 1 and 10 " )
                    
                    why = input("Would you like to share why you rated us this? (yes/no) ").lower()
                    if (why == "yes"):
                        input("Please enter what you thought of your delivery   ")
                    
                    print("Thank you for ordering from Dunn Brothers Coffee have a wonderful Day!")
                    break

                elif review_us == "no":
                    print("Thank you for ordering from Dunn Brothers Coffee have a wonderful Day!")
                    break
                
                else:
                    print("Not a vaild Response. Please enter a yes or no ")

            except ValueError:
                print("Please Enter a number from 1-10 ")
            #Method to calculate total cost of order
    def calculate_total(self, items, has_student_id=False):
                #Calculate the total
                total = sum(self.prices[item] for item in items)

                #calculate discount based on student id.
                if has_student_id and total >10:
                    total *=0.9
                #this method returns the total cost of the order to the code that called method
                return total;

#method to calculate the deilvery time based on location and time of day
    def estimate_delivery(self,location, current_hour,step_on_it):
        #calculate the base time
        base_time =  self.delivery_location[location]
        #Calculate the deilvery time based on the time of day
        if(9 <= current_hour <= 10) or( 11 <= current_hour <= 13):
            if step_on_it:
                base_time = max(1, base_time -3) #got to make sure there is at least a minute for deilvery unless we teleport it to them lol
            return base_time  + 5
        #if they aren't ordring during a busy time, return the base time with no adjustment
        return base_time

    def print_order(self,location,items,current_hour,has_student_id:False,step_on_it):
        #display the order infromation
        print("\n=== Order Summary===")
        print("Delivery to: {location}")
        print("\nItems Ordered:")
        #loop through the list of menu items they orders
        for item in items:
            print(f"- {item}: ${self.prices[item]:.2f}")
        #call the methods to get total cost and dilvery time
        total = self.calculate_total(items, has_student_id)
        delivery_time = self.estimate_delivery(location, current_hour,step_on_it)

        #display the subtotal
        print(f"\nSubtotal: ${sum(self.prices[item] for item in items):.2f}")

        #calculate the total with discount f the customer has student id
        if has_student_id and total < sum(self.prices[item] for item in items):
            print("Student discount applied!")
        #display total after discount & estimated delivery time
        print(f"Total after discount: ${total:.2f}")
        print(f"Estimated delivery time: {delivery_time} minutes")

#main method is executed as soon as the program runs
def main():
        #create a new delivery object - instantiating a new object
        delivery = DunnDelivery()

        step_on_it = delivery.priority_order()

        search_choice = input("would you like to search for items within a specified price range? (yes\no) ").lower()
        if search_choice == "yes":
            delivery.price_range_search()
        #show menu
        delivery.show_menu("Coffee Drinks")
        
        #sample order at 9:30 Am (Peak Morning hour)
        order = ["Latte", "Bagel"]

        #Display recipt for the order
        delivery.print_order("ITEC Computer Lab", order, 9, step_on_it = step_on_it, has_student_id=True);
        #ask for a review
        delivery.Review_Us()
    #add the line of code to automatically call the main method
if __name__ =="__main__":
        main()