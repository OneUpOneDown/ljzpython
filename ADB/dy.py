import json,os
import requests
import collections
import re
# def response(flow):
#     url='https://api.amemv.com/aweme/v1/aweme/post/'
#     #筛选出以上面url为开头的url
#     if flow.request.url.startswith(url):
#         text=flow.response.text
#         #将已编码的json字符串解码为python对象
#         data=json.loads(text)
#         # print(data)
#         #在fiddler中刚刚看到每一个视频的所有信息
#         # 都在aweme_list中
#         video_url=data['aweme_list']
#         path='D:/爬虫数据/douyin'
#         if not os.path.exists(path):
#             os.mkdir(path)

#         for each in video_url:
#             #视频描述
#             desc=each['desc']
#             url=each['video']['play_addr']['url_list'][0]
#             # print(desc,url)
#             filename=path+'/'+desc+'.mp4'
#             # print(filename)
#             req=requests.get(url=url,verify=False)
#             with open(filename,'ab') as f:
#                 f.write(req.content)
#                 f.flush()
#                 print(filename,'下载完毕')
# # --------------------- 
path = 'D:/video/'
num = 1788
cf = []
def response(flow):
	global num
	global cf
	# 经测试发现视频url前缀主要是3个
	# target_urls = ['http://v1-dy.ixigua.com/','http://v1-dy-y.ixigua.com/','http://v9-dy.ixigua.com/',
	# 'http://v3-dy.ixigua.com/','http://v6-dy.ixigua.com/','ixigua']
	# for url in target_urls:
		# 过滤掉不需要的url
	matchObj = re.search( r'ixigua', flow.request.url, re.M|re.I)
	print(flow.request.url)
	print(matchObj)
	if matchObj:
	# if flow.request.url.startswith(url):
		cf.append(flow.request.url)
		print(cf)
		if cf.count(flow.request.url) > 1:
 			print('重复URL')
		else:
			# text=flow.response.text
			print('有没有')
			# print(text)
			#将已编码的json字符串解码为python对象
			# data=json.loads(text)
			# video_url=data['aweme_list']
			print('有没有')
			# print(video_url)
			# 设置视频名
			filename = path + str(num) + '.mp4'
			# 使用request获取视频url的内容
				# stream=True作用是推迟下载响应体直到访问Response.content属性
			res = requests.get(flow.request.url, stream=True)
			print(flow.request.url)
			# 将视频写入文件夹
			with open(filename,'ab') as f:
				f.write(res.content)
				f.flush()
				print(filename + '下载完成')
				num += 1
		return cf