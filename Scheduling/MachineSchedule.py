from datetime import datetime
import heapq

from Scheduling.OrderData import OrderData
from Scheduling.Node import Node


class Main:
    def __init__(self):
        self.orderData = self.load_data()

        now = datetime.today()
        print('Start in ', now)

        self.skylineList = self.heap()

        end = datetime.today()  # Get Run time
        print(len(self.skylineList))
        print('--------------SKYLINE-------------')
        for skyline in self.skylineList:
            skyline.print_path()
            skyline.print_element()
            print()

        print(len(self.skylineList))
        print('End in', end)
        print('Spend time: ', end - now)

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

    def heap(self):
        # Initial the Heap
        heap = []
        sequence = 0  # For record the order that pushed into the heap
        for data in self.orderData:
            node = Node(data)
            heapq.heappush(heap, (node.get_sum(), sequence, node))
            sequence += 1
            # Compare sequence when Sum are same (First In First Out)

        # Extend Heap
        skyline_list = []
        while heap:  # Keep Running when heap not empty
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
                    if len(node.scheduledData) == 4:  # Limit how many nodes in each path
                        break
                    new_node = node.copy()
                    if new_node.add_data(data):
                        heapq.heappush(heap, (new_node.get_sum(), sequence, new_node))
                        sequence += 1
                        is_leaf = False
                # If it is a Leaf then throw into Skyline list
                if is_leaf:
                    skyline_list.append(node)
        return skyline_list


main = Main()
