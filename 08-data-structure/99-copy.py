# ================================================
# 가변(mutable) 객체 예시
# ================================================
print('가변(mutable) 객체 예시')
a = [1, 2, 3, 4]
b = a
b[0] = 100

print(f'a의 값: {a}')  #
print(f'b의 값: {b}')  #
print(f'a와 b가 같은 객체를 참조하는가? {a is b}')  #

# ================================================
# 불변(immutable) 객체 예시
# ================================================
print('\n불변(immutable) 객체 예시')
a = 20
b = a
b = 10

print(f'a의 값: {a}')  #
print(f'b의 값: {b}')  #
print(a is b)  #

# ================================================
# id() 함수를 사용한 메모리 주소 확인
# ================================================
print('\n메모리 주소 확인')
x = [1, 2, 3]
y = x
z = [1, 2, 3]

print(f'x의 id: {id(x)}')
print(f'y의 id: {id(y)}')
print(f'z의 id: {id(z)}')
print(f'x와 y는 같은 객체인가? {x is y}')
print(f'x와 z는 같은 객체인가? {x is z}')

# ================================================
# 얕은 복사
# ================================================
print('\n얕은 복사 예시')

# 1차원 리스트
a = [1, 2, 3]
b = a[:]  # 슬라이싱
c = a.copy()  # copy() 메서드
d = list(a)  # list() 함수

b[0] = 100
c[0] = 999
d[0] = 8080
print(a)  #
print(b)  #
print(c)  #
print(d)  #

# 다차원 리스트
print('\n다차원 리스트 얕은 복사의 한계')
a = [1, 2, [3, 4, 5]]
b = a[:]

b[0] = 999
print(a)  #
print(b)  #

b[2][1] = 100
print(a)  #
print(b)  #
print(f'a[2]와 b[2]가 같은 객체인가? {a[2] is b[2]}')  #

# ================================================
# 깊은 복사
# ================================================
import copy

print('\n깊은 복사 예시')
a = [1, 2, [3, 4, 5]]
b = copy.deepcopy(a)

b[2][1] = 100
print(a)  #
print(b)  #
print(f'a[2]와 b[2]가 같은 객체인가? {a[2] is b[2]}')  #

# 복잡한 중첩 객체 예시
print('\n복잡한 중첩 객체 깊은 복사')
original = {
    'a': [1, 2, 3],
    'b': {
        'c': 4,
        'd': [5, 6],
    },
}
copied = copy.deepcopy(original)

copied['a'][1] = 100
copied['b']['d'][0] = 500

print(f'원본: {original}')  #
print(f'복사본: {copied}')  #
print(
    f'original["b"]와 copied["b"]가 같은 객체인가? {original["b"] is copied["b"]}'
)  #
