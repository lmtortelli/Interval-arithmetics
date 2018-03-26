
# Python
# Rdm-IA implementation
# Dirceu Maraschin
# Lucas Tortelli

class Rdmia(object):

    # Default accuracy
    _precision = 0.01

    @property
    def precision(self):
        return type(self)._precision

    @staticmethod
    def setDotPrecision(val):
       _precision = 10.0/(10.0**val)

    @staticmethod
    def one():
        print ("return Rdm(1)")
    
    @staticmethod
    def zero():
        print ("return Rdm(0)")

    @staticmethod
    def number(x,y=None):
        if y is None:
            print "return Rdm(x)"
        else:
            print "return Rdm(x,y)"



rdmia = Rdmia()
rdmia.zero()