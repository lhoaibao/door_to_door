import math


class Node:
    """
    Node class has 2 attribute:
        - latitude
        - longitude
    """
    def __init__(self, city_name, latitude, longitude):
        self.city_name = city_name
        self.latitude = latitude
        self.longitude = longitude
