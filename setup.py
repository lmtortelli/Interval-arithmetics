# setup.py
#
# Copyright 2008 Rafael Menezes Barreto <rmb3@cin.ufpe.br,
# rafaelbarreto87@gmail.com>
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


from distutils.core import Extension
from distutils.core import setup


_package_description = """Interval Arithmetic package

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

It was developed in CIn/UFPE (Brazil) by Rafael Menezes Barreto
<rmb3@cin.ufpe.br, rafaelbarreto87@gmail.com> and it's free software.
""".split("\n")


if __name__ == "__main__":
    setup(
        name="intervalpy",
        version="0.1.0",
        description=_package_description[0],
        long_description="\n".join(_package_description[2:-1]),
        author="Aline Brum Loreto, Alice Fonseca Finger, Lucas Mendes Tortelli, Dirceu Maraschin Jr.",
        author_email="aline.loreto@gmail.com, aliceffinger@gmail.com,lmtortelli@gmail.com,dirceu.maraschin@gmail.com",
        license="GPL",
        platforms=[
            "Windows",
            "Linux"
        ],
        packages=[
            "intervalpy",
            "intervalpy.kaucher",
            "intervalpy.core",
            "intervalpy.rdmia"
        ],
        package_dir={
            "intervalpy" : "src"
        },
        install_requires = [
                          'numpy >= 1.13.0',
                          'enum34',
                          ],

    )
