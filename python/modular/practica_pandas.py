import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 
z=pd.Series([2,4,6,8,10])
print(z)
altura={'santiago':187,'pedro':178, 'julia':170, 'ana':165}
new=pd.Series(altura)
print(new)
new2=new=pd.Series(altura, index=['pedro', 'julia'])
print(new2)
serie=pd.Series([2,3,4,5], index=['num1','num2','num3','num4'])
print(serie['num3']) 
print(serie[2]) 
#representacion grafica 
temperatura=[4.4, 5.1, 6.1, 6.2, 6.1, 6.1, 5.7, 5.2, 4.7, 4.1, 3.9]
temp=pd.Series(temperatura, name="Temperaturas")
print(temp)
temp.plot()
plt.show()
#DATAFRAME
personas={
    "peso": pd.Series([84,90,56,64], ["Santiago", "Pedro", "Ana", "Julia"]), 
    "altura": pd.Series({"Santiago":187, "Pedro":178, "Julia":170, "Ana":165}), 
    "hijos": pd.Series([2,3], ["Pedro", "Julia"])
}
df=pd.DataFrame(personas)
print(df)
df1=pd.DataFrame(personas, columns=["altura", "peso"], index=["Ana", "Julia", "Santiago"])
print(df1)
valores=[
    [185,4,76], 
    [170,0,65], 
    [190,1,89]
]
val=pd.DataFrame(valores, columns=["altura", "hijos", "peso"], index=["jhiro", "lily", "yofré"])
print(val)
otherway={
    "altura":{"Santiago":187, "Pedro":178, "Julia":170, "Ana":165}, 
    "peso":{"Santiago":87, "Pedro":78, "Julia":70, "Ana":65}
}
df2=pd.DataFrame(otherway)
print(df2)
print(df["peso"])
print(df[["peso", "altura"]])
print(df[df["peso"]>=80])
print(df.loc["Pedro"]) #usar df.loc y df.iloc para acceder ()/en series tbm se puede usar
print(df.iloc[2])
print(df.query("altura>=170 and peso>70"))
#copias de dataframes
df_copia=df.copy()
#modificar un dataframe
df["nacimiento"]=[1990,1987,1980,1994]#añadir nueva columna
print(df)
df["años"]=2024-df["nacimiento"]#añadir columna calculado con otras columnas
print(df)
df_mod=df.assign(Mascotas=[0,1,2,1])#crear nuevo dataframe con nuevas columnas
print(df_mod)
del df["peso"]#eliminar una columna
print(df)
#eliminar la columna pero devolviendo otro dataframe nuevo
defdel=df.drop(["hijos"], axis=1)
print(defdel)
df.eval("media_altura=altura/2", inplace=True)#evaluar y agregar columna
print(df)
max_altura=180
print(df.eval("altura>@max_altura"))
#aplicar funcion externa
def func(x):
    return x+2
print(df["altura"].apply(func))