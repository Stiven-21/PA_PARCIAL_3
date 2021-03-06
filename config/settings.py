from dotenv import load_dotenv
import os 

#OBTIENE LAS VARIABLES DEL .env
load_dotenv()

MYSQL_HOSTNAME = os.environ.get("MYSQL_HOSTNAME")
MYSQL_USERNAME = os.environ.get("MYSQL_USERNAME")
MYSQL_PASSWORD = os.environ.get("MYSQL_PASSWORD")
MYSQL_DATABASE = os.environ.get("MYSQL_DATABASE")
MYSQL_PORT = os.environ.get("MYSQL_PORT")

SMTP_HOSTNAME = os.environ.get("SMTP_HOSTNAME")
SMTP_USERNAME = os.environ.get("SMTP_USERNAME")
SMTP_PASSWORD = os.environ.get("SMTP_PASSWORD")

URL_PAGE = os.environ.get("URL_PAGE")

ROUTE_IMAGE = os.environ.get("ROUTE_IMAGE")
ROUTE_IMAGE_DEFAULT = os.environ.get("ROUTE_IMAGE_DEFAULT")

TOKEN_DISCORD =os.environ.get("TOKEN_DISCORD")