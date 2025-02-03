# HTTP 요청을 보낼 수 있도록 도와주는 requests 라이브러리 import
import requests
import json
# 무작위 사용자 정보를 제공해주는 API의 URL
url = 'https://random-data-api.com/api/v2/users'

# requests.get(url)을 통해 API에 요청을 보냄
# 서버로부터 응답(Response)을 JSON 형태로 받아 Python 객체(딕셔너리/리스트 등)로 변환
response = requests.get(url).json() #json명령어는 딕셔너리형태로 받음

response=json.dumps(response,indent=4)

#딕셔너리와 json의 차이
#1.json은 큰따옴표만 사용
#2.key는 무조건 문자열
# 받은 응답 데이터(딕셔너리 형태)를 출력
print(response)
