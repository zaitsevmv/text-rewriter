from dotenv import load_dotenv, dotenv_values 
from ui import App
from api import first_request, second_request

def main():
    load_dotenv("keys.env") 
    app = App(first_request, second_request)
    app.Start()

if __name__ == "__main__":
    load_dotenv("keys.env")
    main()