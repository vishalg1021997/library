class A:
    def __init__(self):
        print('inside A')
        super().__init__()

    def eat(self):
        print('A is eating')
        super().eat()


class B:
    def __init__(self):
        print('inside B')
        super().__init__()

    def eat(self):
        print('B is eating')
        super().eat()


class C:
    def __init__(self):
        print('inside C')

    def eat(self):
        print('C is eating')


class X(B, A, C):
    def __init__(self):
        print('inside X')
        super().__init__()

    def eat(self):
        print('X is eating')
        super().eat()

obj = X()