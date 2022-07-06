# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 10:50:20 2022

@author: Steve
"""

import sqlite3
conexion = sqlite3.connect("bdbiblioteca.db")
cursor = conexion.cursor()
consulta = """ DELETE FROM EDITORIAL
                WHERE
                    IDEDITORIAL = 5
            """
cursor = conexion.cursor()
cursor.execute(consulta)
conexion.commit()
conexion.close()
