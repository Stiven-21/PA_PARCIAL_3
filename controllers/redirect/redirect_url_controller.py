from controllers.consult_database import get_shortener_controller

def ControllerRedirectUrl(short_url):
    Val_url = get_shortener_controller.GetUrlForRedirect(short_url)
    if Val_url is None:
        return False
    else:
        return Val_url['large_url']