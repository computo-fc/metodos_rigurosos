# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 10:39:30 2013

@author: Ayano
"""

from intervalo_adriano import Intervalo
def test_sub():
    a=Intervalo(-11,4)
    b=Intervalo(2,10)
    c=a-b
    assert c.min==-21 and c.max==2