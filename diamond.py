class A:
    def hi(self):
        print('A')

class B:
    def hi(self) -> None:
        print('B')

class C:
    def hi(self) -> None:
        print('C')

class AB(A, B):
    def hi(self) -> None:
        super().hi()
        print("AB")

class BC(B, C):
    def hi(self) -> None:
        super().hi()
        print("BC")

class ABOne(AB):
    def hi(self) -> None:
        super().hi()
        print("ABOne")

class ABTwo(AB):
    def hi(self) -> None:
        super().hi()
        print("ABTwo")

class ABSum(ABOne, ABTwo):
    def hi(self) -> None:
        super().hi()
        print("ABSum")

class Last(ABSum, BC):
    def hi(self) -> None:
        super().hi()
        print("Last")

last = Last()
last.hi()
print()
print(Last.__mro__)