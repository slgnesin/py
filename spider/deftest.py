def get(tag,str):
    if tag=='str1':
        def getstr1(str):
            print('str1:',str)
        return getstr1(str)
    elif tag == 'str2':
        def getstr2(str):
            print('str2:',str)
        return getstr2(str)

get('str2','Test')