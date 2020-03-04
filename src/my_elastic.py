from elasticsearch import Elasticsearch
from datetime import datetime

es = Elasticsearch()

def push_data(data):


	es = Elasticsearch()


	count=1

	for my_dict in data:
		for item in my_dict:
			try:
				today=datetime(2020, 3, 3, 0, 0)
				item['timestamp']=today
				item['issue_date']=datetime.strptime(item['issue_date'], '%m/%d/%Y')
		# print(item.keys())
				res = es.index(index="test", doc_type='tweet', id=count, body=item)
		# print(count)
				count=count+1
			except:
				pass
				
	
			
		

