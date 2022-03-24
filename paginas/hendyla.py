from selenium import webdriver
import time

from user import user
sleeptime = 0.4
main_page = "https://www.hendyla.com"
post_page = "https://www.hendyla.com/publicar/anuncio.html"

def post(browser,user_info:user,article_list):

    email = user_info.hendyla_mail
    password = user_info.hendyla_pass
    telefono = user_info.telefono
    
    log_in(browser,email,password)    
    for articulo in article_list:
        title = articulo.Titulo
        categoria = articulo.Categoria_hendyla
        condition = articulo.Condicion
        descripcion = articulo.Descripcion
        precio = articulo.Precio
        currency = articulo.moneda
        payment_method = articulo.forma_de_pago
        pic_path = articulo.lista_de_imagenes
        ciudad = articulo.ciudad
        post_add(browser,title,categoria,condition,descripcion,precio,currency,payment_method,telefono,ciudad,pic_path)
    

##############login page###############
def log_in(browser:webdriver, email,password):
    log_in_button_Xpath = "/html/body/div[1]/header/div/div/ul/li[4]/ul/li[2]/div/a[1]"
    email_block_Xpath = '//*[@id="username"]'
    pass_block_Xpath = '//*[@id="password"]'
    log_in_finish_button_Xpath = '//*[@id="login-hendyla-form"]/div[4]/input[3]'
    url = main_page
    time.sleep(5)    
    browser.get(url)
    time.sleep(sleeptime)
    browser.find_element_by_xpath(log_in_button_Xpath).click()
    time.sleep(sleeptime)
    browser.find_element_by_xpath(email_block_Xpath).send_keys(email)
    browser.find_element_by_xpath(pass_block_Xpath).send_keys(password)
    browser.find_element_by_xpath(log_in_finish_button_Xpath).click()
    time.sleep(sleeptime)
    
    
    
def post_add(browser,title,categoriasTexto,condition,descripcion,precio,currency,payment_method,telefono,ciudad,pic_path):
    title_name = 'title'
    categorias_Xpath = 'parent-cats'
    descripcion_ID = 'tinyeditor'
    precio_ID = 'price'
    departamento_ID = 'project'
    publish_ID = 'publicar-btn'
    telefono_ID = 'phone'
    file_upload_drop_zone_Xpath = '/html/body/div[2]/section/form/div[3]/div[1]/div[1]/div[1]/div/input[2]'
    url = post_page
    
    time.sleep(sleeptime)
    browser.get(url)
    time.sleep(sleeptime)
    browser.find_element_by_name(title_name).send_keys(title)

    categoriasTexto = "Electrónica,Otros en Electrónica"
    categoriasLista = categoriasTexto.split(",")
    menu = browser.find_element_by_id(categorias_Xpath)
    time.sleep(sleeptime)


# this is by no means the best solution but im not sure how else to select the correct category
# but based on the fact that the process has x<50 elements it still works fast enough and lets the users simply put
# the catgories in a simple manneer cat1,cat2,cat3,etc #
# #

    for category in categoriasLista:
        foundElement = False
        DivList = menu.find_elements_by_tag_name("div")
        for divElement  in DivList:     
            liList = divElement.find_elements_by_tag_name("li")
            for liElement  in liList:
                if liElement.text == category:
                    liElement.click()
                    time.sleep(sleeptime)   
                    foundElement = True
                    break
            if foundElement:
                break
    browser.find_element_by_xpath('//*[@id="lista3"]/div/div/a').click( )
    time.sleep(sleeptime)
    for pic in pic_path:
        browser.find_element_by_xpath(file_upload_drop_zone_Xpath).send_keys(pic)
    if(condition == "nuevo"):
        browser.find_element_by_xpath('//*[@id="condicion-detalle"]/label[1]/input').click( )
    elif(condition == "nuevo"):
        browser.find_element_by_xpath('//*[@id="condicion-detalle"]/label[2]/input').click( )
    elif(condition == "nuevo"):
        browser.find_element_by_xpath('//*[@id="condicion-detalle"]/label[3]/input').click( )
    browser.find_element_by_id(descripcion_ID).send_keys(descripcion)
    browser.find_element_by_id(precio_ID).send_keys(precio)
    if(currency == "gs"):
        browser.find_element_by_xpath('//*[@id="currency"]/option[1]').click()
    elif(currency == "usd"):
        browser.find_element_by_xpath('//*[@id="currency"]/option[2]').click() 
    if(payment_method == "contado"):
        browser.find_element_by_xpath('//*[@id="forma_pago"]/option[1]')
    elif(payment_method == "cuotas"):
        browser.find_element_by_xpath('//*[@id="forma_pago"]/option[2]')
    elif(payment_method == "entrega"):
        browser.find_element_by_xpath('//*[@id="forma_pago"]/option[3]')
    browser.find_element_by_id(telefono_ID).clear()
    browser.find_element_by_id(telefono_ID).send_keys(telefono)
    browser.find_element_by_id(departamento_ID).clear()
    browser.find_element_by_id(departamento_ID).send_keys(ciudad)
    time.sleep(sleeptime)
    browser.find_element_by_xpath('//*[@id="ui-id-1"]').find_elements_by_tag_name("div")[0].click()
    browser.find_element_by_id(publish_ID).click()