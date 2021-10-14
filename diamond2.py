class A:
    def hi(self):
        print("A")

class B:
    def hi(self):
        print("B")

class C:
    def hi(self):
        print("C")
    
class D:
    def hi(self):
        print("D")

class E(A, B):
    def hi(self):
        super().hi()
        print("E")

class F(B, C):
    def hi(self):
        super().hi()
        print("F")

class G(E):
    def hi(self):
        super().hi()
        print("G")

class H(E):
    def hi(self):
        super().hi()
        print("H")

class I(G, H):
    def hi(self):
        super().hi()
        print("I")

class J(I, F, D):
    def hi(self):
        super().hi()
        print("J")

J().hi()
print(J.mro())
