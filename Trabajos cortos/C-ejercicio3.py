# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 23:23:06 2021

@author: Andrade
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import uic
import math

class Ventana(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        uic.loadUi("Ejercicio3.ui",self)
        self.but.clicked.connect(self.calcular)
        
    
    def calcular(self):
        n1=self.t1.toPlainText()
        n2=self.t2.toPlainText()  
        
        n2=int(n2)
        n1_1=float(n1)
        cortar=0
        cortar2=0
        decimal, entera = math.modf(n1_1)
        if self.rbut.isChecked():
            
            if entera>0 and decimal==0:
                cortar=len(n1)
                cortar2=n2
                errorab=0.5*10**(len(n1)-n2)
            elif entera==0 and decimal>0:
                cortar=len(n1)
                cortar2=2+n2
                errorab=0.5*10**-n2
            elif decimal>0 and entera>0:
                cortar=len(n1)
                cortar2=n2+1
                aux=len(str(entera))-2
                errorab=0.5*10**-(n2-aux)
        
        elif self.rbut2.isChecked():
            cortar=len(n1)
            cortar2=len(str(entera))+n2-1
            errorab=0.5*10**-n2
        else:
            self.t3.setText(str("Seleccione 1"))
            
        em=errorab/float(n1)
        desp=n1[cortar2:cortar]
        
        self.t3.setText(str(errorab)) # Em(x)
        self.t4.setText(str(em)) # em(x)
        self.t5.setText(str(desp)) # despresiables
        
app=QApplication(sys.argv)
_ventana=Ventana()
_ventana.show()
app.exec()