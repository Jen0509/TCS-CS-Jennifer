#def 함수를 이용한 사칙연산자 만들기

def add(a,b):
    return a + b
add_result = add(10,5)
print(add_result)

def sub(a,b):
    return a - b
sub_result = sub(10,5)
print(sub_result)

def mul(a,b):
    return a * b
mul_result = mul(10,5)
print(mul_result)

def div(a,b):
    return a / b
div_result = div(10,5)
print(div_result)

# name의 초기값 정하기 name = Alice

def greet(name = "Alice"):
    return f"Hello, {name}"
print(greet())
print(greet("Bob"))

#sum(1,2,3) -> 6
# add(*numbers): *는 숫자의 개수를 모를 때 붙이는 것, 규칙
def add(*numbers):
    return sum(numbers)
print(add(1,2,3,4,5))

#평균 구하기 
def avg(*numbers):
    return sum(numbers)/len(numbers)
print(avg(4,6,5,1))

def avg1(a,b):
    return int((a+b)/2)
print(avg1(2,4))

