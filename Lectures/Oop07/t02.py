class Polynom:

    def __init__(self, coefs_dict):
        self.coefs: dict = coefs_dict

    def __str__(self):
        sorted_coef = list(self.coefs.keys())
        sorted_coef.sort()
        res = ""
        for i in sorted_coef:
            res += f"{self.coefs[i]}*x^{i} + "
        return res

    # def value(self, x):
    def __call__(self, x):
        res = 0
        for i, ai in self.coefs.items():
            res += ai * x**i
        return res

if __name__ == '__main__':
    p = Polynom({
        1: 1,
        0: 1,
        2: 1
    })
    print(p)

    x = 2
    # px = p.value(x)
    px = p(x) #     px = p.__call__(x)

    print(px)