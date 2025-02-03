class Circle:
    #클래스 변수(속성)
    pi=3.14

    #생성자 메서드
    def __init__(self,radius):
        self.radius = radius
        


# 인스턴스 생성
# c1 = Circle() # radius에 값이 안들어가서 오류 뜸
c1=Circle(1)
c2=Circle(5)
# 인스턴스 변수(속성)
print(c1.radius)
print(c2.radius) # c1과 c2는 다른 객체 
# 클래스 변수(속성)
print(c1.pi)
print(c2.pi) #클래스 변수는 모든 인스턴스가 공유함