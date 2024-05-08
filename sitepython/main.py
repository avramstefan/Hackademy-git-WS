from website import create_app

app = create_app()
#verifică dacă scriptul este rulat direct (nu importat ca modul)
#convenție în Python pentru a asigura că aplicația va fi pornită doar atunci când scriptul este rulat direct și nu când este importat în alt script
if __name__ == '__main__':
    app.run(debug=True)# face ca serverul să repornească automat la modificările aduse în cod (util în timpul dezvoltării), și furnizează informații detaliate despre erori în cazul apariției acestora
    