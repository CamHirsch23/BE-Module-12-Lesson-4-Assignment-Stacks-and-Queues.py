# server.py

import json
import math
from collections import deque
from shutil import copyfileobj

class KitchenOrderStack:
    def __init__(self):
        self.stack = []

    def add_order(self, order):
        self.stack.append(order)
        print(f"Order added to kitchen stack: {order}")

    def complete_order(self):
        if not self.stack:
            print("No orders to complete.")
            return None
        return self.stack.pop()

class CustomerOrderQueue:
    def __init__(self):
        self.queue = deque()

    def add_order(self, order):
        self.queue.append(order)
        print(f"Order added to customer queue: {order}")

    def process_order(self):
        if not self.queue:
            print("No orders to process.")
            return None
        return self.queue.popleft()

def merge_files(file1, file2, merged_file):
    with open(file1, 'r') as f1, open(file2, 'r') as f2, open(merged_file, 'w') as mf:
        copyfileobj(f1, mf)
        copyfileobj(f2, mf)
    print(f"Files {file1} and {file2} merged into {merged_file}")

if __name__ == "__main__":
    kitchen_stack = KitchenOrderStack()
    kitchen_stack.add_order("Order 1")
    kitchen_stack.add_order("Order 2")
    print(f"Completed: {kitchen_stack.complete_order()}")
    print(f"Completed: {kitchen_stack.complete_order()}")
    print(f"Completed: {kitchen_stack.complete_order()}")

    customer_queue = CustomerOrderQueue()
    customer_queue.add_order("Order A")
    customer_queue.add_order("Order B")
    print(f"Processed: {customer_queue.process_order()}")
    print(f"Processed: {customer_queue.process_order()}")
    print(f"Processed: {customer_queue.process_order()}")

    merge_files('file1.txt', 'file2.txt', 'merged_file.txt')

    # Add a newline at the end of the file
    with open('merged_file.txt', 'a') as file:
        file.write('\n')
