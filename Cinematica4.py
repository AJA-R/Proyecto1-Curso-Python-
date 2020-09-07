# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 19:07:20 2020

Programa simple para averiguar párametros de cinematica
orientados en movimiento de proyectil y caída libre 
@authors: 
    Anabell Cálix (Incisos: 8, 9)
    Aylin Antunez (Incisos: 6,7)
    Said Flores (Incisos: 1,2,3,4,5)
"""

import math 

def posición_vertical(yo,vyo,t):
    y=yo+vyo*t+(-9.8)*(t**2)/2
    return y

def posición_horizontal(xo,vxo,t):
    x=xo+vxo*t
    return x

def vectores(x,y,t):
    print("El vector de posicíón para el tiempo ",t," segundos es: ")
    print("r(",x," metros",",",y," metros)")
               
def tiempo_vertical(yo,vyo,y):
    discriminante=(vyo**2)-2*(-9.8)*(y-yo)
    if discriminante<0:
        print("No tiene solución en los reales")
    elif discriminante==0:
        t=(-(-vyo))/(-9.8)
        print("El tiempo es:",t, " segundos")
    elif discriminante>0:
        t1=(-(-vyo)+math.sqrt((vyo**2)-2*(-9.8)*(y-yo)))/(-9.8)
        t2=(-(-vyo)-math.sqrt((vyo**2)-2*(-9.8)*(y-yo)))/(-9.8)
        if t1<0:
           print("El tiempo es:",t2, " segundos")
        else:   
           print("El tiempo es:",t1," segundos")

def tiempo_horizontal(x,xo,vxo):
    t=(x-xo)/vxo  
    print("El tiempo es: ",t)    

def velocidad_inicial_y(y,yo,t):
    vyo=((y-yo)/t)-((-9.8)*(t)/2)
    print("La velocidad inicial en y es:",vyo," metros/segundos")
    return vyo
    
def velocidad_inicial_x(x,xo,t):
    vxo=(x-xo)/t    
    print("La velocidad inicial en x es: ",vxo," metros/segundos")
    return vxo

def posición_inicial(x,vxo,y,vyo,t):
    xo=x-vxo*t
    print("La posición inicial en x es: ",xo,"metros")
    yo=y-vyo*t-((-9.8)*(t)**2)/2
    print("La posición inicial en y es: ",yo, "metros")
    
def altura_maxima(vo,theta):
    ymax=((vo*math.sin(theta))**2)/(2*(9.8))
    print("la altura maxima es: ", ymax, "metros")

def tiempo_en_altura_maxima(vo,theta):
    t_hmax=((vo*math.sin(theta))/(9.8))
    print("el tiempo que tarda en alcanzar la maxima altura es: ", t_hmax, "segundos")       
    
def tiempo_vuelo(vyo, yo):
    discriminante=(vyo**2)-2*(-9.8)*(yo)
    if discriminante<0:
        print("No tiene solución en los reales")
    elif discriminante==0:
        t=(-(-vyo))/(-9.8)
        print("El tiempo de vuelo es ", t, "segundos")
        print("¿Desea saber el alcance?")
        op=str(input("Ingrese si o no: "))
        if op=="si":
            xo=float(input("Ingrese la posición inicial en x: "))
            vxo=float(input("Ingrese la velocidad inicial en x: "))
            alcance_horizontal(xo,vxo,t)
    elif discriminante>0:
        t1=(-(-vyo)+math.sqrt((vyo**2)-2*(-9.8)*(yo)))/(-9.8)
        t2=(-(-vyo)-math.sqrt((vyo**2)-2*(-9.8)*(yo)))/(-9.8)
        if t1<0:
           print("El tiempo de vuelo es ", t2, "segundos")
           print("¿Desea saber la distancia a la que se encuentra la repisa?")
           op=str(input("Ingrese si o no: "))
           if op=="si":
            xo=float(input("Ingrese la posición inicial en x: "))
            vxo=float(input("Ingrese la velocidad inicial en x: "))
            alcance_horizontal(xo,vxo,t2)
        else:   
           print("El tiempo de vuelo es: ",t1," segundos")
           print("¿Desea saber la distancia a la que se encuentra la repisa?")
           op=str(input("Ingrese si o no: "))
           if op=="si":
               xo=float(input("Ingrese la posición inicial en x: "))
               vxo=float(input("Ingrese la velocidad inicial en x: "))
               alcance_horizontal(xo,vxo,t1)
    
def alcance_horizontal(xo,vxo,t):
    x=xo+vxo*t
    print("El alcance horizontal es: ",x,"metros ") 

def tiempo_vuelo_ang(vo,theta):
    t1=(-(-vo*math.sin(theta))+math.sqrt(((vo*math.sin(theta))**2)-2*(-9.8)*(0)))/(-9.8)
    t2=(-(-vo*math.sin(theta))+math.sqrt(((vo*math.sin(theta))**2)-2*(-9.8)*(0)))/(-9.8)
    if t2>t1:
        print("El tiempo de vuelo es ", t2, "segundos")
        print("¿Desea saber el alcance?")
        op=str(input("Ingrese si o no: "))
        if op=="si":
            theta=float(input("Ingrese el ángulo de lanzamiento: "))
            vo=float(input("Ingrese la velocidad inicial: "))
            alcance_horizontal_ang(vo,theta,t2)
    else:
        print("El tiempo de vuelo es ", t1, "segundos")
        print("¿Desea saber el alcance?")
        op=str(input("Ingrese si o no: "))
        if op=="si":
            theta=float(input("Ingrese el ángulo de lanzamiento: "))
            vo=float(input("Ingrese la velocidad inicial: "))
            alcance_horizontal_ang(vo,theta,t1)
       
def alcance_horizontal_ang(vo,theta,t):
    x=vo*math.cos(theta)*t
    print("El alcance horizontal es: ",x,"metros ")
    
def decisión_10(sino):
    if sino=="si":
        yo=float(input(print("Ingrese la posición inicial en y:")))
        vyo=float(input(print("Ingrese la velocidad inicial en y:")))
        tiempo_vuelo(vyo,yo)
    elif sino=="no":
        print("¿Sabe la velocidad inicial y el ángulo (en radianes) de lanzamiento?")
        sino=str(input("Ingrese si o no: "))
        if sino=="si":
            theta=float(input(print("Ingrese el ángulo de lanzamiento (en radianes):")))
            vo=float(input(print("Ingrese la velocidad inicial: ")))
            tiempo_vuelo_ang(vo,theta)
        elif sino=="no":
            print("No tiene datos suficientes")
        else:
            print("No ingreso de forma correcta si o no")
    else:
         print("No ingreso de forma correcta si o no")  

def tiempo_vuelo_h(vyo, yo, h):
    discriminante=(vyo**2)-2*(-9.8)*(yo-h)
    if discriminante<0:
        print("No tiene solución en los reales")
    elif discriminante==0:
        t=(-(-vyo))/(-9.8)
        print("El tiempo de vuelo es ", t, "segundos")
        print("¿Desea saber el alcance?")
        op=str(input("Ingrese si o no: "))
        if op=="si":
            xo=float(input("Ingrese la posición inicial en x: "))
            vxo=float(input("Ingrese la velocidad inicial en x: "))
            alcance_horizontal_h(xo,vxo,t)
    elif discriminante>0:
        t1=(-(-vyo)+math.sqrt((vyo**2)-2*(-9.8)*(yo-h)))/(-9.8)
        t2=(-(-vyo)-math.sqrt((vyo**2)-2*(-9.8)*(yo-h)))/(-9.8)
        if t1<0:
           print("El tiempo de vuelo es ", t2, "segundos")
           print("¿Desea saber la distancia a la que se encuentra la repisa?")
           op=str(input("Ingrese si o no: "))
           if op=="si":
            xo=float(input("Ingrese la posición inicial en x: "))
            vxo=float(input("Ingrese la velocidad inicial en x: "))
            alcance_horizontal_h(xo,vxo,t2)
        else:   
           print("El tiempo de vuelo es: ",t1," segundos")
           print("¿Desea saber la distancia a la que se encuentra la repisa?")
           op=str(input("Ingrese si o no: "))
           if op=="si":
               xo=float(input("Ingrese la posición inicial en x: "))
               vxo=float(input("Ingrese la velocidad inicial en x: "))
               alcance_horizontal_h(xo,vxo,t1)            
       
def alcance_horizontal_h(xo,vxo,t):
    x=xo+vxo*t
    print("La distancia de la repisa al punto de lanzamiento es: ",x,"metros ") 

def tiempo_vuelo_ang_h(vo,theta,h):
    t1=(-(-vo*math.sin(theta))+math.sqrt(((vo*math.sin(theta))**2)-2*(-9.8)*(h)))/(-9.8)
    t2=(-(-vo*math.sin(theta))+math.sqrt(((vo*math.sin(theta))**2)-2*(-9.8)*(h)))/(-9.8)
    if t2>t1:
        print("El tiempo de vuelo es ", t2, "segundos")
        print("¿Desea saber la distancia a la que se encuentra la repisa?")
        op=str(input("Ingrese si o no: "))
        if op=="si":
            theta=float(input("Ingrese el ángulo de lanzamiento: "))
            vo=float(input("Ingrese la velocidad inicial: "))
            alcance_horizontal_ang_h(vo,theta,t2)
    else:
        print("El tiempo de vuelo es ", t1, "segundos")
        print("¿Desea saber el alcance?")
        op=str(input("Ingrese si o no: "))
        if op=="si":
            theta=float(input("Ingrese el ángulo de lanzamiento: "))
            vo=float(input("Ingrese la velocidad inicial: "))
            alcance_horizontal_ang_h(vo,theta,t1)
       
def alcance_horizontal_ang_h(vo,theta,t):
    x=vo*math.cos(theta)*t
    print("La distancia de la repisa al punto de lanzamiento es: ",x,"metros ")

def decisión_11(sino):
    if sino=="si":
        yo=float(input("Ingrese la posición inicial en y:"))
        vyo=float(input("Ingrese la velocidad inicial en y:"))
        h=float(input("Ingrese la altura de la repisa: "))
        tiempo_vuelo_h(vyo,yo,h)
    elif sino=="no":
        print("¿Sabe la velocidad inicial y el ángulo (en radianes) de lanzamiento?")
        sino=str(input("Ingrese si o no: "))
        if sino=="si":
            theta=float(input("Ingrese el ángulo de lanzamiento (en radianes):"))
            vo=float(input("Ingrese la velocidad inicial: "))
            h=float(input("Ingrese la altura de la repisa: "))
            tiempo_vuelo_ang_h(vo,theta,h)
        elif sino=="no":
            print("No tiene datos suficientes")         
    
def programa_calculador():     
    print("Use metros, segundos y metros/segundos") 
    print("En algunas opciones es necesario saber parametros tanto en y como en x")     
    print("Las cosas que puede saber son: ")
    print("1) vector de posición r(x,y)")
    print("2) tiempo vertical")
    print("3) tiempo horizontal")
    print("4) velocidad inicial")     
    print("5) posición inicial")
    print("6) Altura máxima")
    print("7) Tiempo en que alcanza la altura máxima")
    print("8) Tiempo de vuelo")
    print("9) Tiempo de vuelo necesario para que una pelota caiga en una repisa de altura h")
    op=str(input(print("Ingrese el número de la opción que desea saber:")))
    if op=="1":
        print("Desea saber la posición")
        yo=float(input("Ingrese la posición inicial en y:"))
        vyo=float(input("Ingrese la velocidad inicial en y:"))       
        xo=float(input("Ingrese la posición inicial en x:")) 
        vxo=float(input("Ingrese la velocidad inicial en x:"))      
        t=float(input("Ingrese el tiempo:"))
        y=posición_vertical(yo, vyo,t)
        x=posición_horizontal(xo,vxo,t)
        vectores(x,y,t)
    elif op=="2":
        print("Desea saber el tiempo vertical")
        y=float(input("Ingrese la posición en y:"))
        yo=float(input("Ingrese la posición inicial en y:"))
        vyo=float(input("Ingrese la velocidad inicial en y:"))
        tiempo_vertical(yo,vyo,y)
    elif op=="3":
        print("Desea saber el tiempo horizontal")
        x=float(input("Ingrese la posición en x:"))  
        xo=float(input("Ingrese la posición x inicial:"))  
        vxo=float(input("Ingrese la velocidad inicial en x:"))
        tiempo_horizontal(x,xo,vxo)
    elif op=="4":
       print("Desea saber la velocidad inicial")    
       print("Se asume que el tiempo inicial es igual a cero")
       y=float(input("Ingrese la posición final en y: "))
       yo=float(input("Ingrese la posición inicial en y: "))            
       x=float(input("Ingrese la posición final en x: "))
       xo=float(input("Ingrese la posición inicial en x:"))  
       t=float(input("Ingrese el tiempo:"))
       vxo=velocidad_inicial_x(x,xo,t)
       vyo=velocidad_inicial_y(y,yo,t)
       print("La velocidad inicial es Vo=(",vxo,",",vyo,")")
    elif op=="5":
        print("Desea saber la posición inicial")
        x=float(input("Ingrese la posición en x:"))
        vxo=float(input("Ingrese la velocidad inicial en x:"))
        y=float(input("Ingrese la posición en y: "))
        vyo=float(input("Ingrese la velocidad inicial en y:"))
        t=float(input("Ingrese el tiempo:")) 
        posición_inicial(x,vxo,y,vyo,t)
    elif op=="6":
        print("Desea saber la altura maxima")
        vo=float(input("Ingrese la velocidad inicial (en metros/segundos): "))
        theta=float(input("Ingrese el angulo de lanzamiento a nivel del suelo (valor en radianes): "))
        altura_maxima(vo,theta)
    elif op=="7":
        print("Desea conocer el tiempo en que tarda en alcanzar la altura maxima")
        vo=float(input("Ingrese la velocidad inicial (en metros/segundos): "))
        theta=float(input("Ingrese el angulo de lanzamiento a nivel del suelo (valor en radianes): "))
        tiempo_en_altura_maxima(vo,theta)
    elif op=="8":
        print("Desea saber el tiempo de vuelo")
        sino=str(input("¿Sabe la velocidad inicial en 'x' y 'y'?: ")) 
        decisión_10(sino) 
    elif op=="9":
        print("Desea saber el tiempo de vuelo necesario para que una pelota caiga en una repisa de altura h")
        sino=str(input("¿Sabe la velocidad inicial en 'x' y 'y'?: ")) 
        decisión_11(sino) 
    else:
       print("No seleccionó ninguna opción")
       
def decisión(cont):
    while cont=="si":
     programa_calculador()
     print("¿Desea saber algo más?")
     cont=str(input("Escriba si o no (en minuscula y sin espacios enfrente o detrás): "))
    if cont=="no":
     print("Fue un placer") 
    else: 
     print("No ingreso 'si' o 'no' de forma correcta intentelo otra vez")
     sino=str(input("Escriba si o no (sin espacios enfrente o detrás):")) 
     cont=sino
     decisión(cont)
     
print("Bienvenido")
print("Este programa le ayudará a calcular valores de las ecuaciones de cinemática")        
print("¿Desea saber algo?")
sino=str(input("Escriba si o no (sin espacios en frente o detrás):")) 
cont=sino         
decisión(cont)

