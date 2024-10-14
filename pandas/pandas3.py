import pandas as pd

print('--------.csv 파일 -------')
pandas3_csv= pd.read_csv('./pandas3.csv')
print(pandas3_csv)

print('--------.xml 파일 -------')
pandas3_xml = pd.read_xml('./pandas3.xml')
print(pandas3_xml)

print('--------.json 파일 -------')
pandas3_json= pd.read_json('./pandas3.json')
print(pandas3_json)

print('--------.pkl 파일 -------')
pandas3_pickle =pd.read_pickle('./pandas3.pkl')
print(pandas3_pickle)

