# persegi , segitiga, jajargenjang

class LuasKeliling:
    def __init__(self, isLuas, data):
        self.isLuas = isLuas
        self.data = data

    # persegi
    def r0(self):
        try:
            if self.isLuas == True:
                result = self.data['side'] * self.data['side']
            else:
                result = self.data['side'] * 4
        except:
            return 'invalid data'
        return result
    
    # segitiga 
    def r1(self):
        try:
            if self.isLuas == True:
                result = 0.5 * self.data['bottom'] * self.data['height']
            else:
                result = self.data['side1'] + self.data['side2'] + self.data['side3']
        except:
            return 'invalid data'
        return result
    
    # jajargenjang 
    def r2(self):
        try:
            if self.isLuas == True:
                result = self.data['bottom'] * self.data['height']
            else:
                result = (self.data['bottom'] + self.data['height']) * 2
        except:
            return 'invalid data'
        return result

r = LuasKeliling(False, {'side1': 5, 'side2': 23, 'side3': 4})
funct = 'print(str(r.r1()))'
eval(funct)