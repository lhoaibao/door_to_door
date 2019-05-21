from Node import Node
import os


class Graph:
    """
    Graph class has 3 attribute:
        - list_city is a list Node
        - result is a path shorted
        - length is distance from the start to the end get by result
    """
    def __init__(self):
        """
        list_city is a list and will be set later when run load_graph function
        result is a list of city has solve by algo
        length is a variable store the length of road result
        """
        self.list_city = []
        self.result = []
        self.length = 0

    def distance(self, n1, n2):
        """
        function help calculate the distance of two node
        """
        return ((n1.latitude-n2.latitude)**2 +
                (n1.longitude-n2.longitude)**2)**0.5

    def load_graph(self, file_name):
        """
        function read file csv and get content of file into
        a Graph:
            - list_city is a list has node
            - return True when file can access and not empty other return Fasle
        """
        list_city = []
        if os.access(file_name, os.F_OK):
            if os.access(file_name, os.R_OK):
                with open(file_name, 'r') as f:
                    file_content = f.readlines()
                for i in range(len(file_content)):
                    x = file_content[i].strip('\n').split(', ')
                    list_city.append(Node(x[0], float(x[1]), float(x[2])))
                self.list_city = list_city
                if file_content:
                    return True
        return False

    def print_result(self):
        """
        function help show the result after algo excute
        """
        result = self.result
        for i in range(len(result)-1):
            print(result[i].city_name, end=' -> ')
        print(result[-1].city_name)
        print('number of city: ', len(result))
        print('length: ', self.length)
