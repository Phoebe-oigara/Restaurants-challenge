class Review:
    all_reviews = []

    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
        Review.all_reviews.append(self)

    # rating method that return rating
    
    def get_rating(self):
        return self.rating
    
    #class method
    @classmethod
    def all(cls):
        return cls.all_reviews
    
    #method returns the values of the objects rather than object names

    def __str__(self):
        return f"Review: {self.customer.full_name()} rated {self.rating} stars"
    
    # def __str__(self):
    #     return f"Review(customer={self._customer}, restaurant={self._restaurant}, rating={self._rating})"
