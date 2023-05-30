class Review:
    all_reviews = []

    def __init__(self, customer, restaurant, rating):
        self._customer = customer
        self._restaurant = restaurant
        self._rating = rating
        self.all_reviews.append(self)

    # rating method that return rating
    def rating(self):
        return self._rating
    
    #class method
    @classmethod
    def all(cls):
        return cls.all_reviews
    
    def customer(self):
        return self._customer
