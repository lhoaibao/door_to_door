import math


class Node:
    """
    Node class has 3 attribute:
        - city_name
        - latitude
        - longitude
    """
    def __init__(self, city_name, latitude, longitude):
        self.city_name = city_name
        self.latitude = latitude
        self.longitude = longitude
