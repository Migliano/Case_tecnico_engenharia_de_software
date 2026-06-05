from app import create_app

app = create_app() 

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False) 
    ''
#reloader falso para recarregar a pagina enquanto preenche infos e não perder o que foi escrito no html
#debug=True só em desenvolvimen