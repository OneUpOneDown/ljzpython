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
# GET https://aweme.snssdk.com/aweme/v1/feed/?type=0&max_cursor=0&min_cursor=-1&count=6&volume=0.0&pull_type=2&need_relieve_aweme=0&ts=1541592345&app_type=lite&os_api=22&device_type=OPPO%20A53m&device_platform=android&ssmix=a&iid=49176391802&manifest_version_code=179&dpi=320&uuid=860793037946646&version_code=179&app_name=aweme&version_name=1.7.9&openudid=a7cff120682f5086&device_id=58850191695&resolution=720*1200&os_version=5.1.1&language=zh&device_brand=OPPO&ac=wifi&update_version_code=1790&aid=1128&channel=sem_baidu_dy_pz&_rticket=1541592345802&as=a1e5bd7e0921ab35a21310&cp=d112bb569e25e555e1awkc&mas=003184703ef31d6d987579202f6fb009e00c8ccc8c4c86accc4686 HTTP/1.1
# Host: aweme.snssdk.com
# Connection: keep-alive
# Cookie: odin_tt=6f5a3571334b43413065424e5253464c8a64efe60875ad1c81e7e3b7f0ae3ad44d354453942e78f220192b3fc2ac6c9d; qh[360]=1; install_id=49176391802; ttreq=1$bd72a992adaec8e4546c6e7c076514a34434825e
# Accept-Encoding: gzip
# X-SS-REQ-TICKET: 1541592345797
# X-SS-TC: 0
# User-Agent: com.ss.android.ugc.aweme/310 (Linux; U; Android 5.1.1; zh_CN; OPPO A53m; Build/LMY47V; Cronet/58.0.2991.0)

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