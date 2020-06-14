#!/usr/bin/env python
# coding: utf-8

# In[6]:



import numpy as np
pi=np.pi
import tkinter as tk    
from tkinter import ttk

column=0;row=0

win = tk.Tk()           
win.title("Gases disueltos en aceite - Posibles efectos")


especies=["H2","C2H6","CH4","C2H4","C2H2"]
especies2=["Hidrogeno - H2",          "Etano - C2H6",          "Metano - CH4",          "Etileno - C2H4",          "Acetileno - C2H2"]

radio=150
w = tk.Canvas(win,width=radio*2.5,height=radio*2.5)

entradas=[]
escrituras=[]
porcentajes=[]
nuevos=[]
porcentajetxt=[]
polivalue=[]


 
def num(s):
    try:
        return int(s)
    except ValueError:
        return float(s)

def modifica(*args):
    puntos2=[];xi=[];yi=[]
    for i in range(len(escrituras)):
        nuevos[i]=float(escrituras[i].get())
    total=sum(nuevos)
    for i in range(len(escrituras)):
        porcentajetxt[i].set(str(round(nuevos[i]/total*100,4))+"%")
        polivalue[i]=nuevos[i]/total*100
    for i in range(len(escrituras)):
        x2=np.sin(i*angulo/180*pi)*polivalue[i]*ratio+1.25*radio
        y2=np.cos(i*angulo/180*pi)*polivalue[i]*ratio+1.25*radio
        puntos2.append(x2);xi.append(x2)
        puntos2.append(y2);yi.append(y2)
    xi=np.array(xi);yi=np.array(yi)
    
    w.coords(porigon, puntos2);w.tag_raise(porigon)
    A=1/2*abs(np.sum(xi[:-1]*yi[1:])+xi[-1]*yi[0]-np.sum(xi[1:]*yi[:-1])-xi[0]*yi[-1])
    cx=-1/(6*A)*(np.sum((xi[:-1]+xi[1:])*(xi[:-1]*yi[1:]-xi[1:]*yi[:-1]))+(xi[-1]+xi[0])*(xi[-1]*yi[0]-xi[0]*yi[-1]))
    cy=-1/(6*A)*(np.sum((yi[:-1]+yi[1:])*(xi[:-1]*yi[1:]-xi[1:]*yi[:-1]))+(yi[-1]+yi[0])*(xi[-1]*yi[0]-xi[0]*yi[-1]))
    w.coords(centroide,cx,cy,cx,cy);w.tag_raise(centroide)
    w.itemconfig(centroide, fill="white",outline="black",width = 2)
    
    masdeuno=[]
    for i in range(len(diagnosticos)):
        if inside_polygon(cx, cy, diagnosticos[i]):
            masdeuno.append(diagnosticos2[i])
    diag.set(("\n\n").join(masdeuno))
    
    
        
esp=ttk.Label(win,text="Especie de gas", background="cyan",anchor="sw").grid(row=row,column=column,padx=20,sticky="W",pady=(20,0))
porc=ttk.Label(win,text="Porcentaje:", background="").grid(row=row,column=column+2,sticky="W",padx=20,pady=(20,0))
anal=ttk.Label(win,text="Ingrese análisis elemental:", background="").grid(row=row,column=column+1,sticky="W",pady=(20,0));row=row+1

for i in range(5):
    polivalue.append(0)
    porcentajetxt.append(tk.StringVar(value=0))
    nuevos.append(float(0))
    escrituras.append(tk.StringVar(value="0"))
    entradas.append(tk.Entry(win,textvariable=escrituras[i]))
    escrituras[i].trace("w",modifica)
    entradas[i].grid(column=1,row=row,sticky="W")
    ttk.Label(win,text=especies2[i]).grid(column=0,row=row,sticky="W",padx=20)
    porcentajes.append(ttk.Label(win,textvariable=porcentajetxt[i]))
    porcentajes[i].grid(column=column+2,row=row,sticky="W",padx=20);row=row+1
    

puntos=[]

lados=5
angulo=360/lados
for i in range(lados):
    x=np.sin(i*angulo/180*pi)*radio+radio*1.25
    y=np.cos(i*angulo/180*pi)*radio+radio*1.25
    w.create_text((x, y), text=especies[i])
    puntos.append(x)
    puntos.append(y)

ratio=radio/100
#Areas
PD=[(0,24.5),(0,33),(-1,33),(-1,24.5)]
D1=[(0,40),(38.04,12.36),(32,-6),(4,16),(0,1.5)]
D2=[(4,16),(32,-6),(24.3,-30),(-1.6,-3.7)]
T1=[(-22.5,-32.36),(-21,-32.36),(-6,-4),(-1,-2),(0,1.5),(-35,3)]
T2=[(-1,-32.36),(-6,-4),(-21,-32.36)]
T3=[(24.3,-30),(-1,-2),(-6,-4),(-1,-32.36),(23.51,-32.36)]
S=[(-35,3),(0,1.5),(0,24.5),(-1,24.5),(-1,33),(0,33),(0,40),(-38.04,12.36)]
O=[(-23.51,-32.36),(-21,-32.36),(-11,-9),(-3.5,-3.1),(-1.6,-3.7),(-35,3)]
C=[(-21,-32.36),(-11,-9),(-3.5,-3.1),(4,-32.36)]
T3H=[(24.3,-30),(23.51,-32.36),(4,-32.36),(-3.5,-3.1),(-1.6,-3.7)]
def fixed_center(x):
    for i in range(len(x)):
        x[i]=-x[i][0]*ratio+radio*1.25,x[i][1]*ratio+radio*1.25

fixed_center(PD);fixed_center(D1);fixed_center(D2)
fixed_center(T1);fixed_center(T2),fixed_center(T3)
fixed_center(S);fixed_center(O);fixed_center(C)
fixed_center(T3H)

diagnosticos=[PD,D1,D2,T1,T2,T3,S,O,C,T3H]
diagnosticos2=["PD:\nDescargas parciales"               ,"D1:\nDescargas de baja energía"               ,"D2:\nDescargas de alta energía"               ,"T1:\nTérmicas mayores a los 700°C"               ,"T2:\nFallas térmicas de 300 a 700°C"               ,"T3:\nFallas Térmicas<300°C"               ,"S:\nGasificación Inesperada"               ,"O:\nSobrecalentamiento<250°C"               ,"C:\nFallas térmicas T1, T2, T3 con\ncarbonización del papel en el 80% de los casos"               ,"T3-H:\nTérmicas mayores a los 700°C solo en el aceite"]


porigon=w.create_polygon([0,0],outline='black', fill='')
centroide=w.create_oval(0, 0, 0, 0,outline='', fill="")

baphomet=[(puntos[0],puntos[1])          ,(puntos[4],puntos[5])          ,(puntos[8],puntos[9])          ,(puntos[2],puntos[3])          ,(puntos[6],puntos[7])]

bapho=w.create_polygon(baphomet,     outline='gray85', fill='')
w.tag_lower(bapho)
w.create_polygon(puntos,     outline='black', fill='') 
w.create_polygon(PD,     outline='', fill='yellow')
w.create_polygon(D1,     outline='', fill='blue')
w.create_polygon(D2,     outline='', fill='red')
w.create_polygon(T1,     outline='', fill='violet')
w.create_polygon(T2,     outline='', fill='green')
w.create_polygon(T3,     outline='', fill='cyan')
w.create_polygon(S,     outline='', fill='orange')
w.create_polygon(T3H,     outline='black', fill='',dash=True)
w.create_polygon(C,     outline='black', fill='',dash=True)
w.create_polygon(O,     outline='black', fill='',dash=True)

def create_circle(x, y, r, canvasName): #center coordinates, radius
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvasName.create_oval(x0, y0, x1, y1,outline="red")

cc=[(0,0)];fixed_center(cc)

create_circle(cc[0][0], cc[0][1], radio, w)
create_circle(cc[0][0], cc[0][1], radio*1.05, w)

def inside_polygon(x, y, points):
    """
    Return True if a coordinate (x, y) is inside a polygon defined by
    a list of verticies [(x1, y1), (x2, x2), ... , (xN, yN)].

    Reference: http://www.ariel.com.au/a/python-point-int-poly.html
    """
    n = len(points)
    inside = False
    p1x, p1y = points[0]
    for i in range(1, n + 1):
        p2x, p2y = points[i % n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside
        p1x, p1y = p2x, p2y
    return inside

ttk.Label(win,text="Diagnostico/Zona:").grid(row=row+3,column=column+2,sticky="W",padx=20)
diag=tk.StringVar()
zona=ttk.Label(win,textvariable=diag,justify="left")
zona.grid(column=column+2,sticky="W",padx=20,row=row+4)



w.grid(row=row,rowspan=40,column=0,columnspan=2)
win.mainloop()
get_ipython().run_line_magic('reset', '-f')

