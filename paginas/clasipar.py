from selenium import webdriver
from selenium.webdriver.support.ui import Select as select
import time
from article import make_article_list,article
from user import user
sleeptime = 1



main_page = "https://clasipar.paraguay.com"
log_in_page = "https://clasipar.paraguay.com/iniciar-sesion"
post_page = "https://clasipar.paraguay.com/publicar"

#############################################
#login page

def post(browser,user_info,article_list):

    email = user_info.clasipar_mail
    password = user_info.clasipar_pass
    telefono = user_info.telefono
    celular = user_info.celular
    contact_email = user_info.contact_email
    whatsapp_ok = user_info.whatsapp_ok
    log_in(browser,email,password)    
    for articulo in article_list:
        categoria = articulo.Categoria_clasipar
        subcategoria = articulo.Sub_categoria_clasipar
        title = articulo.Titulo
        descripcion = articulo.Descripcion
        precio = articulo.Precio
        departamento = articulo.Departamento
        zona = articulo.Zona
        pic_path = articulo.lista_de_imagenes
        ciudad = articulo.ciudad
        post_add(browser, categoria,subcategoria,title,descripcion,precio,departamento,ciudad,zona,telefono,celular,contact_email,whatsapp_ok,pic_path)

def log_in(browser,email,password):
    email_block_Xpath = '//*[@id="email"]'
    pass_block_Xpath = '//*[@id="password"]'
    log_in_button = '//*[@id="frm_login"]/button'
    url = log_in_page
    browser.get(url)
    time.sleep(sleeptime)
    browser.find_element_by_xpath(email_block_Xpath).send_keys(email)
    browser.find_element_by_xpath(pass_block_Xpath).send_keys(password)
    browser.find_element_by_xpath(log_in_button).click()
    time.sleep(sleeptime)
    
#############################
#post page
def post_add(browser,categoria,subcategoria,title,descripcion,precio,departamento,ciudad,zona,telefono,celular,email,whatsapp_ok,pic_path):
    anuncio_continuar_Xpath = '//*[@id="newformmodalin"]/div[2]/div/div[3]/button'
    categorias_drop_box_Xpath = '//*[@id="categories"]'
    subcategorias_box_Xpath = '//*[@id="subcategories"]'
    title_ID = 'ad_title'
    descripcion_ID = 'description'
    precio_ID = 'ad_value'
    departamento_xpath = '//*[@id="departament"]/div/div[1]/select'
    ciudad_Xpath = '//*[@id="ciudad"]/div/div[1]/select'
    zona_xpath = '//*[@id="meta_keys"]/div[1]/div[1]/input'
    telefono_ID = 'ad_phone_number'
    celular_ID = 'ad_cellphone_number'
    whatsapp_box_ID = 'ad_cellphone_number_whatsapp'
    email_ID = 'ad_email'
    next_page_ID = 'save_anuncio'
    #file_upload_drop_zone = '/html/body/main/section/div/div[3]/article/form/div[1]/div/div[4]/div[2]/div/input'
    file_upload_drop_zone_ID = "upload-ads-image"
    url = post_page
    
    browser.get(url)
    time.sleep(sleeptime)
    browser.find_element_by_xpath(anuncio_continuar_Xpath).click()
    time.sleep(sleeptime)
    #(categoria y sub categoria)
    select(browser.find_element_by_xpath(categorias_drop_box_Xpath)).select_by_visible_text(categoria)
    time.sleep(sleeptime)
    select(browser.find_element_by_xpath(subcategorias_box_Xpath)).select_by_visible_text(subcategoria)
    time.sleep(sleeptime)
    browser.find_element_by_id(title_ID).send_keys(title)
    browser.find_element_by_id(descripcion_ID).send_keys(descripcion)
    browser.find_element_by_id(precio_ID).send_keys(precio)
    #!moneda
    select(browser.find_element_by_xpath(departamento_xpath)).select_by_visible_text(departamento)
    time.sleep(sleeptime)
    if ciudad != "Asunción":
        select(browser.find_element_by_xpath(ciudad_Xpath)).select_by_visible_text(ciudad)
    browser.find_element_by_xpath(zona_xpath).send_keys(zona)
    browser.find_element_by_id(telefono_ID).send_keys(telefono)
    browser.find_element_by_id(celular_ID).send_keys(celular)
    browser.find_element_by_id(whatsapp_box_ID).send_keys(whatsapp_ok)
    browser.find_element_by_id(email_ID).send_keys(email)
    browser.find_element_by_id(next_page_ID).click()
    time.sleep(sleeptime)
    for pic in pic_path:
        browser.find_element_by_id(file_upload_drop_zone_ID).send_keys(pic)
    browser.find_element_by_id(next_page_ID).click()
    time.sleep(sleeptime)
    
    
    
    