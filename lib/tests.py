from customer import Customer

from restaurant import Restaurant

# Create some customers
customer1 = Customer("Euralia", "Wendy")
customer2 = Customer("Romeo", "Evans")

# Create some restaurants
restaurant1 = Restaurant("Panari")
restaurant2 = Restaurant("Hilton")

# Add reviews for customers
customer1.add_review(restaurant1, 4)
customer1.add_review(restaurant2, 5)
customer2.add_review(restaurant1, 3)

# Test the methods
print(customer1.given_name())  
print(customer1.family_name())  
print(customer1.full_name())  

print(Customer.all())  

print(customer1.restaurants()) 
print(customer2.restaurants()) 

print(restaurant1.reviews())  
print(restaurant1.customers()) 

print(restaurant1.average_star_rating())  