import re

urls=set()

str1='http://mail.baidu.com'
str2='http://music.douban.com'
str3='http://mail.douban.com'
str4='http://baike.dd.baidu.com'
str5='./test.html'

strs=[str1,str2,str3,str4,str5]

keystr='baidu.com'

for str in strs:
    if keystr in str or 'http' not in str:
        print('found inner:',str)
    else:
        print('found outer',str)
        urls.remove(str)

strurls='\n'.join(urls)

print(strurls)