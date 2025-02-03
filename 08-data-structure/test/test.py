#알파벳인지 아닌지 확인(대문자인지 소문자인지)

#1.메서드
#2.유니코드 (아스키코드)

# A 유니(아스키)코드, a 유니(아스키)코드
#A는 65 a는 97

# chr1='B'
# chr2='b'
# print(ord(chr2))
# print(chr(ord(chr1) +32)) #문자를 숫자로 바꾸는게 ord, 다시 문자로 chr 
# #32를 더하면 대문자를 소문자로 변경가능,반대로 -32해도 소문자를 대문자로 

a = 'hello'

print(a.find('b'))
#print(a.index('b'))

# try:
#     print(a.index('b'))
# except:
#     print('찾지못함')

# if 'b' in a:
#     print(a.index('b'))
# else:
#     print('찾지못함')

# arr = ['a','b','c']

# #리스트를 문자열로 출력할 때 2가지 방법
# # 1.join 메서드
# # 2.언패킹 연산자

# print(' '.join(arr))
# print(*arr)

#append와 extend의 차이

#append는 요소(항목)를 추가할때
#extend는 iterable을 추가할때

#a=[1,2,3]
#나는 4를 추가할거야 append
#나는 [4,5,6]을 추가할거야 extend

#pop(): 마지막 요소를 제거하고 반환

#sort와 sorted의 차이??
# 원본을 유지하고 싶은 경우 즉 차이점은 반환값이 있는지 없는지 

#원본 바뀜
#arr=[4,1,3,2]
#arr.sort()

#원본 유지
# arr[4,1,3,2]
# arr2=sorted(arr)
# print(arr2) 

#얕은복사 복사본이 변경되면 원본이 변경
#깊은복사:복사본이 변경돼도 원본이 변경x 

#얕은 복사
# arr1 = [1,2,3,[4,5,6]]
# arr2 = arr1[:]
# arr3 = arr1.copy()

# arr2[0] =7
# print(arr1)
# print(arr2)

# arr2[3][0]=8
# print(arr1)
# print(arr2)