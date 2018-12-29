#!/usr/bin/env python3
import sys
import time
from Graph import Graph


def main():
    if len(sys.argv) == 1 or len(sys.argv) > 3:
        print('wrong command')
        return None
    graph = Graph()
    load = graph.load_graph(sys.argv[1])
    if not load:
        print('Something wrong with file')
        return None
    if len(sys.argv) == 2:
        start = time.time()
        result = graph.nearest_neighbor()
    elif sys.argv[2] == 'nearest_neighbor':
        start = time.time()
        result = graph.nearest_neighbor()
    else:
        print('algo is not found')
        return None
    end = time.time()
    print('time run: ',end-start)


if __name__ == '__main__':
    main()
