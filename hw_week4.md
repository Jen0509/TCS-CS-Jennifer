# 📌 HW Week4 - GET 요청하기

## 1. 제목

#      requests 모듈을 활용하여 GET 요청하기

## 2. 이름

#      김지윤(jennifer)


## 3. 제출일

#      24.09.30 (월)


## 4. 과제 목표

#      requests 모듈이 뭔지 알고, 왜 사용해야 하는지 알기. requests 모듈을 설치한 후 Get 요청할 줄 알기.

## 5. 코드 실행 결과

```python
import requests

response = requests.get("https://jsonplaceholder.typicode.con/posts/1")

print("Status Code :", response.status_code)

print("Response Body:", response.text)
```

#result

(env_CS) jennifer@gimjiyun-ui-MacBookAir env_CS % /Users/jennifer/Desktop/python/TCA
-CS-Jenn/env_CS/bin/python /Users/jennifer/Desktop/python/TCA-CS-Jenn/env_CS/hw.py
/Users/jennifer/Desktop/python/TCA-CS-Jenn/env_CS/lib/python3.9/site-packages/urllib3/__init__.py:35: NotOpenSSLWarning: urllib3 v2 only supports OpenSSL 1.1.1+, currently the 'ssl' module is compiled with 'LibreSSL 2.8.3'. See: https://github.com/urllib3/urllib3/issues/3020
  warnings.warn(
Status Code : 200
Response Body: {
  "userId": 1,
  "id": 1,
  "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
  "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
}
(env_CS) jennifer@gimjiyun-ui-MacBookAir env_CS % 

## 6. 문제 해결 과정 및 배운점

requests 모듈을 사용하는 것을 배웠다.
프로그램 작성 중 에러가 떴는데 글자 하나를 잘못 입력한 것이었다. 그래서 다시 고쳤더니 잘 작동되었다.
import를 사용해서 모듈을 불러오는 것을 배웠다. 
