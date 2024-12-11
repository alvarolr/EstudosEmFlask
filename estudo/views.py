from estudo import app
from flask import render_template, request, redirect, url_for, jsonify
import datetime



itens = []

@app.route('/anonovo/')
def segundapagina():
    agora = datetime.datetime.now()
    return render_template('segundapagina.html', anonovo = agora.month == 1 and agora.day == 1)

@app.route('/', methods=['GET', 'POST'])
def homepage():
    if request.method == 'POST':
        # Obtém o item enviado pelo formulário
        novo_item = request.form.get('item')
        if novo_item:
            itens.append(novo_item)
    
    # Renderiza o template HTML, passando a lista de itens
    return render_template('index.html', itens=itens)


@app.route('/delete/<int:index>', methods=['POST'])
def delete_item(index):
    if index >= 0 and index < len(itens):
        itens.pop(index)
    return redirect(url_for('homepage'))


