import json

# 사전 자료형 데이터 선언

user = {
    "id": "gildong",
    "password": "1!2@3#4$",
    "age": 30,
    "hobby": ["football", "programming"]

}

# 파이썬 변수를 JSOn 객체로 변환
json_data = json.dumps(user, indent=4)
print(json_data)

# JSOn 데이터로 변환하여 파일로 저장
with open("user.json", "w", encoding="utf-8") as file:
    json_data = json.dump(user, file, indent=4)

#목킹이란 어떠한 기능이 있는 것처럼 흉내내어 구현한 것을 의미한다.
# 가상의 REST API 제공 https://jsonlaceholder.typicode.com/

