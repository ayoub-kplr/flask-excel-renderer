from flask import Flask,  render_template, request
import pandas

app = Flask(__name__)


@app.get('/')
def upload():
    return render_template('upload_excel.html')


@app.post('/view')
def view():
    # Lire le fichier à l'aide de la requête Flask
    file = request.files['file']
    # Enregistrer le fichier dans le répertoire local
    file.save(file.filename)

    # Analyser les données en tant que type Pandas DataFrame
    data = pandas.read_excel(file)

    # Renvoyer l'extrait de code HTML qui affichera le tableau
    return render_template("table.html", data=data.to_html(classes=["table"]))


if __name__ == '__main__':
    app.run(debug=True)
