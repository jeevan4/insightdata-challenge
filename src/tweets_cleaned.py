# Program that calculates the number of tweets cleaned
import simplejson as sj
import sys

input_file = open(sys.argv[1])
output = open(sys.argv[2],'w')
counter = 0
for line in input_file:
    try: # extraction of timestamp, tweet text from json. If a unicode tweet is found triggers exception
        json = sj.loads(line.strip())
        timestamp = json['created_at']
        text = json['text']
        escaped_text = ''.join([i if ord(i) != 10 and ord(i) != 9 else '' for i in text])
        output.write('%s\t(timestamp: %s)\n'%(escaped_text,timestamp ))  # writing output to ft1.txt file
    except UnicodeEncodeError:  # to clean the tweets that contain unicode and count them
        counter +=1
        text = ''.join([i for i in text if ord(i) < 128 and ord(i) != 10 and ord(i) !=9])
        output.write('%s\t(timestamp: %s)\n'%(text,timestamp))
    except KeyError: # In the input file there are some json tags which are not related to tweets. We just pass them
        pass
output.write('\n%s tweets contained unicode.'%counter)