class Circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius


c1 = Circle(5)
c2 = Circle(10)

print(c1.radius)  # 5
print(c2.radius)  # 10

# c1의 인스턴스 변수 pi를 생성
c1.pi=100

print(c1.pi)  #100
print(Circle.pi)  # 3.14 # 먼저 인스턴스는 자기 자신에게찾음
                 # 없으면 클래스 영역으로감
                 #그래서 c1과 (c2,circle)값이 다름거임
# c2는 인스턴스 변수 pi가 없으므로 클래스 변수 pi를 참조
print(c2.pi)  #
