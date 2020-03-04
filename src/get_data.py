from sodapy import Socrata




def get_data1(app_key:str,page_size:int,num_pages=None):
	list=[]
	client=Socrata("data.cityofnewyork.us",app_key)

	total_len=int(client.get("nc67-uf89",select='COUNT(*)')[0]['COUNT'])
	print(client.get("nc67-uf89",select='COUNT(*)'))

	if num_pages!=None:
		for i in range(int(num_pages)):
			list.append(client.get("nc67-uf89",limit=page_size,offset=int(page_size)*int(i)))

	else:
		count=0
	
		while count<total_len:
			try:
				list.append(client.get("nc67-uf89",limit=page_size,offset=counter*page_size))
				count=count+page_size
			except:
				pass
		
		# for j in range(int(total_len)):
		# 	list.append(client.get("nc67-uf89",limit=page_size,offset=int(j)*int(page_size))

	# return list
	# print(total_len)