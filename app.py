import PySimpleGUI as sg

def criar_nova_inicial():
    sg.theme('Reddit')
    linha = [
        [sg.Checkbox(''), sg.Input('')]
    ]
    layoutt = [
        [sg.Frame('Tarefas', font='Any 11', title_color='Black', layout=linha, key='container')],
        [sg.Button('Nova Tarefa'), sg.Button('Resetar')],
    ]
    
    return sg.Window('Todo List', layout=layoutt, finalize=True)

janela = criar_nova_inicial()

while True:
    event, values = janela.read()
    if event == sg.WIN_CLOSED: 
        break
    elif event == 'Nova Tarefa':
        janela.extend_layout(janela['container'], [[sg.Checkbox(''), sg.Input('')]])
    elif event == 'Resetar':
        janela.close()
        janela = criar_nova_inicial()
