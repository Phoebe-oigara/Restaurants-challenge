class Restaurant:
     all_restaurants = []
 
     def __init__(self, name):
         self._name = name
         self.all_restaurants.append(self)
    
     def name(self):
        return self._name
     
 
     def reviews(self):
         restaurant_reviews = []
         for review in Review.all():
             if review.restaurant() == self:
                 restaurant_reviews.append(review)
         return [review.rating() for review in restaurant_reviews]