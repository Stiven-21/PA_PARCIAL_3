from config.database import db

def CreateShortener(large_url, short_url):
    cursor = db.cursor()
    cursor.execute('insert into acortador(short_url, large_url) values(%s,%s)',(
        short_url,
        large_url
    ))
    cursor.close()