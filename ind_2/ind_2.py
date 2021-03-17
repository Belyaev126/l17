class Fraction:

    def __init__(self, whole='0', fractional='0'):
        whole = int(whole)
        fractional = int(fractional)

        self.__whole = abs(whole)
        self.__fractional = abs(fractional)

    @property
    def whole(self):
        return self.__whole

    @property
    def fractional(self):
        return self.__fractional

    def read(self, prompt=None):
        line = input() if prompt is None else input(prompt)
        parts = list(map(int, line.split('/', maxsplit=1)))

        if parts[1] == 0:
            raise ValueError()

        self.__whole = abs(parts[0])
        self.__fractional = abs(parts[1])

    def display(self):
        print(f"{self.__whole}/{self.__fractional}")

    def __add__(self, rhs):
        if isinstance(rhs, Fraction):
            whole = self.whole * rhs.fractional + \
                    self.fractional * rhs.whole
            fractional = self.fractional * rhs.fractional

            return Fraction(whole, fractional)
        else:
            raise ValueError()

    def __sub__(self, rhs):
        if isinstance(rhs, Fraction):
            whole = self.whole * rhs.fractional - \
                    self.fractional * rhs.whole
            fractional = self.fractional * rhs.fractional

            return Fraction(whole, fractional)
        else:
            raise ValueError()

    def __mul__(self, rhs):
        if isinstance(rhs, Fraction):
            whole = self.whole * rhs.whole
            fractional = self.fractional * rhs.fractional

            return Fraction(whole, fractional)
        else:
            raise ValueError()

    def equals(self, rhs):
        if isinstance(rhs, Fraction):
            return (self.whole == rhs.whole) and \
                   (self.fractional == rhs.fractional)
        else:
            return False

    def greater(self, rhs):
        if isinstance(rhs, Fraction):
            v1 = self.whole / self.__fractional
            v2 = rhs.whole / rhs.fractional

            return v1 > v2
        else:
            return False

    def less(self, rhs):
        if isinstance(rhs, Fraction):
            v1 = self.whole / self.__fractional
            v2 = rhs.whole / rhs.fractional

            return v1 < v2
        else:
            return False

    def __lt__(self, rhs):
        return (self.__whole, self.__fractional) < (rhs.whole, rhs.fractional)

    def __eq__(self, rhs):
        return (self.__whole, self.__fractional) == (rhs.whole, rhs.fractional)

    def __ne__(self, rhs):
        return (self.__whole, self.__fractional) != (rhs.whole, rhs.fractional)

    def __gt__(self, rhs):
        return (self.__whole, self.__fractional) > (rhs.whole, rhs.fractional)

    def __ge__(self, rhs):
        return (self.__whole, self.__fractional) >= (rhs.whole, rhs.fractional)

    def __le__(self, rhs):
        return (self.__whole, self.__fractional) <= (rhs.whole, rhs.fractional)

    def __truediv__(self, rhs):
        if (self.__whole, self.__fractional) >= (rhs.whole, rhs.fractional):
            return (self.__whole, self.__fractional) / (rhs.whole, rhs.fractional)
        else:
            return (rhs.whole, rhs.fractional) / (self.__whole, self.__fractional)

