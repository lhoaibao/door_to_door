#!/usr/bin/env python3
import sys
import time
from nearest_neighbor import nearest_neighbor
from two_opt import two_opt


def main():
    if len(sys.argv) == 1 or len(sys.argv) > 3:
        print('wrong command')
        return None
    if len(sys.argv) == 2:
        graph = nearest_neighbor()
        load = graph.load_graph(sys.argv[1])
        if not load:
            print('Something wrong with file')
            return None
        start = time.time()
        result = graph.nearest_neighbor()
    elif sys.argv[2] == 'nearest_neighbor':
        graph = nearest_neighbor()
        load = graph.load_graph(sys.argv[1])
        if not load:
            print('Something wrong with file')
            return None
        start = time.time()
        result = graph.nearest_neighbor()
    elif sys.argv[2] == 'two_opt':
        graph = two_opt()
        load = graph.load_graph(sys.argv[1])
        if not load:
            print('Something wrong with file')
            return None
        start = time.time()
        result = graph.two_opt()
    else:
        print('algo is not found')
        return None
    graph.print_result()
    end = time.time()
    print('time run: ',end-start)


if __name__ == '__main__':
    main()
