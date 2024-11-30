import math

def check(angles, sides, n_angles):
    if n_angles != 0:
        if n_angles != len(sides):
            print("Недостаточно сторон")
            return False

        if not all(0 < angle < 360 for angle in angles):
            print("Ошибка с углами")
            return False
        if not all(side > 0 for side in sides):
            print("Ошибка со сторонами")
            return False

        cur_sum = sum(angles)
        real_sum = (n_angles - 2) * 180
        if cur_sum != real_sum:
            print ("Сумма углов не соответсвует")
            return False

        for i in range(n_angles):
            if sides[i] <= 0:
                return False
            if i > 0 and (sides[i - 1] + sides[i] <= sides[(i + 1) % n_angles]):
                return False


    return True

class Shapes:
    def __init__(self, n_angles, angles, sides):
        if not check(angles, sides, n_angles):
            raise ValueError("Ошибка в образовании фигуры.")

        self.n_angles = n_angles
        self.angles = angles
        self.sides = sides

    def get_perimeter(self):
        if self.n_angles != 0:
            return sum(self.sides)
        else:
            return  round(2 * math.pi * self.sides[0], 2)

    def get_info(self):
        print('Количество углов:', self.n_angles)
        print('Значение углов:', self.angles)
        print('Стороны:', self.sides)
        print('Периметр:', self.get_perimeter())

    def set_sides(self, new_sides):
        for i in range(self.n_angles):
            self.sides[i] = new_sides[i]

    def set_angles(self, new_angles):
        for i in range(self.n_angles):
            self.angles[i] = new_angles[i]



class Circle(Shapes):
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Ошибка с радиусом")
        super().__init__(0, [], [radius])
        self.name = "Круг"
        self.radius = radius

    def get_sq(self):
        return  round(math.pi * (self.radius ** 2), 2)

    def get_info(self):
        print("Название:", self.name)
        print("Радиус:", self.radius)
        print("Длина окружности:", self.get_perimeter())
        print("Площадь:", self.get_sq())



class Triangle(Shapes):
    def __init__(self, angles, sides):
        summa = 0
        flag = 0
        for i in range(3):
            if str(angles[i]) == '-':
                ind = i
                flag = 1
            else:
                summa += angles[i]
        if flag == 1:
            a = 180 - summa
            angles[ind] = a
        if len(angles) < 3:
            raise ValueError("Ошибка в образовании фигуры.")
        super().__init__(3, angles, sides)
        self.name = "Треугольник"

    def get_sq(self):
        p = self.get_perimeter() / 2
        area1 =  round(math.sqrt(p * (p - self.sides[0]) * (p - self.sides[1]) * (p - self.sides[2])), 2)
        area2 =  round(0.5 * self.sides[0] * self.sides[1] * math.sin(math.radians(self.angles[1])), 2)
        h = self.sides[0] *  math.sin(math.radians(self.angles[0]))
        area3 =  round(0.5 * h * self.sides[2], 2)
        if (area1 == area2) and (area2 == area3):
            print("Площади:\nПо Герону: ", area1, "\nЧерез 2 стороны и углу между ними: ", area2,
                  "\nЧерез высоту: ", area3)
            return area1
        else:
            print("Площади (не совпали):\nПо Герону:", area1, "\nЧерез 2 стороны и углу между ними:", area2, "\nЧерез высоту:", area3)
            return area1

    def get_info(self):
        print("Название: ", self.name)
        super().get_info()
        self.get_sq()



class Quadrangle(Shapes):
    def __init__(self, angles, sides):
        summa = 0
        flag = 0
        for i in range(4):
            if str(angles[i]) == '-':
                ind = i
                flag = 1
            else:
                summa += angles[i]
        if flag != 0:
            a = 360 - summa
            angles[ind] = a
        if len(angles) < 4:
            raise ValueError("Ошибка в образовании фигуры.")

        super().__init__(4, angles, sides)
        if self.angles[0] + self.angles[1] == 180:
            if self.angles[1] + self.angles[2] == 180: #Параллелограмм
                if (self.sides[0] == self.sides[1]) and (self.sides[2] == self.sides[1]):#Ромб
                    if all(angle == 90 for angle in angles):
                        if self.sides[0] == self.sides[1]:
                            self.name = "Квадрат"
                    else:
                        self.name = "Ромб"
                elif all(angle == 90 for angle in angles) and (self.sides[0] != self.sides[1]):
                    self.name = "Прямоугольник"
                else:
                    self.name = "Параллелограмм"
            else:
                self.name = "Трепеция"
        else:
            self.name = "Четырехугольник"


    def get_sq(self):
        if self.name == "Квадрат" or self.name == "Прямоугольник" or self.name == "Ромб" or self.name == "Параллелограмм":
            return round(self.sides[0] * self.sides[1] * math.sin(math.radians(self.angles[1])), 2)
        elif self.name == "Трепеция":
            h = self.sides[0] * math.sin(math.radians(self.angles[0]))
            if self.angles[0] + self.angles[1] == 180:
                a = self.sides[1]
                b = self.sides[3]
            else:
                a = self.sides[0]
                b = self.sides[2]
            return round(0.5 * h * (a+b), 2)
        else:
            p = self.get_perimeter()*0.5
            #d1 = math.sqrt(self.sides[0]**2 + self.sides[3]**2 - 2*self.sides[0]*self.sides[3]*math.cos(math.radians(self.angles[0])))
            #d2 = math.sqrt(self.sides[0] ** 2 + self.sides[1] ** 2 - 2 * self.sides[0] * self.sides[1] * math.cos(math.radians(self.angles[1])))
            return round(math.sqrt(p*(p-self.sides[0])*(p-self.sides[1])*(p-self.sides[2])*(p-self.sides[3])), 2)

    def get_info(self):
        print("Название: ", self.name)
        super().get_info()
        print("Площадь:", self.get_sq())

class Nangle(Shapes):
    def __init__(self, n_angles, angles, sides):
        summa = 0
        flag = 0
        for i in range(n_angles):
            if str(angles[i]) == '-':
                ind = i
                flag = 1
            else:
                summa += angles[i]
        if flag == 1:
            a = (n_angles - 2) * 180 - summa
            angles[ind] = a
        if len(angles) < n_angles - 1:
            raise ValueError("Ошибка в образовании фигуры.")
        super().__init__(n_angles, angles, sides)
        s = str(n_angles)
        self.name = s + "-угольник"
    def get_info(self):
        print("Название: ", self.name)
        super().get_info()


try:
    cir1 = Circle(10)
    cir1.get_info()
except ValueError:
    print("Ошибка\n")

try:
    tri = Triangle([60, '-', 60], [10, 10, 10])
    tri.get_info()
    tri.set_sides([30,30,30])
    tri.get_info()
except ValueError:
    print("Ошибка\n")

try:
    squ = Quadrangle([60, 120, 60, 120], [10, 10, 10, 10])
    squ.get_info()
except ValueError:
    print("Ошибка\n")

try:
    n = Nangle(6, [120, 120, 120, 120, 120,120], [10, 10, 10, 10, 10, 10])
    n.get_info()
except ValueError:
    print("Ошибка\n")