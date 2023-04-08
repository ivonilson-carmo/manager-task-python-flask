import dataset as data_s


def AddInfo(text_t):
    """  acrescenta ao banco de dados uma task(text_t) com o state = 'Em Aberto' """
    
    location_file = 'sqlite:///tasks.db'

    with data_s.connect(location_file) as db:
        db['tasks'].insert(dict( task=text_t, state='Em Aberto' ))
        
    return True


def loadInfo():
    """ Obtem uma lista com as tasks no banco de dados """
    
    location_file = 'sqlite:///tasks.db'

    with data_s.connect(location_file) as db:
        tasks = db['tasks'].all()
    
    return tasks

def delete(item):
    """ Deleta item no banco de dados | item => id da tasks """

    location_file = 'sqlite:///tasks.db'

    with data_s.connect(location_file) as db:
        item = int(item)
        tasks = db['tasks'].delete(id=item)
    
    return True

def updateCheck(item):
    """ Atualiza o status de uma tarefa | item => id da tasks """
    
    location_file = 'sqlite:///tasks.db'

    with data_s.connect(location_file) as db:
        item = int(item)
        item_change = db['tasks'].find_one(id=item)
        item_change['state'] = 'Feito' if item_change['state'] == 'Em Aberto' else 'Aberto'
        db['tasks'].update(item_change, ['id'])

    

