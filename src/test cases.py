#this is just a test case. I used the provided example in the tutorial to validate my calculation
#it's completely indepedent w/ average_degree.py

from hashtag_graph import *
import time
def preprocessTime(tweet_time):
    ts= time.strptime(tweet_time,'%a %b %d %H:%M:%S +0000 %Y')
    return time.mktime(ts)

def test_case1():
    
    times = ['Thu Mar 24 17:51:10 +0000 2016','Thu Mar 24 17:51:15 +0000 2016','Thu Mar 24 17:51:30 +0000 2016','Thu Mar 24 17:51:55 +0000 2016','Thu Mar 24 17:51:58 +0000 2016','Thu Mar 24 17:52:12 +0000 2016']
    hashtags = [['Spark','Apache'],['Apache','Hadoop','Storm'],['Apache'],['Flink','Spark'],['Spark','HBase'],['Hadoop', 'Apache']]
    return times,hashtags


def test_case2():
    times = ['Thu Mar 24 17:51:10 +0000 2016','Thu Mar 24 17:51:15 +0000 2016','Thu Mar 24 17:51:30 +0000 2016','Thu Mar 24 17:51:55 +0000 2016','Thu Mar 24 17:51:58 +0000 2016','Thu Mar 24 17:52:12 +0000 2016','Thu Mar 24 17:52:10 +0000 2016','Thu Mar 24 17:52:20 +0000 2016']
    hashtags = [['Spark','Apache'],['Apache','Hadoop','Storm'],['Apache'],['Flink','Spark'],['Spark','HBase'],['Hadoop', 'Apache'],['Flink','HBase'],['Kafka', 'Apache']]
    return times,hashtags

def validate():
    #initiate a hashtagGraph object
    
    hashtagGraph = HashTagGraph()
    times,hashtags = test_case2()
    for i in xrange(len(times)):
        hashtag_ = hashtags[i]
        time_ = preprocessTime(times[i])
        hashtagGraph.updateNewTweet(time_,hashtag_)
        print
        print hashtagGraph.calculateAvg()


validate()


