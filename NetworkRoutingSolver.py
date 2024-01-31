#!/usr/bin/python3
import sys

from CS312Graph import *
from module import PQ_Dict, PQ_Heap
import time
import math



class NetworkRoutingSolver:
    def __init__( self):
        pass

    def initializeNetwork( self, network ):
        assert( type(network) == CS312Graph )
        self.network = network

    def getShortestPath( self, destIndex ):
        self.dest = destIndex

        path_edges = []
        total_length = 0
        nodeID = destIndex

        # returns no path when there is no path from source to destination
        if self.prev[nodeID] == None:
            return {'cost': math.inf, 'path': []}

        # tracks back from destination to source using the 'prev' map
        while nodeID != self.source:
            for edge in self.network.nodes[self.prev[nodeID]].neighbors:
                if edge.dest.node_id == nodeID:
                    path_edges.append((edge.src.loc, edge.dest.loc, '{:.0f}'.format(edge.length)))
                    total_length += edge.length
                    nodeID = self.prev[nodeID]
                    break

        return {'cost': total_length, 'path': path_edges}


    def computeShortestPaths( self, srcIndex, use_heap=False ):
        self.source = srcIndex
        t1 = time.time()

        self.dijkstras(srcIndex, use_heap)

        t2 = time.time()
        return (t2-t1)

    def dijkstras(self, startNodeIndex, use_heap):
        dist = {}
        prev = {}

        # initializes dist and prev with appropriate values for all nodes and starting node
        for node in self.network.nodes:
            dist[node.node_id] = sys.maxsize
            prev[node.node_id] = None
        dist[startNodeIndex] = 0

        # creates priority queue with array or dict based on user specifications
        if(use_heap):
            priority_queue = PQ_Heap()
        else:
            priority_queue = PQ_Dict()
        priority_queue.makeQueue(dist.keys(), startNodeIndex)

        # iterate through every node
        while not priority_queue.isEmpty():
            # delete node with smallest priority from priority queues
            newStartNodeID = priority_queue.deleteMin()
            # loop through every edge with newStart node as the source
            for neighbor in self.network.nodes[newStartNodeID].neighbors:
                endNodeIndex = neighbor.dest.node_id
                edgeLength = neighbor.length
                # compare new found path distance with current path distance and update if it's short
                if dist[endNodeIndex] > dist[newStartNodeID] + edgeLength:
                    dist[endNodeIndex] = dist[newStartNodeID] + edgeLength
                    prev[endNodeIndex] = newStartNodeID
                    priority_queue.decreaseKey(endNodeIndex, dist[newStartNodeID] + edgeLength)

        self.dist = dist
        self.prev = prev








