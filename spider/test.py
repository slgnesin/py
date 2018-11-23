import requests

headers={
    'User-Agent':'Fuckyou Unspider Zhihu'
}
r=requests.get('https://www.zhihu.com/explore',headers=headers)
print(r.text)
