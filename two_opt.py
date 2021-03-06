from Graph import Graph


class two_opt(Graph):
    """
    this class is inherited by class Graph
    """
    def __init__(sefl):
        super().__init__()

    def route_distance(self, route):
        """
        function calculate the length of road route
        """
        sum = 0
        for i in range(1, len(route)):
            sum += self.distance(route[i-1], route[i])
        return sum

    def swap_2opt(self, route, i, k):
        """
        function get the route and return the new_route has reversed
        from item i to k
        """
        new_route = route[0:i]
        new_route.extend(reversed(route[i:k+1]))
        new_route.extend(route[k+1:])
        return new_route

    def find_shortest_path(self):
        improvement = True
        best_route = self.list_city.copy()
        best_distance = self.route_distance(best_route)
        while improvement:
            improvement = False
            for i in range(1, len(best_route)-1):
                for k in range(i+1, len(best_route)):
                    new_route = self.swap_2opt(best_route, i, k)
                    new_distance = self.route_distance(new_route)
                    if new_distance < best_distance:
                        best_distance = new_distance
                        best_route = new_route
                        improvement = True
        self.result = best_route
        self.length = best_distance
