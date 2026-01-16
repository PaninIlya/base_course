class ClassVector:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    

    def __len__(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5
    
    def __str__(self):
        print(f'Вектор с координатами X :{self.x}; Y: {self.y}; Z:{self.z}')
    
    def __repr__(self):
        return f'ClassVector(x={self.x}, y={self.y}, z={self.z})'
    
    def __add__(self, other):
         return ClassVector(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z
        )

    def __sub__(self, other):
            return ClassVector(
            self.x - other.x,
            self.y - other.y,
            self.z - other.z
        )              

    def __mul__(self, other):
         
             return ClassVector(
                self.x * other,
                self.y * other,
                self.z * other
            )
    
    def __radd__(self, other):
         return ClassVector(
            other.x + self.x,
            other.y + self.y,
            other.z + self.z
        )

    def __rsub__(self, other):
         return ClassVector(
            other.x - self.x,
            other.y - self.y,
            other.z - self.z
        )       
        
    def __rmul__(self, other):
         return ClassVector(
            other.x * self.x,
            other.y * self.y,
            other.z * self.z
        )
    
    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        self.z += other.z
        return self
    
    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        self.z -= other.z
        return self
    
    def __imul__(self, other):
        self.x *= other.x
        self.y *= other.y
        self.z *= other.z
        return self
           
            