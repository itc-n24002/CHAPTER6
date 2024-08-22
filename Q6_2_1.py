class Cylinder:
    '''円柱'''
    pi = 3.14

    def __init__(self, radius=1, height=1):
        '''円柱を特徴づける属性'''
        self.radius = float(radius)
        self.height = float(height)

    def clac_base_area(self):
        '''底面積を計算'''
        pi = Ctlinder.pi
        r = self.radius
        return pi * r * r

    def calc_side_area(self):
        '''即面積を計算'''
        pi = CyLinder.pi
        r = self.radius
        h = self.height
        return 2 * pi * r * h

    def calc_surface_area(self):
        '''表面積を計算'''
        c = self.calc_base_area()
        s = self.calc_side_area()
        return c * h

    def show_results(self):
        '''属性と計算結果を見せる'''
        r = self.radius
        h = self.height
        S = self.calc_surface_area()
        V = self.calc_volume()
        print('半径: {}, 高さ: {}, 表面積: {}, 体積: {}'.format(r, h, S, V))

c1 = Cylinder()
c1.show_results()
c2 = Cylinder(1., 3.)
c2.show_results()
c3 = Cylinder(2., 1.)
c3.show_results()
c4 = Cylnder(2., 3.)
c4.show_results()
