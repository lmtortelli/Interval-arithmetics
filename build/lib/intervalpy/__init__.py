# __init__.py
#
# Copyright 2008 Rafael Menezes Barreto <rmb3@cin.ufpe.br,
# lmtortelli@gmail.com>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License version 2
# as published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA 02110-1301, USA.


"""Interval Arithmetic package

This package provides types and functions for Maximum Accuracy Interval
Arithmetic.

The Interval Arithmetic is a mathematical tool for the solution of problems
related to numerical errors, based on an algebraic system formed by all closed
intervals of Real Line (or rectangles of Complex Plane) and operations defined
on it. Rather than usual numerical algorithms, it's used interval algorithms
producing intervals containing the correct answer as a result.

The Maximum Accuracy, on the other hand, provides an axiomatic method for
arithmetic operations performed in computers that capture essential properties
associated with rounding.

For more information about it, see:

[1] Moore, R. E., Interval Analysis. Prentice-Hall, Englewood Cliffs, New
    Jersey, 1966.
[2] Moore, R. E., Methods and Applications of Interval Analysis. SIAM Studies
    in Applied Mathematics, Philadelphia, 1979.
[3] Kulisch, U. W., Miranker, W. L., Computer Arithmetic in Theory and
    Practice. Academic Press, 1981.

Currently only Real Intervals are available. No Complex Intervals, no Interval
Vectors and Matrixes, and no extensions of basic functions. These will be our
next work.

It was developed in PPGC/UFPel (Brazil) by Lucas Mendes Tortelli
<rmb3@cin.ufpe.br, rafaelbarreto87@gmail.com> and it's free software.
"""

from intervalpy.kaucher import *
from intervalpy.core import *
from intervalpy.rdmia import *


def _test():
    from doctest import DocTestSuite
    from inspect import getmodule
    from os import walk
    from os.path import abspath, dirname, join
    from unittest import TestSuite, TextTestRunner
    test_suite = TestSuite()
    for root, dirs, files in walk(dirname(abspath(__file__))):
        module_files = [join(root, file) for file in files if \
            file.endswith(".py")]
        test_suite.addTests(DocTestSuite(getmodule(None, file)) for file in \
            module_files)
    TextTestRunner().run(test_suite)


if __name__ == "__main__":
    _test()
