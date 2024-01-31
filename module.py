import sys

class PQ_Dict:
    def __init__(self):
        self.nodeID_to_distance = {}

    # Time Complexity: O(1)
    # Space Complexity: 0(n)
    #Adds a new element to the set
    def insert(self, nodeID, distance):
        self.nodeID_to_distance[nodeID] = distance

    # Time Complexity: O(n)
    # Space Complexity: 0(n)
    # Build a priority queue out of the given elements, with default start values
    def makeQueue(self, node_set, startNode_id):
        for node in node_set:
            self.nodeID_to_distance[node] = sys.maxsize;
        self.nodeID_to_distance[startNode_id] = 0;

    # Time Complexity: O(n)
    # Space Complexity: 0(1)
    # Return the element with the smallest key, and remove it from the set
    def deleteMin(self):
        min_key = min(self.nodeID_to_distance, key=self.nodeID_to_distance.get)
        self.nodeID_to_distance.pop(min_key)
        return min_key

    # Time Complexity: O(1)
    # Space Complexity: 0(1)
    # Accommodates the decrease in key value of a particular element
    def decreaseKey(self, key, newDistance):
        self.nodeID_to_distance[key] = newDistance

    def isEmpty(self):
        return len(self.nodeID_to_distance) == 0


class PQ_Heap:
    def __init__(self):
        self.heap_tree_list = []
        self.nodeID_to_priority = {}
        self.nodeID_to_position = {}

    # Time Complexity: O(log(n))
    # Space Complexity: 0(1)
    # Adds a new element to the set
    def insert(self, nodeID, distance):
        # add new node to the end of the heap
        self.heap_tree_list.append(nodeID)
        self.nodeID_to_priority[nodeID] = distance
        self.nodeID_to_position[nodeID] = len(self.heap_tree_list) - 1

        # moves node to the right place
        self.bubble_up(nodeID)

    # Time Complexity: O(n)
    # Space Complexity: 0(n)
    # Build a priority queue out of the given elements, with default start values
    def makeQueue(self, node_set, startNode_ID):
        self.heap_tree_list.append(startNode_ID)
        self.nodeID_to_priority[startNode_ID] = 0
        self.nodeID_to_position[startNode_ID] = 0
        for node in node_set:
            if not node==startNode_ID:
                self.heap_tree_list.append(node)
                self.nodeID_to_priority[node] = sys.maxsize
                self.nodeID_to_position[node] = len(self.heap_tree_list) - 1

    # Time Complexity: O(log(n))
    # Space Complexity: 0(1)
    # Return the element with the smallest key, and remove it from the set
    def deleteMin(self):
        minID = self.heap_tree_list[0]
        lastNodeID = self.heap_tree_list[-1]

        #swap places in heap tree
        self.heap_tree_list[0] = lastNodeID
        self.heap_tree_list.pop()

        #if there is nothing left in queue after popping last element, return
        if len(self.heap_tree_list) == 0:
            return minID

        #update the postions
        self.nodeID_to_position[lastNodeID] = 0
        del self.nodeID_to_position[minID]

        #bubble down the node that got pushed to the top
        self.bubble_down(lastNodeID)

        return minID

    # Time Complexity: O(log(n))
    # Space Complexity: 0(1)
    # Accommodates the decrease in key value of a particular element
    def decreaseKey(self, key, newDistance):
        self.nodeID_to_priority[key] = newDistance

        # moves node to the right place
        self.bubble_up(key)

    def isEmpty(self):
        return len(self.heap_tree_list) == 0

    # swaps a node and it's parent if the parent's priority is smaller than the node's priority
    def bubble_up(self, nodeID):
        parentID = self.find_parent(nodeID)
        while parentID is not None and self.nodeID_to_priority[parentID] > self.nodeID_to_priority[nodeID]:
            self.swap(nodeID, parentID)
            parentID = self.find_parent(nodeID)

    # swaps a node and it's child if the child's priority is smaller than the parent's priority
    def bubble_down(self, nodeID):
        childID = self.find_lowest_priority_child(nodeID)
        while childID is not None and self.nodeID_to_priority[childID] < self.nodeID_to_priority[nodeID]:
            self.swap(nodeID, childID)
            childID = self.find_lowest_priority_child(nodeID)

    # returns the id of a node's parent
    def find_parent(self, nodeID):
        if self.nodeID_to_position[nodeID] == 0:
            return None
        parentIndex = (self.nodeID_to_position[nodeID] - 1) // 2
        return self.heap_tree_list[parentIndex]

    # returns the id of a node's child with the lowest priority
    def find_lowest_priority_child(self, nodeID):
        right_child_index = (self.nodeID_to_position[nodeID] + 1) * 2
        left_child_index = (self.nodeID_to_position[nodeID] + 1) * 2 - 1

        #no children
        if left_child_index > len(self.heap_tree_list) - 1:
            return None
        #2 children
        elif right_child_index <= len(self.heap_tree_list) - 1:
            right_nodeID = self.heap_tree_list[right_child_index]
            left_nodeID = self.heap_tree_list[left_child_index]

            if self.nodeID_to_priority[left_nodeID] < self.nodeID_to_priority[right_nodeID]:
                return left_nodeID
            else:
                return right_nodeID
        #1 child
        else:
            return self.heap_tree_list[left_child_index]

    # swaps two nodes in the heap tree
    def swap(self, node1_id, node2_id):
        node1_position = self.nodeID_to_position[node1_id]
        node2_position = self.nodeID_to_position[node2_id]

        self.nodeID_to_position[node1_id] = node2_position
        self.nodeID_to_position[node2_id] = node1_position

        self.heap_tree_list[node1_position] = node2_id
        self.heap_tree_list[node2_position] = node1_id




