from flask import Flask, render_template, request, flash, redirect, url_for

app = flask(__name__)

app. secret_key = 'sua_chave_secreta'

@app.route('/cadastro', methods=[ 'GET','POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form.get('nome', '').strip()
        email = request,form.get('email', '').strip().lower()

        if not name :
            flash('O nome é obrigatorio.', 'erro')
            return redirect(url_for('cadastro'))
        if not email:
            flash('O e-mail é obrigatorio.', 'erro')
            return redirect(url_for('cadastro')-