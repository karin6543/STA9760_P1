from sodapy import Socrata



# data=client.get("nc67-uf89",limit=10)


# client.get("nc67-uf89",limit=10,offset=10)


# client.get("nc67-uf89",select='COUNT(*)')

def get_data1(app_key:str,page_size:int,num_pages=None):
	list=[]
	client=Socrata("data.cityofnewyork.us",app_key)
	total_len=client.get("nc67-uf89",limit=page_size,select='COUNT(*)')
	if num_pages!=None:
		for i in range(int(num_pages)):
			list.append(client.get("nc67-uf89",limit=page_size,offset=page_size*int(i)))

	else:
		# count=0
	
		# while num_pages==None:
		# 	try:
		# 		list.append(client.get("nc67-uf89",limit=page_size,offset=counter*page_size))
		# 		count+=1
		# 	except:
		# 		num_pages==0

		for i in range(total_len):
			list.append(client.get("nc67-uf89",limit=page_size,offset=counter*page_size))
		# 


	return list