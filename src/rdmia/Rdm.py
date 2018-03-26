from Rdmia import Rdmia as rdm
import numpy as np
import sys

class Rdm(object):
    _lower = 0.0
    _upper = 0.0
    _alpha = 0.0
    f = None


    def __init__(self,x,y=None):
        self._alpha = 0.01
        self._lower = np.float64(x)
        self._upper = np.float64(x) if y is None  else np.float64(y)
        self._f = lambda alpha: self._lower + alpha*(self._upper - self._lower) 


    def __checkValue(self,other):
        if(type(other) is not Rdm):
            other = Rdm(other)
        return other

    def __str__(self):
        return "["+str(self._lower)+" , "+str(self._upper)+"]"

    def __repr__(self):
        return "[%r, %r]" % (self._lower, self._upper)

    def __getitem__(self):
        return np.array([self._lower,self._upper])

    def __add__(self,other):
        other = self.__checkValue(other)
        values = []
        rupper = 1+self._alpha
        for alpha_self in np.arange(0,rupper,self._alpha):
            for alpha_other in np.arange(0,rupper,self._alpha):
                values.append(self._f(alpha_self) + other._f(alpha_other))
        
        return Rdm(min(values),max(values))

    def __sub__(self,other):
        other = self.__checkValue(other)
        values = []
        rupper = 1+self._alpha
        for alpha_self in np.arange(0,rupper,self._alpha):
            for alpha_other in np.arange(0,rupper,self._alpha):
                values.append(self._f(alpha_self) - other._f(alpha_other))
        
        return Rdm(min(values),max(values))

    def __mul__(self,other):
        other = self.__checkValue(other)
        values = []
        rupper = 1+self._alpha
        for alpha_self in np.arange(0,rupper,self._alpha):
            for alpha_other in np.arange(0,rupper,self._alpha):
                values.append(self._f(alpha_self) * other._f(alpha_other))
        
        return Rdm(min(values),max(values))

    def __div__(self,other):
        other = self.__checkValue(other)
        
        values = []
        rupper = 1+self._alpha
        for alpha_self in np.arange(0,rupper,self._alpha):
            for alpha_other in np.arange(0,rupper,self._alpha):
                values.append(self._f(alpha_self) / other._f(alpha_other))
        
        return Rdm(min(values),max(values))

    def __rdiv__(self,other):
        other = self.__checkValue(other)
        
        values = []
        rupper = 1+self._alpha
        for alpha_self in np.arange(0,rupper,self._alpha):
            for alpha_other in np.arange(0,rupper,self._alpha):
                values.append(other._f(alpha_other) / self._f(alpha_self))
        
        return Rdm(min(values),max(values))

    def __rsub__(self,other):
        other = self.__checkValue(other)
        
        values = []
        rupper = 1+self._alpha
        for alpha_self in np.arange(0,rupper,self._alpha):
            for alpha_other in np.arange(0,rupper,self._alpha):
                values.append(other._f(alpha_other) - self._f(alpha_self))
        
        return Rdm(min(values),max(values))

    def __radd__(self,other):
        other = self.__checkValue(other)
        
        values = []
        rupper = 1+self._alpha
        for alpha_self in np.arange(0,rupper,self._alpha):
            for alpha_other in np.arange(0,rupper,self._alpha):
                values.append(other._f(alpha_other) + self._f(alpha_self))
        
        return Rdm(min(values),max(values))

    def __rmul__(self,other):
        other = self.__checkValue(other)
        
        values = []
        rupper = 1+self._alpha
        for alpha_self in np.arange(0,rupper,self._alpha):
            for alpha_other in np.arange(0,rupper,self._alpha):
                values.append(other._f(alpha_other) * self._f(alpha_self))
        
        return Rdm(min(values),max(values))

   



print 1 /  Rdm(3,4)
print 3 * Rdm(3,4)
print 5 + Rdm(3,4)