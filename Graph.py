class Graph:
    """
    Graph class has 1 attribute:
        - map is an dictionary with key is city_name
    * value of each key is a node has longitude and latitude
    """
    def __init__(self, list_city):
        self.list_city = list_city
        self.result = []
        self.length = 0

    # def distance(self, node1, node2):
    #     return ((node1.latitude-node2.latitude)**2+(node1.longitude-node2.longitude)**2)**0.5

    def nearest_neighbor(self):
        sum = 0
        check_list = self.list_city.copy()
        first = self.list_city[0]
        result = []
        result.append(first)
        check_list.remove(first)
        while check_list:
            min = ((result[-1].latitude-check_list[0].latitude)**2+(result[-1].longitude-check_list[0].longitude)**2)**0.5
            nearest = check_list[0]
            # nearest = min(check_list, key=lambda x: self.distance(result[-1], x))
            # sum += self.distance(result[-1], nearest)
            for i in range(1,len(check_list)):
                check = ((result[-1].latitude-check_list[i].latitude)**2+(result[-1].longitude-check_list[i].longitude)**2)**0.5
                if check < min:
                    min = check
                    nearest = check_list[i]
            sum += min
            result.append(nearest)
            check_list.remove(nearest)
        self.length = sum
        self.result = result

    def print_result(self):
        result = self.result
        for i in range(len(result)-1):
            print(result[i].city_name, end='-> ')
        print(result[-1].city_name)
        print('length: ', self.length)
