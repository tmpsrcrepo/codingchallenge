# codingchallenge

Required dependencies:  (should be default modules, but list them down below just in case)

Modules: collections,itertools,heapq


(Short summary of my code):
1. average_degrees.py: read tweets from a json file input and continuously update hash tag graph (class structure defined in hashtag_graph.py).
2. hashtag_graph.py: defiend a class called HashTagGraph. It maintains the following fields:
* total (total number of degrees)
* maxTime (most recent timestamp)
* minTime (least recent timestamp)
* threshold (maxTime - 60 sec)
* cache (a minheap storing (timestamp, edge pairs), minTime = timestamp of root of the minheap. The reason of using min heap is that it takes O(1) to retrieve the minimum value, and takes O(lg n) to insert a variable to keep the order. 
* degrees (a hashmap storing (node:degree) pairs. if an edge doesn't exist, then the degrees of two nodes on the same edge will be increased by 1. When remove a tweet, we decrement the degree value by 1 if one of its edges is deleted. We remove the (node:degree) pair if degree = 0)
* edges (a hashmap storing (edge pair:count). Since the graph is undirected, we only place one sorted order of edge pair into the graph instead of both directions. We increment count if we've seen this edge more than once. When we remove a tweet, we decrement the edge count. We only remove the edge if the edge count = 0)
