#!/usr/bin/python
#-*- coding: utf-8 -*-

import requests
from requests.auth import HTTPBasicAuth
from configparser import ConfigParser
import json

class ThousandEyesApi:

	def __init__(self):
		te_api_config = ConfigParser()
		te_api_config.read("config.ini")
		self.email = te_api_config['TE']['email']
		self.authToken = te_api_config['TE']['token']
		self.base_url = te_api_config['TE']['base_url']
		self.accountGroupId = te_api_config['TE']['accountGroupId']
		print("self.accountGroupId = accountGroupId: ", self.accountGroupId)
		print(self.base_url)

	def getRequest(self, endpoint: str, uriParameters = {}):
		httpBasicAuth = HTTPBasicAuth(self.email, self.authToken)
		# https://requests.readthedocs.io/en/latest/user/authentication/#basic-authentication
		
		uriParameters['Content-Type'] = "application/json"
		uriParameters['Accept'] = "application/json"
		uriParameters['format'] = 'json'
		if (self.accountGroupId != None):
			uriParameters['aid'] = self.accountGroupId

		resp = requests.get(url=self.base_url.strip('/') + '/' + endpoint.strip('/') + ".json", auth= httpBasicAuth)
		print (resp.status_code)
		return (resp)


	# def getPureUrlRequest(self, uri):
	# 	"""
	# 	Performs GET HTTP request to desired API URL and returns JSON data
	# 	Does not manage parameters. Use for pagination

	# 	Parameters
	# 	----------
	# 	url : str
	# 		ThousandEyes API endpoint URL

	# 	Returns
	# 	-------
	# 	object
	# 		ThousandEyes API result object. Refer to the API endpoint documentation
	# 		for return object description.
	# 	"""

	# 	return


	def postRequest(self, endpoint: str, properties, uriParameters = {}):
		httpBasicAuth = HTTPBasicAuth(self.email, self.authToken)
		# https://requests.readthedocs.io/en/latest/user/authentication/#basic-authentication
		
		uriParameters['Content-Type'] = "application/json"
		uriParameters['Accept'] = "application/json"
		# uriParameters['format'] = 'json'
		if (self.accountGroupId != None):
			uriParameters['aid'] = self.accountGroupId

		resp = requests.post(url=self.base_url.strip('/') + '/' + endpoint.strip('/') + ".json" , auth= httpBasicAuth, data=properties, headers = uriParameters)
		# print (resp.status_code)
		return (resp.json())
		