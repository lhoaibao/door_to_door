#!/usr/bin/env python3
import sys
import time
from nearest_neighbor import nearest_neighbor
from two_opt import two_opt


def main():
    dic = {'nearest': nearest_neighbor, 'two_opt': two_opt}
    if len(sys.argv) == 1 or len(sys.argv) > 3:
        print('wrong command')
        return None
    else:
        if len(sys.argv) == 2:
            graph = nearest_neighbor()
        else:
            if sys.argv[2] in dic:
                graph = dic[sys.argv[2]]()
            else:
                print('algo not found')
                return None
        load = graph.load_graph(sys.argv[1])
        if not load:
            print('Something wrong with file or file is empty')
            return None
        start = time.time()
        result = graph.find_shortest_path()
    graph.print_result()
    end = time.time()
    print('time run: ', end-start)


if __name__ == '__main__':
    main()
