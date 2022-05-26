from flask import flash
from controllers.validations import validations_controller
from controllers.consult_database import get_shortener_controller
from config import settings
from models.shortener import insert_shortener
import string
import random

def ControllerShortener(url):
    isValid = True
    if not validations_controller.ControllerValidateEmpty(url):
        flash('Porfavor ingrese la url que desea acortar')
        isValid = False
    else:
        if not validations_controller.Val_url(url):
            flash("Ingrese una direccion url valida")
            isValid = False
        if get_shortener_controller.GetShortUrlExits(url) != None:
            flash("La url ingresada fue generada por esta pagina")
            isValid = False
    return isValid
    
def ControllerSendShortenerDatabase(url):
    Val_url = get_shortener_controller.GerLargeUrlExits(url)
    if Val_url is None:
        short =(''.join(random.choice(string.ascii_letters + string.digits) for _ in range(3)))
        short_url = settings.URL_PAGE+"/"+short
        insert_shortener.CreateShortener(short_url=short_url, large_url=url)
    else:
        short_url = Val_url['short_url']
    return short_url