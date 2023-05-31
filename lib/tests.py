from customer import Customer
from restaurant import Restaurant

long_line = '_' * 50
# Create some customers
customer1 = Customer("Euralia", "Wendy")
customer2 = Customer("Romeo", "Evans")

# Create some restaurants
restaurant1 = Restaurant("Panari")
restaurant2 = Restaurant("Hilton")

# Add reviews for customers
customer1.add_review(restaurant1, 4)
customer1.add_review(restaurant2, 3)
customer2.add_review(restaurant1, 5)

# full_name()
print("")
print("Customer 1 full name:")
print("")
print(customer1.full_name())
print(long_line)

# restaurants()
print("")
print("Customer 1 reviewed restaurants:")
print("")
print([restaurant.name for restaurant in customer1.restaurants()])
print(long_line)

# average_star_rating()
print("")
print("Average star rating for Restaurant 1:")
print("")
print(restaurant1.average_star_rating())
print(long_line)

# customers()
print("")
print("Customers who reviewed Restaurant 1:")
print("")
print([customer.full_name() for customer in restaurant1.customers()])
print(long_line)