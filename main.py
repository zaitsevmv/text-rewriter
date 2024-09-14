import os
from dotenv import load_dotenv, dotenv_values 

from ui import App

def ya_request():
    https://translate.yandex.ru/?source_lang=ru&target_lang=emj&text=Привет%2C%20как%20дела

def main():
    load_dotenv("keys.env") 
    os.getenv("YA_KEY")
    app = App()
    app.Start()

if __name__ == "__main__":
    main()