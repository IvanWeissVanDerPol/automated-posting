from instabot import Bot
from article import article
from user import user
#############################################
#login page

def post(user_info:user,article_list):
    bot = Bot()
    
    bot.login(username = user_info.instagram_mail,password = user_info.instagram_pass)
    for article in article_list:
        pic_path = article.lista_de_imagenes
        descripcion = article.descripcion_completa
        bot.upload_photo(pic_path, descripcion)
    
