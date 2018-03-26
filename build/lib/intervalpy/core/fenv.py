#+
# This Python 3 module gives access to the floating-point environment-control
# functions available in <fenv.h> with C99, along with some other useful
# numerics-related stuff not currently standard in Python.
#
# This code as it currently stands is almost certainly GCC- and x86-specific.
# How to make it more portable while keeping it in pure Python?
#
# Copyright 2016 by Lawrence D'Oliveiro <ldo@geek-central.gen.nz>.
# Licensed under CC-BY-SA <http://creativecommons.org/licenses/by-sa/4.0/>.
#-

import enum
import ctypes as ct

libm = ct.cdll.LoadLibrary("libm.so.6")

class FE :
    # any lower-level definitions from the include files would go here.

    fexcept_t = ct.c_ushort

#end FE

@enum.unique
class EXCEPT(enum.Enum) :
    "the various possible floating-point exceptions."
    # values are bit numbers
    INVALID = 0
    DENORM = 1
    DIVBYZERO = 2
    OVERFLOW = 3
    UNDERFLOW = 4
    INEXACT = 5

    @property
    def mask(self) :
        return \
            1 << self.value
    #end mask

    @classmethod
    def from_mask(celf, mask) :
        "converts a bitmask to a frozenset of EXCEPT.xxx values."
        result = set()
        for e in celf.__members__.values() :
            if e.mask & mask != 0 :
                result.add(e)
            #end if
        #end for
        return \
            frozenset(result)
    #end from_mask

    @classmethod
    def to_mask(celf, flags) :
        "converts a set of EXCEPT.xxx values to a bitmask."
        result = 0
        for e in celf.__members__.values() :
            if e in flags :
                result |= e.mask
            #end if
        #end for
        return \
            result
    #end to_mask

    def clear(self) :
        "clears this exception."
        libm.feclearexcept(self.mask)
    #end clear

    def raises(self) :
        "raises this exception."
        libm.feraiseexcept(self.mask)
    #end raıse

    raiise = raises # if you prefer

    @property
    def test(self) :
        "is this exception currently set."
        return \
            libm.fetestexcept(self.mask) & self.mask != 0
    #end test

#end EXCEPT
EXCEPT_ALL = frozenset \
  (
    e for e in EXCEPT.__members__.values()
  )

@enum.unique
class ROUND(enum.Enum) :
    TONEAREST = 0
    DOWNWARD = 0x400
    UPWARD = 0x800
    TOWARDZERO = 0xc00

    @classmethod
    def get(celf) :
        "returns the current rounding setting as a ROUND.xxx value."
        return \
            celf(libm.fegetround())
    #end get

    def set(self) :
        "sets the current rounding direction to this ROUND.xxx value."
        libm.fesetround(self.value)
    #end set

#end ROUND

# man page says these return nonzero iff error; but what errors could I check for?
libm.feclearexcept.restype = ct.c_int
libm.feclearexcept.argtypes = (ct.c_int,)
libm.fegetexceptflag.restype = ct.c_int
libm.fegetexceptflag.argtypes = (ct.POINTER(FE.fexcept_t), ct.c_int)
libm.feraiseexcept.restype = ct.c_int
libm.feraiseexcept.argtypes = (ct.c_int,)
libm.fesetexceptflag.restype = ct.c_int
libm.fesetexceptflag.argtypes = (ct.POINTER(FE.fexcept_t), ct.c_int)
libm.fetestexcept.restype = ct.c_int
libm.fetestexcept.argtypes = (ct.c_int,)

libm.fegetround.restype = ct.c_int
libm.fegetround.argtypes = ()
libm.fesetround.restype = ct.c_int
libm.fesetround.argtypes = (ct.c_int,)

# TODO: fenv_t functions

libm.feenableexcept.restype =  ct.c_int
libm.feenableexcept.argtypes = (ct.c_int,)
libm.fedisableexcept.restype =  ct.c_int
libm.fedisableexcept.argtypes = (ct.c_int,)
libm.fegetexcept.restype =  ct.c_int
libm.fegetexcept.argtypes = ()

# additional useful stuff

libm.nearbyint.restype = ct.c_double
libm.nearbyint.argtypes = (ct.c_double,)
libm.rint.restype = ct.c_double
libm.rint.argtypes = (ct.c_double,)
libm.nextafter.restype = ct.c_double
libm.nextafter.argtypes = (ct.c_double, ct.c_double)

libm.__fpclassify.restype = ct.c_int
libm.__fpclassify.argtypes = (ct.c_double,)
libm.fpclassify = libm.__fpclassify
  # avoid weird error when trying to call it under its actual name

class ExceptFlag :
    "wrapper for implementation-defined representation of exception flags." \
    " Do not instantiate directly; use the getflag method."

    __slots__ = ("_flags",)

    def __init__(self, _flags) :
        self._flags = _flags
    #end __init__

    @classmethod
    def clear(celf, excepts) :
        "clears the exceptions represented by excepts, which is a set of EXCEPT.xxx values."
        libm.feclearexcept(EXCEPT.to_mask(excepts))
    #end clear

    @classmethod
    def getflag(celf, excepts) :
        "returns the state of the exceptions represented by excepts," \
        " which is a set of EXCEPT.xxx values, as a new ExceptFlag object."
        c_result = FE.fexcept_t()
        libm.fegetexceptflag(ct.byref(c_result), EXCEPT.to_mask(excepts))
        return \
            celf(EXCEPT.from_mask(c_result.value))
    #end getflag

    @classmethod
    def raises(celf, excepts) :
        "raises the exceptions represented by excepts, which is a set of EXCEPT.xxx values."
        libm.feraiseexcept(EXCEPT.to_mask(excepts))
    #end raıse

    def setflag(self, excepts) :
        "sets status for all exceptions represented by excepts, which is a set of" \
        " EXCEPT.xxx values, to those saved in this ExceptFlag instance."
        c_flags = FE.fexcept_t(EXCEPT.to_mask(self._flags))
        libm.fesetexceptflag(ct.byref(c_flags), EXCEPT.to_mask(excepts))
    #end setflag

    @classmethod
    def test(celf, excepts) :
        "returns a set of EXCEPT.xxx values indicating which of the exceptions" \
        " in excepts, which is a set of EXCEPT.xxx values, are currently set."
        return \
            EXCEPT.from_mask(libm.fetestexcept(EXCEPT.to_mask(excepts)))
    #end test

#end ExceptFlag

# TODO: floating-point environment, enable/disable individual exceptions

def nearbyint(x) :
    "rounding which respects current rounding direction, without raising INEXACT."
    return \
        libm.nearbyint(x)
#end nearbyint

def rint(x) :
    "rounding which respects current rounding direction, and which might raise INEXACT."
    return \
        libm.rint(x)
#end rint

def nextafter(x, y) :
    "returns the next representable float from x in the direction of y."
    return \
        libm.nextafter(x, y)
#end nextafter

class SaveRounding :
    "context manager which saves and restores the current rounding setting."

    __slots__ = ("saved_rounding",)

    def __enter__(self) :
        self.saved_rounding = ROUND.get()
        return \
            self
    #end __enter__

    def __exit__(self, exc_type, exc_value, traceback) :
        self.saved_rounding.set()
        return \
            False
    #end __exit__

#end SaveRounding

@enum.unique
class FP(enum.Enum) :
    "classification of numeric values."
    NAN = 0
    INFINITE = 1
    ZERO = 2
    SUBNORMAL = 3
    NORMAL = 4

    @classmethod
    def classify(celf, x) :
        "returns the classification of the real value x."
        return \
            celf(libm.fpclassify(x))
    #end classify

#end FP

def isnormal(x) :
    "is x a normalized float."
    return \
        FP.classify(x) == FP.NORMAL
#end isnormal
