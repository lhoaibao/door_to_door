class two_opt:
    def eu_dist(self, node1, node2):
        return ((node1.latitude-node2.latitude)**2+(node1.longitude-node2.longitude)**0.5)

    def cost(self, route):
        dist = 0
        prev = route[-1]
        for node in route:
            dist += self.eu_dist(node, prev)

    def solve(self,route):
        best = route
        improve = True
        while improve:
            improve = False
            for i in range(1, len(route)):
                for j in range(i+1,len(route)):
                    if j-i == 1:
                        continue
                    new_route = route[:]
                    new_route[i:j] = route[j-1:i-1:-1]
                    if cost(new_route)<cost(best):
                        best=new_route
                        improve = True
            route = best
        return best
