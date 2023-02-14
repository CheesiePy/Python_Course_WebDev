# point class
class Point:
    def __init__(self, x, y): # for ClassName()
        self.x = x
        self.y = y
    
    def __str__(self): # for print()
        return f"({self.x}, {self.y})"
    
    def __eq__(self, other): # for ==
        return self.x == other.x and self.y == other.y
    
    def __add__(self, other): # for +
        return Point(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other): # for -
        return Point(self.x - other.x, self.y - other.y)
    
    def __mul__(self, other): # for *
        return Point(self.x * other.x, self.y * other.y)
    
    def __truediv__(self, other): # for /
        return Point(self.x / other.x, self.y / other.y)
    
    def __floordiv__(self, other): # for //
        return Point(self.x // other.x, self.y // other.y)
    
    def __mod__(self, other): # for %
        return Point(self.x % other.x, self.y % other.y)    
    
    def __pow__(self, other): # for **
        return Point(self.x ** other.x, self.y ** other.y)
    
    def __lt__(self, other): # for <
        return self.x < other.x and self.y < other.y
    
    def __le__(self, other): # for <=
        return self.x <= other.x and self.y <= other.y
    
    def __gt__(self, other): # for >
        return self.x > other.x and self.y > other.y
    
    def __ge__(self, other): # for >=
        return self.x >= other.x and self.y >= other.y
    
    def __ne__(self, other): # for !=
        return self.x != other.x and self.y != other.y
    
    def __neg__(self): # for -
        return Point(-self.x, -self.y)

#   def __pos__(self):  # not needed
#       return Point(self.x, self.y)    

    def __abs__(self): # for abs()
        return Point(abs(self.x), abs(self.y))
    
    def __round__(self, n): # for round()
        return Point(round(self.x, n), round(self.y, n))

    def __len__(self): # for len()
        return 2
    
    def __getitem__(self, index): # for []
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError("Index out of range")
        
    def __setitem__(self, index, value): # for [] = 
        if index == 0:
            self.x = value
        elif index == 1:
            self.y = value
        else:
            raise IndexError("Index out of range") 
    
    def __iter__(self): # for iteration (for loop)
        yield self.x
        yield self.y
    
    def __contains__(self, item): # for in
        return item in (self.x, self.y)


    