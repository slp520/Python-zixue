import requests

req = requests.get('http://www.nnzhp.cn', data={'username': 'xxx'}, cookies={'k': 'v'},
                   headers={'User-Agent': 'Chrome'}, verify=False, timeout=3)  # 发送get请求，data是请求数据，
# cookies是要发送的cookies，headers是请求头信息，verify=False是https请求的时候要加上，要不然会报错。
# timeout参数是超时时间，超过几秒钟的话，就不再去请求它了，会返回timeout异常
# 这些都可以不写，如果有的话，可以加上
req2 = requests.post('http://www.nnzhp.cn', data={'username': 'xxx'}, cookies={'k': 'v'},
                     headers={'User-Agent': 'Chrome'}, files={'file': open('a.txt')}, timeout=3)  # 发送post请求，data是请求数据，
# cookies是要发送的cookies，headers是请求头信息，files是发送的文件，verify=False是https请求的时候要加上，
# 要不然会报错,timeout参数是超时时间，超过几秒钟的话，就不再去请求它了，会返回timeout异常
# 这些都可以不写，如果有的话，可以加上

req3 = requests.put('http://www.nnzhp.cn')  # put方式请求
req4 = requests.patch('http://www.nnzhp.cn')  # patch方式请求
req5 = requests.delete('http://www.nnzhp.cn')  # delete方式请求
req6 = requests.options('http://www.nnzhp.cn')  # options方式请求，用法和上面的get、post都一样

print(req.status_code)  # 获取返回状态码
print(req.content)  # 获取返回的内容，二进制格式,一般下载图片、视频用这个
print(req.text)  # 获取返回的内容，字符串格式
print(req.json())  # 获取返回的内容，json格式,这个必须是返回的是json才可以使用，否则会报错
print(req.headers)  # 获取响应头
print(req.cookies)  # 获取返回的cookie
print(req.encoding)  # 获取返回的字符集