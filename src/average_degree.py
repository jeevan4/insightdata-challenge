# example of program that calculates the number of tweets cleaned
import simplejson as sj
import re as re
from dateutil import parser
import datetime as dt
import networkx as nx
import matplotlib.pyplot as plt

input_file = open('../tweet_input/tweets.txt')
output_file = open('../tweet_output/ft2.txt','a')
lines = input_file.readlines()
leng = len(lines)
json = sj.loads(lines[leng-1].strip())
last_ts = parser.parse(json['created_at'])
print last_ts
create_ts = last_ts
counter = leng-1
total_has_tags=[]
edge_list=[]
while((last_ts-create_ts).seconds <= 60 and counter>-1):
    try:
        hash_tags = []
        hash_text = json['entities']['hashtags']
        counter -= 1
        if len(hash_text)>0:
            hash_tags = ['#'+i['text'].encode('ascii','ignore').lower() for i in hash_text if len(i['text'].encode('ascii','ignore')) > 0]
            # print hash_tags,create_ts
        if len(hash_tags) > 1:
            total_has_tags.append(hash_tags)
        json = sj.loads(lines[counter].strip())
        create_ts = parser.parse(json['created_at'])
    except KeyError:
        counter -= 1
        json = sj.loads(lines[counter].strip())

from itertools import combinations
for i in total_has_tags:
    edge_list.append(list(combinations(sorted(i),2)))
# print edge_list

set_list = {j for i in edge_list for j in i}
G=nx.Graph()
G.add_edges_from(set_list)
print len(G.nodes()),sum(G.degree().values())*1.0/len(G.nodes())

nx.draw(G,nx.spring_layout(G, scale=2),node_size=500,with_labels=True)
# nx.draw_networkx_labels(G,nx.spring_layout(G),labels=cities)
plt.savefig('circular_tree.png')

plt.show()
