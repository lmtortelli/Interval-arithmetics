
# Python
# RDM-IA implementation
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
        print ("return RDM(1)")
    
    @staticmethod
    def zero():
        print ("return RDM(0)")

    @staticmethod
    def number(x,y=None):
        if y is None:
            print "return RDM(x)"
        else:
            print "return RDM(x,y)"



rdmia = RDMIA()
rdmia.zero()