# example of program that calculates the number of tweets cleaned
import simplejson as sj
import sys
import datetime as dt
from dateutil import parser
import networkx as nx
import matplotlib.pyplot as plt

# reads the input tweet file, scans the file from bottom to get the most latest timestamp
input_file = open(sys.argv[1])
output_file = open(sys.argv[2],'a')
lines = input_file.readlines()
leng = len(lines)
json = sj.loads(lines[leng-1].strip())
last_ts = parser.parse(json['created_at'])
print 'Most Latest Date: ',last_ts
create_ts = last_ts
counter = leng-1
total_has_tags=[]
edge_list=[]
# Loops through the input tweet file, till it reaches a tweet posted 60 seconds ago..
while((last_ts-create_ts).seconds <= 60 and counter>-1):
    try:
        hash_tags = []
        hash_text = json['entities']['hashtags']
        counter -= 1
        # if there is any hash tag in the tweet, extract only the ascii content hash tags from the tweet
        if len(hash_text)>0:
            hash_tags = ['#'+i['text'].encode('ascii','ignore').lower() for i in hash_text if len(i['text'].encode('ascii','ignore')) > 0]
            # print hash_tags,create_ts
        # if the hash tags are more than one, then they are used to build edge-list and to calculate degree
        if len(hash_tags) > 1:
            total_has_tags.append(hash_tags)
        json = sj.loads(lines[counter].strip())
        create_ts = parser.parse(json['created_at'])
    except KeyError:
        counter -= 1
        json = sj.loads(lines[counter].strip())

# Creating all the combinations of hash tags and sorted so as to avoid duplicated edge list
from itertools import combinations
for i in total_has_tags:
    edge_list.append(list(combinations(sorted(i),2)))
# print edge_list
set_list = {j for i in edge_list for j in i} # duplicate edge list is avoided by Set item

# Created Graph using Networkx module, plotted graph and extracted degree and number of nodes
G=nx.Graph()
G.add_edges_from(set_list)
try:
    avg_deg = round(sum(G.degree().values())*1.0/len(G.nodes()),2)
    print len(G.nodes()),avg_deg
    output_file.write('%s\n'%(avg_deg))
except ZeroDivisionError:
    print "No hashtags found in the last 60 seconds to create hash graph"

nx.draw(G,nx.spring_layout(G, scale=2),node_size=500,with_labels=True)
# nx.draw_networkx_labels(G,nx.spring_layout(G),labels=cities)
# plt.savefig('circular_tree.png')
plt.show()
