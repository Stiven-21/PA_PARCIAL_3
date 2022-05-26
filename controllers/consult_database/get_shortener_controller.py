from models.shortener import select_shortener

def GerLargeUrlExits(url):
    return select_shortener.GetLargeUrlExits(url=url)

def GetUrlForRedirect(short_url):
    return select_shortener.GetUrlRedirect(short_url=short_url)

def GetShortUrlExits(url):
    return select_shortener.GetShortUrlExits(short_url=url)