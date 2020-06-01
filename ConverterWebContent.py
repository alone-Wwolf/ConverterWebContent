import argparse
import re


def main():
	parser = argparse.ArgumentParser(description='convert content type of Http request ')
	parser.add_argument('-t', type=str,help='enter your data json or html ',required=True)
	parser.add_argument('-f', type=str,help='which data you want to convert to it ',required=True)
	args = parser.parse_args()
	
	return args


def define_type(type_):
	currnet_type = type_.t.strip()
	return_current_type = ""

	for t in currnet_type:
		if not currnet_type.startswith("{") and not currnet_type.startswith("<") :
			return_current_type = "html"

		elif currnet_type.startswith("{"):
			return_current_type = "json"

		else:
			print("your data has unknown type")


	return return_current_type


def check_for_format_type(type_of_current_format,c):
	data = main().t.lower().strip()
	if type_of_current_format == c:
		print(f"The Type of current data equal to data you want to convert it {type_of_current_format}" )
		return
	else:
		converted_data(type_of_current_format,data.strip(),c)


def converted_data(data_format_type,data,converted_data_type):

	result_json = ""
	if(data_format_type == "html" and converted_data_type == "json"):
		for t in data:
			if t != "&" and t != "=":
				result_json+=t
			else:
				result_json+='"'+t.replace("=" , ":").replace("&",",")+'"'

		print('{"'+result_json+'"}' + "\n")

	elif (data_format_type == "json" and converted_data_type == "html"):
		for t in data:
			result_json += t.replace("{" ,"").replace("}" ,"").replace('"',"").replace(":","=").replace(",","&")

		print(re.sub(r"\s+", "", result_json), sep='')

	else:
		print("That Format Not supported !")
	



if __name__ == '__main__':
	main_var = main()
	define_type_var = define_type(main_var)
	check_for_format_type_var = check_for_format_type(define_type_var,main_var.f.strip())


