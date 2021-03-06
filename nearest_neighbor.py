from Graph import Graph


class nearest_neighbor(Graph):
    """
    this class is inherited by class Graph
    """
    def __init__(self):
        super().__init__()

    def find_shortest_path(self):
        sum = 0
        result = []
        check_list = self.list_city
        first = self.list_city[0]
        result.append(first)
        check_list.remove(first)
        while check_list:
            min = self.distance(result[-1], check_list[0])
            nearest = check_list[0]
            for i in range(1, len(check_list)):
                check = self.distance(result[-1], check_list[i])
                if check < min:
                    min = check
                    nearest = check_list[i]
            sum += min
            result.append(nearest)
            check_list.remove(nearest)
        self.length = sum
        self.result = result
