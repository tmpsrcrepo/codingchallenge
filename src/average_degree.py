from hashtag_graph import * #class hashtag_graph
import sys
import json
import time
from datetime import datetime

def preprocessTime(tweet_time):
    ts= time.strptime(tweet_time,'%a %b %d %H:%M:%S +0000 %Y')
    return time.mktime(ts)

def preprocessHashtags(hashtag_):
    #retrieve hashtag texts
    return [h['text'] for h in hashtag_]

def writeOutput(filename,list_):
    with open(filename, 'w') as f:
        for t in list_:
            f.write(t + '\n')

def calculateAverage(filename):
    #initiate a hashtagGraph object
    hashtagGraph = HashTagGraph()
    min_ = float('Inf')
    max_ = 0
    for line in open(filename,'r'):
        data = json.loads(line)

        if 'created_at' in data:
            
            timestamp =  preprocessTime(data['created_at'])
            hashtags = data['entities']['hashtags']
            #only handle nonempty hashtags
            if len(hashtags)>0:
                hashtags = preprocessHashtags(hashtags)
                hashtagGraph.updateNewTweet(timestamp,hashtags)
                yield(hashtagGraph.calculateAvg())

def main():
    file_path = (sys.argv[1])
    print file_path
    out_path = open(sys.argv[2],'wr')
    tweets = calculateAverage(file_path)
    out_path.writelines('%s\n' % i for i in list(tweets))
#
#tweets = calculateAverage('./tweets.txt')
#print list(tweets)
#print time.time()-start

if __name__ == '__main__':
    main()
