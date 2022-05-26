from config.database import db

def GetLargeUrlExits(url):
    cursor = db.cursor(dictionary=True)
    cursor.execute('SELECT * FROM acortador WHERE large_url="'+url+'" ')
    UrlDate = cursor.fetchone()
    cursor.close()
    return UrlDate

def GetUrlRedirect(short_url):
    cursor = db.cursor(dictionary=True)
    cursor.execute('SELECT * FROM acortador WHERE short_url  LIKE "%'+short_url+'" ')
    UrlDate = cursor.fetchone()
    cursor.close()
    return UrlDate

def GetShortUrlExits(short_url):
    cursor = db.cursor(dictionary=True)
    cursor.execute('SELECT * FROM acortador WHERE short_url = "'+short_url+'" ')
    UrlDate = cursor.fetchone()
    cursor.close()
    return UrlDate
    