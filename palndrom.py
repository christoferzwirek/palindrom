# -*- coding: utf-8 -*-
'''
Czy dany wyraz jest palindrom?
'''


def czypal(wyraz):
    rev=''.join(reversed(wyraz))
    if (wyraz==rev):
        return True
    return False
    

wyraz=input("Poadj wyraz ")
print(czypal(wyraz))
