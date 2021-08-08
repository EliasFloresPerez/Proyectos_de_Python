class A:
    def primer(self):
        print("A")

class B(A):
    def segundo(self):
        print("B")
class C(B):
    def tercer(slef):
        print("C")
class D(C):
    def tercer(self):
        print("D")
        super().tercer()

C().primer()
C().segundo()
C().tercer()
D().tercer()