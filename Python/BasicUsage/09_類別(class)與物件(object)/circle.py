
class Circle:
    _radius = 0
    PI = 3.1415926

    def __init__(self, radius):
        self._radius = radius

    def get_area(self):
        return self.PI * (self._radius ** 2)
    
    def get_circumference(self):
        return 2 * self.PI * self._radius

    @staticmethod
    def calc_area(radius):
        return Circle.PI * (radius ** 2)
    
    @staticmethod
    def calc_circumference(radius):
        return 2 * Circle.PI * radius
