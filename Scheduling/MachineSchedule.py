import copy
from datetime import datetime
import heapq

import sys

from Scheduling.OrderData import OrderData
from Scheduling.Node import Node


class Main:
    def __init__(self):
        self.orderData = self.load_data()
        self.sequence = 0  # For record the order that pushed into the heap
        start = datetime.today()
        print('Execute Start at: ', start)
        heap = self.initial_heap()
        self.skylineList = self.extend_heap(heap)
        finish = datetime.today()  # Get Run time

        print('--------------SKYLINE-------------')
        for skyline in self.skylineList:
            skyline.print_path()
            skyline.print_element()
            print()

        print('Length:', len(self.skylineList))
        print('Start: ', start)
        print('Finish:', finish)
        print('Spend: ', finish - start)

    @staticmethod
    def load_data():
        file = open('C:/Users/User/Google 雲端硬碟/畢業專題/漢翔/MachineScheduling/data1.txt')
        time_format = "%Y-%m-%d.%H:%M:%S"
        order_data = []
        for line in file:
            section = line.split(';')
            receive = (datetime.strptime(section[2], time_format) - datetime(1970, 1, 1)).total_seconds()
            deadline = (datetime.strptime(section[3], time_format) - datetime(1970, 1, 1)).total_seconds()
            order_data.append(OrderData(section[4], section[0], int(section[1]), receive, deadline))
        file.close()
        return order_data

    def initial_heap(self):
        heap = []
        for data in self.orderData:
            node = Node(data)
            heapq.heappush(heap, (node.get_sum(), self.sequence, copy.deepcopy(node)))
            self.sequence += 1   # Compare sequence when Sum are same (First In First Out)
        return heap

    def extend_heap(self, heap):
        # Extend Heap
        skyline_list = []
        while heap:  # Keep Running when heap not empty

            # for h in heap:
            #     h[2].print_path()
            # print('-----------------------')

            node = heapq.heappop(heap)[2]
            # Check if been dominated or not
            dominate = False
            for skyline in skyline_list:
                if node.dominate(skyline):
                    dominate = True
            if not dominate:
                # Check if it has been Leaf already or not
                is_leaf = True
                for data in self.orderData:
                    if len(node.scheduledData) == 13:  # Limit how many nodes in each path
                        break
                    # node.print_path()
                    new_node = copy.deepcopy(node)
                    if new_node.add_data(data):
                        heapq.heappush(heap, (new_node.get_sum(), self.sequence, copy.deepcopy(new_node)))
                        self.sequence += 1
                        is_leaf = False
                # If it is a Leaf then throw into Skyline list
                if is_leaf:
                    print(datetime.now())
                    skyline_list.append(node)
                # elif sys.getsizeof(heap) > 1000000:
                #         print(len(heap), '\t\t', sys.getsizeof(heap))
            # if sys.getsizeof(heap) > 4800000:
            #     print(sys.getsizeof(heap), 'Before')
            #     skyline_list.extend(self.split_heap(heap))
            #     print(sys.getsizeof(heap), 'After')
        return skyline_list

    def split_heap(self, heap):
        new_heap = []
        length = len(heap) * 0.3
        while len(new_heap) < length:
            heapq.heappush(new_heap, heapq.heappop(heap))
        return self.extend_heap(new_heap)


main = Main()
