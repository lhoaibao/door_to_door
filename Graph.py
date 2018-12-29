class Graph:
    """
    Graph class has 3 attribute:
        - list_city is a list Node
        - result is a path shorted
        - length is distance from the start to the end get by result
    *
    """
    def __init__(self, list_city):
        """
        """
        self.list_city = list_city
        self.result = []
        self.length = 0

    def nearest_neighbor(self):
        """
        """
        sum = 0
        check_list = self.list_city.copy()
        first = self.list_city[0]
        result = []
        result.append(first)
        check_list.remove(first)
        while check_list:
            min = ((result[-1].latitude-check_list[0].latitude)**2+(result[-1].longitude-check_list[0].longitude)**2)**0.5
            nearest = check_list[0]
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
        """
        """
        result = self.result
        for i in range(len(result)-1):
            print(result[i].city_name, end='-> ')
        print(result[-1].city_name)
        print('length: ', self.length)
