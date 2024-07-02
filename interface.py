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

    fig = graphs.plot_pie('CNES_EXEC', anos=None, sexos=None, estab=None)

    if request.method == 'POST':
        anos = request.form.getlist('years') if request.form.getlist('years') != '' else None
        sexos = request.form.getlist('sexos') if request.form.getlist('sexos') != '' else None
        estab = request.form.getlist('estabelecimentos') if request.form.getlist('estabelecimentos') != '' else None
        
        if request.form['modo'] == 'sum':
            fig = graphs.plot_pie('CNES_EXEC', anos, sexos, estab)
        else:
            fig = graphs.plot_bar_compare('CNES_EXEC', anos, sexos, estab)
    
    return render_template('estabelecimentos.html', plot=fig.to_html())

@app.route('/idades', methods=['GET', 'POST'])
def idades():

    fig = graphs.plot_bar_sum('IDADEPAC', anos=None, sexos=None, estab=None)

    if request.method == 'POST':
        anos = request.form.getlist('years') if request.form.getlist('years') != '' else None
        sexos = request.form.getlist('sexos') if request.form.getlist('sexos') != '' else None
        estab = request.form.getlist('estabelecimentos') if request.form.getlist('estabelecimentos') != '' else None
        
        if request.form['modo'] == 'sum':
            fig = graphs.plot_bar_sum('IDADEPAC', anos, sexos, estab)
        else:
            fig = graphs.plot_bar_compare('IDADEPAC', anos, sexos, estab)

    return render_template('idades.html', plot=fig.to_html())

@app.route('/municipios', methods=['GET', 'POST'])
def municipios():

    fig = graphs.plot_pie('MUNPAC', anos=None, sexos=None, estab=None)

    if request.method == 'POST':
        anos = request.form.getlist('years') if request.form.getlist('years') != '' else None
        sexos = request.form.getlist('sexos') if request.form.getlist('sexos') != '' else None
        estab = request.form.getlist('estabelecimentos') if request.form.getlist('estabelecimentos') != '' else None
        
        if request.form['modo'] == 'sum':
            fig = graphs.plot_pie('MUNPAC', anos, sexos, estab)
        else:
            fig = graphs.plot_bar_compare('MUNPAC', anos, sexos, estab)

    return render_template('municipios.html', plot=fig.to_html())

@app.route('/raca', methods=['GET', 'POST'])
def raca():

    fig = graphs.plot_pie('RACACOR', anos=None, sexos=None, estab=None)

    if request.method == 'POST':
        anos = request.form.getlist('years') if request.form.getlist('years') != '' else None
        sexos = request.form.getlist('sexos') if request.form.getlist('sexos') != '' else None
        estab = request.form.getlist('estabelecimentos') if request.form.getlist('estabelecimentos') != '' else None
        
        if request.form['modo'] == 'sum':
            fig = graphs.plot_pie('RACACOR', anos, sexos, estab)
        else:
            fig = graphs.plot_bar_compare('RACACOR', anos, sexos, estab)

    return render_template('raca.html', plot=fig.to_html())

@app.route('/cid', methods=['GET', 'POST'])
def cid():

    fig = graphs.plot_pie('CIDPRI', anos=None, sexos=None, estab=None)

    if request.method == 'POST':
        anos = request.form.getlist('years') if request.form.getlist('years') != '' else None
        sexos = request.form.getlist('sexos') if request.form.getlist('sexos') != '' else None
        estab = request.form.getlist('estabelecimentos') if request.form.getlist('estabelecimentos') != '' else None
        
        if request.form['modo'] == 'sum':
            fig = graphs.plot_pie('CIDPRI', anos, sexos, estab)
        else:
            fig = graphs.plot_bar_compare('CIDPRI', anos, sexos, estab)

    return render_template('cid.html', plot=fig.to_html())

@app.route('/cobertura', methods=['GET', 'POST'])
def cobertura():

    fig = graphs.plot_pie('COB_ESF', anos=None, sexos=None, estab=None)

    if request.method == 'POST':
        anos = request.form.getlist('years') if request.form.getlist('years') != '' else None
        sexos = request.form.getlist('sexos') if request.form.getlist('sexos') != '' else None
        estab = request.form.getlist('estabelecimentos') if request.form.getlist('estabelecimentos') != '' else None
        
        if request.form['modo'] == 'sum':
            fig = graphs.plot_pie('COB_ESF', anos, sexos, estab)
        else:
            fig = graphs.plot_bar_compare('COB_ESF', anos, sexos, estab)

    return render_template('cobertura.html', plot=fig.to_html())

@app.route('/situacaorua', methods=['GET', 'POST'])
def situacaorua():

    fig = graphs.plot_pie('SIT_RUA', anos=None, sexos=None, estab=None)

    if request.method == 'POST':
        anos = request.form.getlist('years') if request.form.getlist('years') != '' else None
        sexos = request.form.getlist('sexos') if request.form.getlist('sexos') != '' else None
        estab = request.form.getlist('estabelecimentos') if request.form.getlist('estabelecimentos') != '' else None
        
        if request.form['modo'] == 'sum':
            fig = graphs.plot_pie('SIT_RUA', anos, sexos, estab)
        else:
            fig = graphs.plot_bar_compare('SIT_RUA', anos, sexos, estab)

    return render_template('situacaorua.html', plot=fig.to_html())

@app.route('/sexo', methods=['GET', 'POST'])
def sexo():

    fig = graphs.plot_pie('SEXOPAC', anos=None, sexos=None, estab=None)

    if request.method == 'POST':
        anos = request.form.getlist('years') if request.form.getlist('years') != '' else None
        sexos = request.form.getlist('sexos') if request.form.getlist('sexos') != '' else None
        estab = request.form.getlist('estabelecimentos') if request.form.getlist('estabelecimentos') != '' else None
        
        if request.form['modo'] == 'sum':
            fig = graphs.plot_pie('SEXOPAC', anos, sexos, estab)
        else:
            fig = graphs.plot_bar_compare('SEXOPAC', anos, sexos, estab)

    return render_template('sexo.html', plot=fig.to_html())

@app.route('/droga', methods=['GET', 'POST'])
def droga():

    fig = graphs.plot_pie('TP_DROGA', anos=None, sexos=None, estab=None)

    if request.method == 'POST':
        anos = request.form.getlist('years') if request.form.getlist('years') != '' else None
        sexos = request.form.getlist('sexos') if request.form.getlist('sexos') != '' else None
        estab = request.form.getlist('estabelecimentos') if request.form.getlist('estabelecimentos') != '' else None
        
        if request.form['modo'] == 'sum':
            fig = graphs.plot_pie('TP_DROGA', anos, sexos, estab)
        else:
            fig = graphs.plot_bar_compare('TP_DROGA', anos, sexos, estab)

    return render_template('droga.html', plot=fig.to_html())

@app.route('/local', methods=['GET', 'POST'])
def local():

    fig = graphs.plot_pie('LOC_REALIZ', anos=None, sexos=None, estab=None)

    if request.method == 'POST':
        anos = request.form.getlist('years') if request.form.getlist('years') != '' else None
        sexos = request.form.getlist('sexos') if request.form.getlist('sexos') != '' else None
        estab = request.form.getlist('estabelecimentos') if request.form.getlist('estabelecimentos') != '' else None
        
        if request.form['modo'] == 'sum':
            fig = graphs.plot_pie('LOC_REALIZ', anos, sexos, estab)
        else:
            fig = graphs.plot_bar_compare('LOC_REALIZ', anos, sexos, estab)

    return render_template('local.html', plot=fig.to_html())

@app.route('/procedimento', methods=['GET', 'POST'])
def procedimento():

    fig = graphs.plot_pie('PA_PROC_ID', anos=None, sexos=None, estab=None)

    if request.method == 'POST':
        anos = request.form.getlist('years') if request.form.getlist('years') != '' else None
        sexos = request.form.getlist('sexos') if request.form.getlist('sexos') != '' else None
        estab = request.form.getlist('estabelecimentos') if request.form.getlist('estabelecimentos') != '' else None
        
        if request.form['modo'] == 'sum':
            fig = graphs.plot_pie('PA_PROC_ID', anos, sexos, estab)
        else:
            fig = graphs.plot_bar_compare('PA_PROC_ID', anos, sexos, estab)

    return render_template('procedimento.html', plot=fig.to_html())

if __name__ == '__main__':
    app.run(debug=True)