import math


class Node:
    """
    Node class has 2 attribute:
        - latitude
        - longitude
    """
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def distance(self,node):
        return math.sqrt((self.latitude-node.latitude)**2+(self.longitude-node.longitude)**2)
