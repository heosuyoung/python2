# packed_values = 1, 2, 3, 4, 5

# # 언패킹
# a, b, c, d, e = packed_values
# print(a, b, c, d, e)  # 1 2 3 4 5


# def my_function(x, y, z):
#     print(x, y, z)


# names = ['alice', 'jane', 'peter']
# my_function(*names)  # alice jane peter


def my_function(a, b, c):
    print(c, b, a)


my_dict = {'a': 1, 'b': 2, 'c': 3}
my_function(**my_dict)  # 1 2 3
