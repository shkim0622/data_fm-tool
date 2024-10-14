import yaml

with open('yaml1.yaml', 'r') as f:
    a = yaml.load(f, Loader=yaml.FullLoader)
    print("org : ", a)

data = {'person1': [{'name': 'C', 'age': 30, 'cmd': 'happy', 'value': 300}]}

for key, value in data.items():
    if key not in a:
        a[key] = value
    else:

        pass

# 수정된 데이터 출력
print("updated: ", a)

# YAML 파일에 쓰기
with open('yaml1_new3.yaml', 'w') as f:
    yaml.dump(a, f)
