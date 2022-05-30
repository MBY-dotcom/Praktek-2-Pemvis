# tabung, balok, prisma

class Volume:
    def __init__(self, data):
        self.data = data

    # tabung 
    def v0(self):
        try:
            result = 3.14 * self.data['spoke']
            return result
        except:
            return 'invalid data parameter'

    # balok 
    def v1(self):
        try:
            result = self.data['long'] * self.data['width'] * self.data['height']
            return result
        except:
            return 'invalid data parameter'

    # prisma 
    def v2(self):
        try:
            result = 1.5 * self.data['bottom'] * self.data['height']
            return result
        except:
            return 'invalid data parameter'

volumePrisma = Volume({'bottom': 57, 'height': 88})
print(str(volumePrisma.v2()))