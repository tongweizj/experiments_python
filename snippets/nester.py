"""
this is wtong's frist code
python 能用中文注释吗？
"""

def print_lol(the_list):
	"""
	print_lol can print every item in a list
	"""
	for each_item in the_list : 
		if isinstance(each_item, list):
			print_lol(each_item,0)
		else :
			print(each_item)
			
