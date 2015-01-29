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
        scores[term] = int(score)
    return(scores)
    
def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    #hw()
    #lines(sent_file)
    #lines(tweet_file)
    dict_senti = get_senti_dict(tweet_file)    
    
    new_senti = {}
    count = {} 
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
                for word in words:
                    if word not in new_senti:
                        new_senti[word] = senti_score
                        count[word] = 1 
                    else:
                        new_senti[word] = new_senti[word] + senti_score
                        count[word] = count[word] + 1 
    for k,v in new_senti.items():
        v = float(v)/count[k]
        sys.stdout.write('%s %s\n' %(k,v))
    
                        
                        
                        
                        
               #print tweet['text'].encode('utf-8'), senti_score
                
                #if 'text' in tweet.keys():
                 #   print tweet['text'].encode('utf-8')
            
        #sys.stdout.write('%d\n'%senti_score)
if __name__ == '__main__':
    main()
