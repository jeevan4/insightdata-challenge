Insight Data Challenge Code Submission

Hi I am Jeevan Vankayala graduate student in Computer Science at the University of New Mexico

The challenge is about extracting tweets from the Json output of Twitter API. I have implemented the project in Python.
Before executing the project kindly check if you have the following installed in your system

1. simplejson
2. networkx
3. matplotlib.pyplot

If any of the library is not present please install them using 'pip'

Eg : pip install simplejson etc.

Feature Extraction 1:
---------------------
input : tweet_input/tweets.txt


output : tweet_output/ft1.txt

Clean and extract the text from the raw JSON tweets that come from the Twitter Streaming API, and track the number of tweets that contain unicode.

1.I have procesed the json tweets, extracted the tweet and timestamp using 'text' and 'created_at' tags.

2.Removed escape and unicode characters, kept track of the number of unicode tweets as requested.

3.Results could be found in tweet_output/ft1.txt

Feature Extraction 2:
---------------------
input : tweet_input/tweets.txt

output : tweet_output/ft2.txt

The second feature will continually update the Twitter hashtag graph and calculates the average degree of the graph. 
The graph has been built using the tweets that arrived in the last 60 seconds as compared to the timestamp of the latest tweet. 

1.I have procesed the json tweets, extracted the hashtag and timestamp from 'entities', 'hashtag' and 'created_at' tags.

2.Collected the hashtags from every tweet which is in between 60 sec and created a hash graph.

3.Calculated the average degrees and output could be found in tweet_output/ft2.txt

