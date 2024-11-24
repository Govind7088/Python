# Create a class c2dvec and use it to another class c3dvec.

class C2dVec:
  def __init__(self,i,j):
    self.i=i
    self.j=j
  
  def __str__(self) -> str:
    return f"{self.i}i + {self.j}j"
  
class C3dVec(C2dVec):
  def __init__(self, i, j,k):
    super().__init__(i, j,)
    self.k=k

  def __str__(self) -> str:
    return f"{self.i}i + {self.j}j + {self.k}k"

v2d=C2dVec(1,3)
v3d=C3dVec(1,8,6)
print(v2d)
print(v3d)