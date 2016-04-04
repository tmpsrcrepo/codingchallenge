import collections
from collections import defaultdict
import itertools
import heapq
import math

#Class for all the operations of calculating the number of hashtags
class HashTagGraph(object):
    def __init__(self):
        self.total = 0 #total sum of degrees
        self.maxTime = 0
        self.minTime = 0
        self.threshold = 0
        self.cache = [] #store (timestamp,hashtaglist) pair on a min-heap (priority queue)
        self.degrees = defaultdict(int) #record degrees of each edges
        self.edges = defaultdict(int) #record edges and corresponding counts

    def updateNewTweet(self,timestamp,hashtag_list):
        #create combination of pairs
        pairs = list(itertools.combinations(hashtag_list, 2))
        if timestamp < self.threshold: #ignore the tweet if it comes before the threshold
            return
        
        #when the new timestamp is the most recent, update and check if we need to remove hashtags
        elif timestamp > self.maxTime:
            self.maxTime = timestamp
            self.threshold = timestamp - 60
            self.removeHashtagsBefore()
        #if there are more than 2 hashtags, we push the pair to the heap
        if pairs:
            #the reason for using heap is that: it's more efficient than using list, it takes O(1) to remove the min element (oldest timestamp)
            heapq.heappush(self.cache,(timestamp,pairs))
            self.updateDegrees(pairs)

    def orderedPair(self,pair):
        hashtag1,hashtag2 = pair
        if hashtag1[0]<hashtag2[0]:
            return (hashtag1,hashtag2)
        return (hashtag2,hashtag1)


    def addPair(self,pair):
        pair = self.orderedPair(pair)
        hashtag1,hashtag2 = pair
        if not pair in self.edges:
            #update total number of pairs
            self.total+=2
            #increment degree number if this is a new pair
            self.degrees[hashtag1]+=1
            self.degrees[hashtag2]+=1
        
        #increment edge count if it's seen more than once
        self.edges[pair]+=1


    def updateDegrees(self,pairs):
        for pair in pairs:
            self.addPair(pair)


    def removePair(self,pair):
        pair = self.orderedPair(pair)
        hashtag1,hashtag2 = pair
        self.edges[pair]-=1
        
        #decrement total counts and degrees only if the edge count == 0
        if self.edges[pair]==0:
            del self.edges[pair]
            self.degrees[hashtag1]-=1
            self.degrees[hashtag2]-=1
            self.total-=2
        
        #if the node has no edges after this point, delete it
        if self.degrees[hashtag1] == 0:
            del self.degrees[hashtag1]
        
        if self.degrees[hashtag2]==0:
            del self.degrees[hashtag2]


    def removeHashtag(self,pairs):
        for pair in pairs:
            self.removePair(pair)

    def removeHashtagsBefore(self):
        
        while self.cache and self.minTime<self.threshold:
            t,pairs = heapq.heappop(self.cache)
            #decrement edges, degree graphs and total
            self.removeHashtag(pairs)
            if self.cache:
                self.minTime = self.cache[0][0]
        
        if not self.cache:
            self.minTime = self.maxTime
        

    def calculateAvg(self):
        #2D decimal places
        if not (self.degrees):
            return format(0.0,'.2f')
        
        v = self.total*1.0/len(self.degrees)
        #need to truncate the ratio to 2 decimal points w/o rounding (since 5/3 = 1.66 instead of 1.67)
        return format(math.floor(v*100)/100,'.2f')








