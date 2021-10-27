# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 20:15:49 2021

@author: Edwin
"""

class Asiento :

    def __init__ (self, color, precio, registro) :
        self.registro = registro
        self.precio = precio
        self.color = color

    def cambiarColor (self, color) :
        C=['rojo','verde','amarillo','negro','blanco']
        if (color in C)==True:
            self.color = color


class Auto :
    cantidadCreados = 0
    def __init__ (self, modelo, precio, asientos, marca, motor, registro) :
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro

    def cantidadAsientos (self) :
        a = 0
        for k in self.asientos :
            if isinstance (k, Asiento) :
                a = a+1
        return a

    def verificarIntegridad (self) :
        b = False
        if self.motor.registro == self.registro :
            for i in self.asientos :
                if isinstance (i, Asiento) and i.registro == self.registro :
                    b = True
                elif  isinstance (i, Asiento) and i.registro != self.registro:
                    b = False
                    break
        else:
            b = False

        if b == False:
            return ("Las piezas no son originales")
        else:
            return ("Auto original")
        

class Motor :

    def __init__ (self, numeroCilindros, tipo, registro) :
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro (self, nregistro) :
        self.registro = nregistro

    def asignarTipo (self, tipomotor) :
        if tipomotor == "normal" or tipomotor == "electrico" :
            self.tipo = tipomotor
