import sys
import json
import operator

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

    
def main():
    sent_file = open(sys.argv[1])
    hastags = {}    
    while 1:
        line = sent_file.readline()
         
        if not line:
            break
            
        tweet = json.loads(line)
        if 'deleted' not in tweet.keys() and 'lang' in tweet.keys():
            if tweet['lang'] == 'en':
                if 'entities' in tweet.keys():
                    if 'hashtags' in tweet['entities']:
                        for item in tweet['entities']['hashtags']:
                            tags = item['text'].encode('utf-8')
                            if tags not in hastags:
                                hastags[tags] = 1
                            else:
                                hastags[tags] = hastags[tags] + 1 
                        
                        
                        
    sort_tags = sorted(hastags.items(),key = operator.itemgetter(1),reverse = True)
    
    for i in range(1,10):
        sys.stdout.write('%s %s\n' %(sort_tags[i][0],sort_tags[i][1]))
               
                        
               #print tweet['text'].encode('utf-8'), senti_score
                
                #if 'text' in tweet.keys():
                 #   print tweet['text'].encode('utf-8')
            
        #sys.stdout.write('%d\n'%senti_score)
if __name__ == '__main__':
    main()
