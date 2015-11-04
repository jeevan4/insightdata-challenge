# Program that calculates the number of tweets cleaned
import simplejson as sj
import sys



input_file = open('../tweet_input/tweets.txt')
output = open('../tweet_output/ft1.txt','w')
counter = 0
for line in input_file:
    try:
        json = sj.loads(line.strip())
        timestamp = json['created_at']
        text = json['text']
        escaped_text = ''.join([i if ord(i) != 10 and ord(i) != 9 else '' for i in text])
        output.write('%s\t(timestamp: %s)\n'%(escaped_text,timestamp ))
    except UnicodeEncodeError:
        counter +=1
        text = ''.join([i if ord(i) < 128 and ord(i) != 10 and ord(i) !=9 else '' for i in text])
        output.write('%s\t(timestamp: %s)\n'%(text,timestamp))
    except KeyError:
        pass
output.write('\n%s tweets contained unicode.'%counter)