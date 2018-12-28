class Graph:
    """
    Graph class has 1 attribute:
        - map is an dictionary with key is city_name
    * value of each key is a node has longitude and latitude
    """
    def __init__(self, list_map, first_city):
        self.list_map = list_map
        self.first_city = first_city

    def find_shortest_path(self):
        sum = 0
        must_visit = list(self.list_map.keys()).copy()
        result = [self.first_city.name]
        path = [self.first_city]
        must_visit.remove(self.first_city)
        while must_visit:
            nearest = min(must_visit, key=lambda x: self.list_map[path[-1]].distance(self.list_map[x]))
            sum += self.list_map[path[-1]].distance(self.list_map[nearest])
            path.append(nearest)
            result.append(nearest.name)
            must_visit.remove(nearest)
        return result,sum,len(path)
