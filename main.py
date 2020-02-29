from sodapy import Socrata
from src.get_data import get_data1
from sys import argv



if __name__ == '__main__':


	MY_MAIN=argv[0]
	APP_KEY=argv[1]
	PAGE_SIZE=argv[2]
	NUM_PAGE=argv[3]
	OUTPUT=argv[4]

	default_args = {
		"APP_KEY": None,
		"PAGE_SIZE": None,
		"NUM_PAGE": None,
		"OUTPUT": None,
	}


	for arg in argv[1:]:
		argname, argval = arg.split('=')

		if argname[2:] in default_args:
			default_args[argname[2:]] = argval

	

	# print(get_data1('InDdKBeT33KdisYHHQEAfpTlG',10,1))
	# APP_KEY2=APP_KEY[APP_KEY.index("=")+1:len(APP_KEY)]
	# PAGE_SIZE2=PAGE_SIZE[PAGE_SIZE.index("=")+1:len(PAGE_SIZE)]
	# NUM_PAGE2=NUM_PAGE[NUM_PAGE.index("=")+1:len(NUM_PAGE)]
	# OUTPUT2=OUTPUT[OUTPUT.index("=")+1:len(OUTPUT)]

	data=get_data1(default_args["APP_KEY"],default_args["PAGE_SIZE"],default_args["NUM_PAGE"])



	with open(default_args["OUTPUT"],"w") as fw:
		for item in data:
			for j in item: 
				fw.write(str(j)+'\n')
