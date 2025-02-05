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
            "Coffee Drinks": ["Latte", "Cappuchino"],
            "Breakfast": ["Bagel", "Muffin", "Scone"],
            "Lunch": ["Flafael wrap", "Hummus and Pita", "Chicken Wrap"]
        }

        #prices are also encapuslated
        self.prices = {
            "Monster": 3.99, "Rockstar": 3.99,
            "Latte": 4.99, "Cappuchino": 4.99,
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

            #Method to calculate total cost of order
    def calculate_total(self, items, has_student_id=False):
                #Calcualte the total
                total = sum(self.prices[item] for item in items)

                #calculate discount based on student id.
                if has_student_id and total >10:
                    total *=0.9
                #this method returns the total cost of the order to the code that called method
                return total;

#method to calculate the dilvery time based on location and time of day
    def estimate_delivery(self,location, current_hour):
        #calculate the base time
        base_time =  self.delivery_location[location]

        #Calculate the dilvery time based on the time of day
        if(9 <= current_hour <= 10) or( 11 <= current_hour <= 13):
            return base_time  + 5
        #if they aren't ordring during a bust time, return the base time with no adjustment
        return base_time

    def print_order(self,location,items,current_hour,has_student_id:False):
        #display the order infromation
        print("\n=== Order Summary===")
        print("Delivery to: {location}")
        print("\nItems Ordered:")
        #loop through the list of menu items they orders
        for item in items:
            print(f"- {item}: ${self.prices[item]:.2f}")
        #call the methods to get total cost and dilvery time
        total = self.calculate_total(items, has_student_id)
        delivery_time = self.estimate_delivery(location, current_hour)

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

        #show menu
        delivery.show_menu("Coffee Drinks")
        
        #sample order at 9:30 Am (Peak Morning hour)
        order = ["Latte", "Bagel"]

        #Display recipt for the order
        delivery.print_order("ITEC Computer Lab", order, 9, has_student_id=True);
    #add the line of code to automatically call the main method
if __name__ =="__main__":
        main()