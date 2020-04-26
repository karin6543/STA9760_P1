from sodapy import Socrata
from src.get_data import get_data1
from sys import argv
import os




if __name__ == '__main__':



	APP_KEY=os.environ['APP_KEY']


	default_args = {
		"APP_KEY": APP_KEY,
		"page_size": None,
		"num_pages": None,
		"output": None,
	}


	for arg in argv[1:]:
		argname, argval = arg.split('=')
		if argname[2:] in default_args:
				default_args[argname[2:]] =argval
			

	if default_args["APP_KEY"]==None:
		raise Exception('missing APP KEY!!!')

	if default_args["page_size"]==None:
		raise Exception('ya got to specify page size!!!')

	if default_args["num_pages"]==None:
		print('ya didn\'t told me about the Number of Page you want, I am gonna get all of...' )


	raw_data=get_data1(default_args["APP_KEY"],default_args["page_size"],default_args["num_pages"])

	with open(default_args["output"],"w") as fw:
	
		for item in raw_data:
			for j in item: 
				fw.write(str(j)+'\n')
