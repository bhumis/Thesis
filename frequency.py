import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

    
def main():
    sent_file = open(sys.argv[1])
    term = {}    
    while 1:
        line = sent_file.readline()
         
        if not line:
            break
            
        tweet = json.loads(line)
        if 'deleted' not in tweet.keys() and 'lang' in tweet.keys():
            if tweet['lang'] == 'en':
                words = tweet['text'].encode('utf-8').split()             
                for word in words:
                    if word not in term:
                        term[word] = 1 
                    else:
                        term[word] = term[word] + 1 
    sum = 0 # to keep track of the total 
    for k,v in term.items():
        sum = sum + v 
    for k,v in term.items():
        v = float(v)/sum 
        sys.stdout.write('%s %s\n' %(k,v))
    
                        
                        
                        
                        
               #print tweet['text'].encode('utf-8'), senti_score
                
                #if 'text' in tweet.keys():
                 #   print tweet['text'].encode('utf-8')
            
        #sys.stdout.write('%d\n'%senti_score)
if __name__ == '__main__':
    main()
