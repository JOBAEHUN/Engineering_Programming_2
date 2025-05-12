import pandas as pd

dict1 = {'이름':{0:'한빛', 1:'한결', 2:'한라'},
 '성별':{0:'남자', 1:'남자', 2:'여자'},
 '나이':{0:'20', 1:'21', 2:'20'},
 '키':{0:'180', 1:'177', 2:'160'}}
df = pd.DataFrame(dict1)

df.to_csv('./file.csv',header = True,index = False, encoding='utf-8')

df2 = pd.read_csv('./file.csv', sep=',')
print(df2)