import sys

class BitField:
    def __init__(self, field):
        n = field.find(':')
        self.msb = False

        if (n < 0):
            self.start = int(field)
            self.end   = self.start
        else:
            self.start = int(field[:n])
            self.end   = int(field[n+1:])

        if (self.start > self.end):
            temp = self.start
            self.start = self.end
            self.end = temp
            self.msb = True

        self.mask = 0
        for i in range(self.start, self.end + 1):
            self.mask |= 1 << i

        # print('BitField: start %d, end %d, mask 0x%x' % (self.start, self.end, self.mask))
    def toString(self):
        if (self.start == self.end):
            return 'BIT[%d]' % (self.start)
        else:
            if (self.msb):
                return 'BIT[%d:%d]' % (self.end, self.start)
            else:
                return 'BIT[%d:%d]' % (self.start, self.end)

class BitFields:
    def __init__(self, fields):
        self.fields = []
        bits = fields.split(';')

        for field in bits:
            if (field != ''):
                self.fields.append(BitField(field))

    def dec2bin(self, data, n, msb):
        ret = ''
        for i in range(n):
            if (msb):
                mask = 1 << (n - i)
            else:
                mask = 1 << i
            if (data & mask): 
                ret += '1'
            else:
                ret += '0'
        return ret;

    def results(self, data):
        ret = []
        for field in self.fields:
            ret.append(field.toString() + ':' + self.dec2bin((data & field.mask) >> field.start, field.end - field.start + 1, field.msb))
        return ret
