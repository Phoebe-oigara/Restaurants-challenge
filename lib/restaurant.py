class Restaurant:
     all_restaurants = []
 
     def __init__(self, name):
         self._name = name
         self.all_restaurants.append(self)