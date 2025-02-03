############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 파이썬 내장 함수 min 함수를 사용하지 않습니다.
def min_score(scores):
    
    # 여기에 코드를 작성하여 함수를 완성합니다.
    # if not scores:
    #     return None
    min_value = scores[0]

    for score in scores:
        if score < min_value:
            min_value=score
    return min_value    

def max_score(scores):
    max_value = scores[0]

    for score in scores:
        if score>max_value:
            max_value=score
    return max_value

def len_score(scores):
    count=0
    for _ in scores:
        count+=1
    return count

def sum_score(scores):
    total=0
    for score in scores:
        total+=score
    return total

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(min_score([30, 60, 90, 70])) # 30
print(min_score([0, 10, 20, 30, 40, 50])) # 0
print(min_score([50, 70, 50, 45, 80, 80])) # 45
#####################################################

# 테스트 코드는 이곳에
print(min_score([100, 100]))  

print(max_score([30, 60, 90, 70])) # 30
print(max_score([0, 10, 20, 30, 40, 50])) # 0
print(max_score([50, 70, 50, 45, 80, 80])) # 45

print(len_score([30, 60, 90, 70])) # 30
print(len_score([0, 10, 20, 30, 40, 50])) # 0
print(len_score([50, 70, 50, 45, 80, 80])) # 45

print(sum_score([30, 60, 90, 70])) # 30
print(sum_score([0, 10, 20, 30, 40, 50])) # 0
print(sum_score([50, 70, 50, 45, 80, 80])) # 45