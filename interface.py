from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import graphs

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login = request.form['login']
        password = request.form['password']
        
        if login == 'admin' and password == 'admin':
            return redirect(url_for('estabelecimentos'))
        
    return render_template('login.html')

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

@app.route('/cobertura', methods=['GET', 'POST'])
def cobertura():
    fig = graphs.plot_pie('COB_ESF')

    if request.method == 'POST':
        years = request.form.getlist('years')
        fig = graphs.plot_pie('COB_ESF', years)

    return render_template('cobertura.html', plot=fig.to_html())

@app.route('/situacaorua', methods=['GET', 'POST'])
def situacaorua():
    fig = graphs.plot_pie('SIT_RUA')

    if request.method == 'POST':
        years = request.form.getlist('years')
        fig = graphs.plot_pie('SIT_RUA', years)

    return render_template('situacaorua.html', plot=fig.to_html())

@app.route('/sexo', methods=['GET', 'POST'])
def sexo():
    fig = graphs.plot_pie('SEXOPAC')

    if request.method == 'POST':
        years = request.form.getlist('years')
        fig = graphs.plot_pie('SEXOPAC', years)

    return render_template('sexo.html', plot=fig.to_html())

@app.route('/droga', methods=['GET', 'POST'])
def droga():
    fig = graphs.plot_pie('TP_DROGA')

    if request.method == 'POST':
        years = request.form.getlist('years')
        fig = graphs.plot_pie('TP_DROGA', years)

    return render_template('droga.html', plot=fig.to_html())

@app.route('/local', methods=['GET', 'POST'])
def local():
    fig = graphs.plot_pie('LOC_REALIZ')

    if request.method == 'POST':
        years = request.form.getlist('years')
        fig = graphs.plot_pie('LOC_REALIZ', years)

    return render_template('local.html', plot=fig.to_html())

@app.route('/procedimento', methods=['GET', 'POST'])
def procedimento():
    fig = graphs.plot_pie('PA_PROC_ID')

    if request.method == 'POST':
        years = request.form.getlist('years')
        fig = graphs.plot_pie('PA_PROC_ID', years)

    return render_template('procedimento.html', plot=fig.to_html())

if __name__ == '__main__':
    app.run(debug=True)