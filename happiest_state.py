import sys
import json
import operator
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
    sent_file = open(sys.argv[1],'r')
    tweet_file = open(sys.argv[2],'r')
    #print sys.argv[1]
    #print sys.argv[2]
    #hw()
    #lines(sent_file)
    #lines(tweet_file)
    states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}
    dict_senti = get_senti_dict(tweet_file)    
    
    
    state_senti = {}
    count = {}
    for k,v in states.items():
        state_senti[k] = 0
        count[k] = 0
    #print state_senti
        
    
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
                
                if 'place' in tweet.keys():
                    
                    if tweet['place'] is not None: 
                        if tweet['place']['country_code'] == 'US':
                            state_obj = tweet['place']['full_name'].encode('utf-8')
                            if state_obj.find(',') != -1:
                                
                                state = tweet['place']['full_name'].encode('utf-8').split(',')[1].strip()
                                if (state in states):
                                    state_senti[state] = state_senti[state] + senti_score
                                    count[state] = count[state] + 1 
                #if 'user' in tweet.keys():
                    #print tweet['user']['location'].encode('utf-8')
                    
                    #words = tweet['text'].encode('utf-8').split()             
                    #for word in words:
                     #   if word in dict_senti:
                        
                        
                      #      senti_score = senti_score + dict_senti[word]
                #print tweet['text'].encode('utf-8'), senti_score
                
                #if 'text' in tweet.keys():
                 #   print tweet['text'].encode('utf-8')
            
        #sys.stdout.write('%d\n'%senti_score)
    
    for k,v in state_senti.iteritems():
        state_senti[k] = float(v)/(count[k]+1)
        
    #print state_senti
    fout = open('state_sentiment.csv','w')
    
    for k,v in state_senti.iteritems():
        fout.write('%s,%s\n' %(k,v))

    fout.close()
    
    sorted_senti = sorted(state_senti.items(),key = operator.itemgetter(1),reverse = True)
    sys.stdout.write('%s'%sorted_senti[0][0])
        
if __name__ == '__main__':
    main()
