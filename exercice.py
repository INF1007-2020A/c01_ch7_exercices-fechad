#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
import math


# TODO: Définissez vos fonction ici
def ellipsoïde(a,b,c,masse_volume):
    volume = (4/3)*math.pi*a*b*c
    masse = masse_volume*volume
    answer = (f'volume = {volume}, masse = {masse}') 
    return answer


if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    for i in range(5):
        a, b, c, masse = i, i+1, 2*i, 5*i
        print(ellipsoïde(a,b,c,masse))

    
