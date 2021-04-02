import requests
from bs4 import BeautifulSoup
#读取文件
citys=[]
with open("city.txt",'r',encoding="utf-8") as f:
	for line in f.readlines():
		citys.append(line.strip('\n'))
# citys=['静海区','蓟州区']
code='邮编'
citys_code=[]
i=0
for city in citys:
	citys_code.append(city+code)

# url="http://www.baidu.com/s"
url="http://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=baidu&"
# headers = {
# 	'Accept': 'application/json, text/javascript, */*; q=0.01',
#     'Accept-Encoding': 'gzip, deflate, br',
#     'Accept-Language': 'zh-CN,zh;q=0.9',
#     'Connection': 'Keep-Alive',
#     # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
#     'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"'
# }

headers={
	'Accept': 'application/json, text/javascript, */*; q=0.01',
	'Accept-Encoding': 'gzip, deflate, br',
	'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
	'Connection': 'keep-alive',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.63'
}

# print(citys_code[0])
# payloads=[
# 	{'wd':'静海区邮编'},
# 	{'wd':'蓟州区邮编'},
# ]
with open("code.txt",'a',encoding='utf-8') as f:
	for city_code in citys_code:
		payload={
			'wd':city_code
		}
		r=requests.get(url,params=payload,headers=headers)
		# print(r.url)
		r.encoding = 'utf-8'
	
		soup=BeautifulSoup(r.text,'html.parser')
	
		# print(soup.prettify())
		str = "op_exactqa_s_answer c-color-t"
		tag=soup.find("div",class_=str)

		text= citys[i]+'	'+tag.string.strip()
		i+=1
		f.write(text+'\n')
	



