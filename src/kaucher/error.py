# Copyright 2015 Aline Brum Loreto<aline.loreto@lower.ufpel.edu.br>, Alice Fonseca Finger <aliceffinger@gmail.com>, Mauricio Dorneles
# Caldeira Balboni<mdcbalboni@lower.ufpel.edu.br>,Lucas Mendes Tortelli <lmtortelli@lower.ufpel.edu.br>, Vinicius Signori Furlan<vsfurlan@.lower.ufpel.edu.br>
#
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

#Calculates Relative Error
def relativeError(xInt,xReal):
    try:
        r = abs((xReal - m(xInt))/xReal)
        error = (diam(xInt))/(2*xInt.lower)
    except:
        r = "NaN"
        error = "NaN"
    return str(r)+" <= "+str(error)

#Calculates interval diameter
def diam(xInt):
    return xInt.upper - xInt.lower

def m(xInt):
    return (xInt.lower + xInt.upper)/2.0

#Calculates absolute error
def absError(xInt,xReal):
    try:
        r = abs((xReal - m(xInt))/xReal)
        error = (diam(xInt)/2)
    except:
        r = "NaN"
        error = "NaN"
    return str(r)+" <= "+str(error)
