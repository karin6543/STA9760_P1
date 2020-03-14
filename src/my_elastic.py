from elasticsearch import Elasticsearch
from datetime import datetime


def push_data(data):


	es = Elasticsearch()


	count=1

	for my_dict in data:
		for item in my_dict:
			try:
				today=datetime(2020, 3, 4, 0, 0)
				item['timestamp']=today
				item['issue_date']=datetime.strptime(item['issue_date'], '%m/%d/%Y')
				item['fine_amount']=float(item['fine_amount'])
				item['penalty_amount']=float(item['penalty_amount'])
				item['interest_amount']=float(item['interest_amount'])
				item['reduction_amount']=float(item['reduction_amount'])
				item['payment_amount']=float(item['payment_amount'])
				item['amount_due']=float(item['amount_due'])
				# print(item)
		# print(item.keys())
				res = es.index(index="test-index", doc_type='tweet', id=count, body=item)
		
		# print(count)
				count=count+1	
			except:
				pass
			
	
			
		

