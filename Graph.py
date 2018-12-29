from Node import Node
import os


class Graph:
    """
    Graph class has 3 attribute:
        - list_city is a list Node
        - result is a path shorted
        - length is distance from the start to the end get by result
    *
    """
    def __init__(self):
        self.list_city = []
        self.result = []
        self.length = 0

    def distance(self, n1, n2):
        return ((n1.latitude-n2.latitude)**2+(n1.longitude-n2.longitude)**2)**0.5

    def load_graph(self, file_name):
        """
        function read file csv and get content of file into
        a list
        -   return file_content when file exists and can read
        -   return None when file cant read or doesnt exists
        """
        list_city = []
        if os.access(file_name,os.F_OK):
            if os.access(file_name,os.R_OK):
                with open(file_name,'r') as f:
                    file_content = f.readlines()
                for i in range(len(file_content)):
                    x = file_content[i].strip('\n').split(', ')
                    list_city.append(Node(x[0],float(x[1]),float(x[2])))
                self.list_city = list_city
                return True
        return False

    def nearest_neighbor(self):
        sum = 0
        result = []
        check_list = self.list_city
        first = self.list_city[0]
        result.append(first)
        check_list.remove(first)
        while check_list:
            min = self.distance(result[-1], check_list[0])
            nearest = check_list[0]
            for i in range(1,len(check_list)):
                check = self.distance(result[-1], check_list[i])
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
            print(result[i].city_name, end= ' -> ')
        print(result[-1].city_name)
        print('length: ', self.length)
