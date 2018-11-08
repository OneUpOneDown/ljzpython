import collections
cf = []
def a_b():
	# global num
	global cf
	# 经测试发现视频url前缀主要是3个
	target_urls = ['a', 'b',
	'c']
	dz = 'as/bc'
	cf.append(dz)
	# print(cf)
	print(cf.count(dz))
	if cf.count(dz) > 1:
	 	print('重复URL')
	else:
		for url in target_urls:
		# 过滤掉不需要的url
			if dz.startswith(url):

				print('正常URL',cf)
				return cf
a_b()
a_b()
a_b()
a_b()
# print([item for item, count in collections.Counter(a).items() if count > 1])
	# 设置视频名
		# filename = path + str(num) + '.mp4'
		# # 使用request获取视频url的内容
		# # stream=True作用是推迟下载响应体直到访问Response.content属性
		# res = requests.get(flow.request.url, stream=True)
# 将视频写入文件夹
	# with open(filename, 'ab') as f:
	# 	f.write(res.content)
	# 	f.flush()
	# 	print(filename + '下载完成')
	# 	num += 1