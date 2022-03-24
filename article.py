import os
import pandas as pd
class article: 
    def __init__(self, lista_de_imagenes,Titulo,Descripcion,Precio,moneda,descripcion_completa,Categoria_clasipar,Sub_categoria_clasipar,Departamento,Zona,Categoria_hendyla,Condicion,forma_de_pago,ciudad): 
        self.lista_de_imagenes = lista_de_imagenes
        self.Titulo = Titulo
        self.Descripcion = Descripcion
        self.Precio = Precio
        self.moneda = moneda
        self.descripcion_completa = descripcion_completa
        self.Categoria_clasipar = Categoria_clasipar
        self.Sub_categoria_clasipar = Sub_categoria_clasipar
        self.Departamento = Departamento
        self.Zona = Zona
        self.Categoria_hendyla = Categoria_hendyla
        self.Condicion = Condicion
        self.forma_de_pago = forma_de_pago
        self.ciudad = ciudad


def make_article_list(article_list: list):
    df = pd.read_excel('Excel\\autoPosterData.xlsx',sheet_name='products',skiprows=1)
    for row in df.iterrows():
        print(row)
        row = row[1]
        print(row)
        lista_de_imagenes = []
        direccion_de_la_imagen = row["direccion de la imagen"]
        Titulo = row["Titulo"]
        Descripcion = row["Descripcion"]
        Precio = row["Precio"]
        moneda = row["moneda [gs/usd]"]
        descripcion_completa = row["descripcion completa"]
        Categoria_clasipar = row["Categoria clasipar"]
        Sub_categoria_clasipar = row["Sub categoria calsipar"]
        Departamento = row["Departamento"]
        ciudad = row["ciudad"]
        Zona = row["Zona"]
        Categoria_hendyla = row["Categoria [cat1,cat2,cat3]"]
        Condicion = row["Condicion [nuevo / recondicionado / usado] "]
        forma_de_pago = row["forma de pago [contado / cuotas / entrega]"]
        #for filename in os.scandir(direccion_de_la_imagen):
        #    if filename.is_file():
        #        print(filename.path)
        #        lista_de_imagenes.append(filename.path)
        lista_de_imagenes = ["asd","asdasd"]
        new_article = article(lista_de_imagenes,Titulo,Descripcion,Precio,moneda,descripcion_completa,Categoria_clasipar,Sub_categoria_clasipar,Departamento,Zona,Categoria_hendyla,Condicion,forma_de_pago,ciudad)
        article_list.append(new_article)

