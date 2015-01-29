import sys
import json
 
def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def get_senti_dict(handler):
    scores = {}
    while 1:
        line = handler.readline().rstrip()
        if not line:
            break
        term,score = line.split('\t')
        #print line
        #print term, score
        scores[term] = int(score)
    return(scores)

def main():
    sent_file = open(sys.argv[1],'r')
    tweet_file = open(sys.argv[2],'r')
    #print sys.argv[1]
    #print sys.argv[2]
    #hw()
    #lines(sent_file)
    #lines(tweet_file)
    
    dict_senti = get_senti_dict(tweet_file)    
    
    fout = open('tweet_sentiments.txt','w')
    while 1:
        line = sent_file.readline()
        senti_score = 0 
        if not line:
            break
            
        tweet = json.loads(line)
        if 'deleted' not in tweet.keys() and 'lang' in tweet.keys():
            if tweet['lang'] == 'en':
                words = tweet['text'].encode('utf-8').split()             
                for word in words:
                    if word in dict_senti:
                        
                        
                        senti_score = senti_score + dict_senti[word]
                tweet_text = tweet['text'].encode('utf-8')
                #print tweet_text
                       
                fout.write('%s,%s\n' %(tweet_text.rstrip(), senti_score))
                
                #if 'text' in tweet.keys():
                 #   print tweet['text'].encode('utf-8')
        
        #if senti_score !=0:
        #    sys.stdout.write('%d\n'%senti_score)
    fout.close()
     
if __name__ == '__main__':
    main()
