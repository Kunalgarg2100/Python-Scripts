
#!/usr/bin/python3
import unittest
class Matrix:
    '''Class for matrix operations'''
    def __init__(self, lofl, m, n):
        assert len(lofl) == m
        for row in lofl:
            assert len(row) == n
        self.lofl = lofl
        self.m = m
        self.n = n

    def __add__(self, mat):
        m3 = []
        for row in range(0, self.m):
            m3.append([])
        assert self.m == mat.m
        assert self.n == mat.n
        m1  = self.lofl
        m2 = mat.lofl
        for row in range(0,self.m):
            for column in range(0,self.n):
                    m3[row].append(m1[row][column] + m2[row][column])
        return Matrix(m3,mat.m,mat.n)

    def __sub__(self, mat):
        assert self.m == mat.m
        assert self.n == mat.n
        m3  =[]
        for row in range(0,self.m):
            m3.append([])
        m1 = self.lofl
        m2 = mat.lofl
        for row in range(0, self.m):
            for column in range(0, self.n):
                m3[row].append(m1[row][column] - m2[row][column])
        return Matrix(m3, mat.m, mat.n)

    def __mul__(self, mat):
        m3 = []
        for row in range(0, self.m):
            m3.append([])
        assert self.n == mat.m
        m1 = self.lofl
        m2 = mat.lofl
        for row in range(0, self.m):
            for column in range(0, mat.n):
                calculate = 0;
                for k in range(0,mat.m):
                    calculate += m1[row][k] * m2[k][column]
                m3[row].append(calculate)
        return Matrix(m3, self.m, mat.n)

    def __str__(self):
        stri = ''
        for i, row in enumerate(self.lofl):
            for j, elem in enumerate(row):
                stri += str(elem) + ' '
            stri += '\n'
        return stri

    def __iter__(self):
        assert self.m == self.m
        assert self.n == self.n
        self.it = -1
        return self

    def __next__(self):
        m1 = self.lofl
        k = []
        for row in range(0, self.m):
            for column in range(0, self.n):
                k.append(m1[row][column])

        numi = self.m * self.n-1
        if self.it < numi:
            self.it+=1
            return k[self.it]
        else:
            raise StopIteration

class MatrixTest(unittest.TestCase):
    def test_add1(self):
        m1 = Matrix([[1, 2], [3, 4]], 2, 2)
        m2 = Matrix([[5, 6], [7, 8]], 2, 2)
        self.assertEqual(str(m1 + m2), str(Matrix([[6, 8], [10, 12]], 2, 2)))

    def test_add2(self):
        m1 = Matrix([[1, 2, 3], [3, 4, 5]], 2, 3)
        m2 = Matrix([[5, 6], [7, 8]], 2, 2)
        with self.assertRaises(AssertionError):
            m1 + m2

    def test_sub1(self):
        m1 = Matrix([[1, 2], [3, 4]], 2, 2)
        m2 = Matrix([[5, 6], [7, 8]], 2, 2)
        self.assertEqual(str(m1 - m2), str(Matrix([[-4, -4], [-4, -4]], 2, 2)))

    def test_mul1(self):
        m1 = Matrix([[1, 2], [3, 4], [8, 9]], 3, 2)
        m2 = Matrix([[5, 6, 7], [7, 8, 3]], 2, 3)
        self.assertEqual(str(m1 * m2), str(Matrix([[19, 22, 13],[43, 50, 33],[103, 120, 83]], 3, 3)))

    def test_mul2(self):
        m1 = Matrix([[5, 6, 7], [7, 8, 3]], 2, 3)
        m2 = Matrix([[1, 2], [3, 4]], 2, 2)
        with self.assertRaises(AssertionError):
            m1 * m2

    def test_it1(self):
        m1 = Matrix([[1, 2], [3, 4]], 2, 2)
        self.assertEqual(list(m1), [1, 2, 3, 4])

    def test_it2(self):
        m1 = Matrix([[5, 6, 7], [7, 8, 3]], 2, 3)
        self.assertEqual(list(m1), [5, 6, 7, 7, 8, 3])
if __name__ == "__main__":
    unittest.main()
