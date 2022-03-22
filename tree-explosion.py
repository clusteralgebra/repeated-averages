from collections import deque

class Node():
    def __init__(self, val):
        self.val = val

n = 100 # dimension

def trial():
    root = Node(1)
    q = deque()
