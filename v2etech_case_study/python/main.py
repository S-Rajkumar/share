#!/usr/bin/env python3

"""
author : S.Rajkumar
date   : 07-10-2020
"""

import pandas
import requests
import json


headers = {
 'Content-Type': 'application/json; charset=utf-8',
 'User-Agent' : 'XY'
 }
def show_data() :
	data = pandas.read_csv('data.csv')
	data_frame = pandas.DataFrame(data)
	print(data_frame[['id','employee_name','employee_salary','employee_age']])

def get_data() :
	try :
		url = "https://dummy.restapiexample.com/api/v1/employees"
		response = requests.get(url,headers=headers)
		if response.status_code == 200 :
			response_json = json.loads(response.text)
			data = pandas.DataFrame(data=response_json["data"])
			data.to_csv('data.csv')
			return True
		else :
			return False
	except Exception as err :
		print("Issue while get data : "+str(err))
if get_data() :
	print("success\n")
	show_data()
else :
	print("issue")
