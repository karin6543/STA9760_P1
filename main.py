
from sodapy import Socrata
from src.get_data import get_data1
from sys import argv
import os




if __name__ == '__main__':



	APP_KEY=os.environ['APP_KEY']

	default_args = {
		"APP_KEY": APP_KEY,
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




	data=get_data1(default_args["APP_KEY"],default_args["PAGE_SIZE"],default_args["NUM_PAGE"])


	with open(default_args["OUTPUT"],"w") as fw:
	
		for item in data:
			for j in item: 
				fw.write(str(j)+'\n')
