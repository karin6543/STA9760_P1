from datetime import datetime
from elasticsearch import Elasticsearch
from sys import argv
import os
from src.get_data import get_data1
from sodapy import Socrata
from src.my_elastic import push_data




if __name__ == '__main__':



	# APP_KEY=os.environ['APP_KEY']


	default_args = {
		"APP_KEY": None,
		"PAGE_SIZE": None,
		"NUM_PAGE": None,
		"OUTPUT": None,
	}


	for arg in argv[1:]:
		argname, argval = arg.split('=')
		if argname[2:] in default_args:
				default_args[argname[2:]] =argval
			

	if default_args["APP_KEY"]==None:
		raise Exception('missing APP KEY!!!')

	if default_args["PAGE_SIZE"]==None:
		raise Exception('ya got to specify page size!!!')

	if default_args["NUM_PAGE"]==None:
		print('ya didn\'t told me about the Number of Page you want, I am gonna get all of...' )




	raw_data=get_data1(default_args["APP_KEY"],default_args["PAGE_SIZE"],default_args["NUM_PAGE"])



	push_data(raw_data)


import urllib3
import json
from bs4 import BeautifulSoup
# =================================
# Store some data

http = urllib3.PoolManager()
url = 'http://localhost:9200'

header = {
    'county': 'NY'
    }
# have to send the data as JSON
header = json.dumps(header)


req =http.request('GET',url,header)
# out = urllib3.urlopen(req)
print(req.data)

# # =================================
# # Query the resulting "table"

# url = 'http://localhost:9200/_search?q=count:NY'
# req = http.request('GET',url)
# # out = http.request('GET',req)
# data = BeautifulSoup(req.data)
# print(req)
# # returned data is JSON
# # data = json.loads(data)
# # total number of results
# print(data)

	

# # load a tweet into ES
	
# 	res = es.index(index="test-index", doc_type='tweet', id=2, body=doc)
	# ind=0

	# for item in data:
	# 	count=len(item)
		
	# 	for j in item:
	# 		res=es.index(index="test-index", doc_type='tweet', id=ind, body=j)
	# 		ind=ind+1



				# fw.write(str(j)+'\n')





# query by id
# res = es.get(index="test-index", doc_type='tweet', id=1)
# print(res['_source'])

# es.indices.refresh(index="test-index")

# # search
# res = es.search(index="test-index", body={"query": {"match_all": {}}})
# print("Got %d Hits:" % res['hits']['total'])
# for hit in res['hits']['hits']:
#     print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])
