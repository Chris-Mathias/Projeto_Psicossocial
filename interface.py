from flask import Flask, render_template, request
import pandas as pd
import graphs

app = Flask(__name__)

@app.route('/estabelecimentos', methods=['GET', 'POST'])
def estabelecimentos():
    fig = graphs.plot_pie('CNES_EXEC')

    if request.method == 'POST':
        years = request.form.getlist('years')
        fig = graphs.plot_pie('CNES_EXEC', years)

    return render_template('estabelecimentos.html', plot=fig.to_html())

@app.route('/idades', methods=['GET', 'POST'])
def idades():
    fig = graphs.plot_line('IDADEPAC')

    if request.method == 'POST':
        years = request.form.getlist('years')
        fig = graphs.plot_line('IDADEPAC', years)

    return render_template('idades.html', plot=fig.to_html())

@app.route('/municipios', methods=['GET', 'POST'])
def municipios():
    fig = graphs.plot_bar('MUNPAC')

    if request.method == 'POST':
        years = request.form.getlist('years')
        fig = graphs.plot_bar('MUNPAC', years)

    return render_template('municipios.html', plot=fig.to_html())

@app.route('/raca', methods=['GET', 'POST'])
def raca():
    fig = graphs.plot_pie('RACACOR')

    if request.method == 'POST':
        years = request.form.getlist('years')
        fig = graphs.plot_pie('RACACOR', years)

    return render_template('raca.html', plot=fig.to_html())

@app.route('/cid', methods=['GET', 'POST'])
def cid():
    fig = graphs.plot_bar('CIDPRI')

    if request.method == 'POST':
        years = request.form.getlist('years')
        fig = graphs.plot_bar('CIDPRI', years)

    return render_template('cid.html', plot=fig.to_html())

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)