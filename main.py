from flask import Flask, render_template, request
from services.managerDB import *


app = Flask(__name__)


@app.route('/', methods=['get', 'post'])
def index():
    mensagem = ''
    item = []
    func = ''
    
    # adciona tarefas a tela
    for listitem in loadInfo():
        item.append(dict(listitem))
    
    # se a pagina for solicitada em metodo 'post' >> tarefa foi adcionada
    if request.method == 'POST':
        task = request.form['task']
        AddInfo(task)
        
        mensagem = ''
        func = 'showMsg("event")'
    
    # caso o motodo seja 'GET
    elif request.method == 'GET':
        func = ''
        # obtem os argumentos passados na URL
        args = request.args

        # cao exista args
        if args:
            if 'del_item' in args.keys():
                delete(args['del_item'])
                mensagem = f'Item removido com sucesso!'
            
            elif 'change_item' in args.keys():
                updateCheck(args['change_item'])
                print(updateCheck)
                mensagem = 'Tarefa realizada com sucesso'
            
            func = 'showMsg("event")'
    
    return render_template('index.html', loadF=item, msg=mensagem, func=func)
    


app.run(debug=True)