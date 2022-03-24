import pandas as pd


class user: 
    def __init__(self,hendyla_mail,hendyla_pass,clasipar_mail,clasipar_pass,instagram_mail,instagram_pass,telefono,celular,whatsapp_ok,contact_email): 
        self.hendyla_mail = hendyla_mail
        self.hendyla_pass = hendyla_pass
        self.clasipar_mail = clasipar_mail
        self.clasipar_pass = clasipar_pass
        self.instagram_mail = instagram_mail
        self.instagram_pass = instagram_pass
        self.telefono = telefono
        self.celular = celular
        self.whatsapp_ok = whatsapp_ok
        self.contact_email = contact_email

def get_user_info():
    hendyla_mail = ""
    hendyla_pass = ""
    clasipar_mail = ""
    clasipar_pass = ""
    instagram_mail = ""    
    instagram_pass = ""
    telefono = ""
    celular = ""
    whatsapp_ok = ""
    contact_email = ""
    df = pd.read_excel('Excel\\autoPosterData.xlsx',sheet_name='paginas',skiprows=1)
    for cont in range(0,len(df)):
        content = df.loc[cont]
        if content["pagina"] == "hendyla":
            hendyla_mail = content["usuario/email"]
            hendyla_pass = content["contraseña"]
        if content["pagina"] == "clasipar":
            clasipar_mail = content["usuario/email"]
            clasipar_pass = content["contraseña"]
        if content["pagina"] == "instagram":
            instagram_mail = content["usuario/email"]
            instagram_pass = content["contraseña"]
            break
    df = pd.read_excel('Excel\\autoPosterData.xlsx',sheet_name='paginas',skiprows=7)
    for cont in range(0,len(df)):
        content = df.loc[cont]
        if content["campos"] == "telefono":
            telefono = content["datos para contacto"]
        if content["campos"] == "celular":
            celular = content["datos para contacto"]
        if content["campos"] == "contacto por whatsapp":
            whatsapp_ok = content["datos para contacto"]
            if whatsapp_ok.lower() == "si":
                whatsapp_ok = True
            else:
                whatsapp_ok = False
        if content["campos"] == "email":
            contact_email = content["datos para contacto"]
    new_user = user(hendyla_mail,hendyla_pass,clasipar_mail,clasipar_pass,instagram_mail,instagram_pass,telefono,celular,whatsapp_ok,contact_email)
    return new_user
