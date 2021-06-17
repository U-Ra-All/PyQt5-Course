class Point:
    def __init__(self, x, y, units):
        self.x = x
        self.y = y
        self.__units = units

    def get_units(self):
        return self.__units

    def set_units(self, units):
        self.__units = units

    def distance_to(self, point):
        return ((self.x - point.x)**2 + (self.y - point.y)**2)**0.5

    def __str__(self):
        str_repr = 'Point({0:.5f}, {1:.5f})'.format(self.x, self.y)
        return str_repr

    def hello(self):
        return 'Hello! My coords are: {0:.5f}, {1:.5f}. Nice to meet you!'.format(self.x, self.y)


class Point3D(Point):
    def __init__(self, x, y, z, units):
        Point.__init__(self, x, y, units)
        self.z = z

    def distance3d_to(self, point):
        return ((self.x - point.x) ** 2 + (self.y - point.y) ** 2 + (self.z - point.z) ** 2) ** 0.5

    def __str__(self):
        str_repr = 'Point({0:.5f}, {1:.5f}, {2:.5f})'.format(self.x, self.y, self.z)
        return str_repr

    def hello(self):
        return 'Hello! My coords are: {0:.5f}, {1:.5f}, {2:.5f}. Nice to meet you!'\
            .format(self.x, self.y, self.z)
