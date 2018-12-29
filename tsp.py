#!/usr/bin/env python3
import sys
import os
from Node import Node
from Graph import Graph
import time


class name:
    def __init__(self, name):
        self.name = name

def read_file(file_name):
    """
    function read file csv and get content of file into
    a list
    -   return file_content when file exists and can read
    -   return None when file cant read or doesnt exists
    """
    file_content = []
    if os.access(file_name,os.F_OK):
        if os.access(file_name,os.R_OK):
            with open(file_name,'r') as f:
                file_content = f.readlines()
            for i in range(len(file_content)):
                file_content[i] = file_content[i].strip('\n').split(', ')
                file_content[i][1] = float(file_content[i][1])
                file_content[i][2] = float(file_content[i][2])
            return file_content
    return None


def parse_map(cities):
    """
    function parse a list of city in to a object Graph is a dictionary
    key of dic is city_name
    value is a object Node has two arg is latitude and longitude
    -   return a Graph object if list of city not None
    -   return None if list of city None
    """
    list_city = []
    if cities:
        for i in range(len(cities)):
            list_city.append(Node(cities[i][0], cities[i][1], cities[i][2]))
        return Graph(list_city)
    else:
        return None


def main():
    start = time.time()
    file_content = read_file(sys.argv[1])
    graph = parse_map(file_content)
    # end = time.time()
    # print('time read and parse map: {}'.format(end-start))
    # start = time.time()
    result = graph.nearest_neighbor()
    end = time.time()
    graph.print_result();
    print(end-start)

if __name__ == '__main__':
    main()
