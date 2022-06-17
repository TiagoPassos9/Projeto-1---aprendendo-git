import PySimpleGUI as sg

def test():
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Sair':
            break
        elif event == 'Calcular' and values['opc'] == '+':
            total = float(values['input1']) + float(values['input2'])
            window['display'].update(total)
        elif event == 'Calcular' and values['opc'] == '-':
            total = float(values['input1']) - float(values['input2'])
            window['display'].update(total)
        elif event == 'Calcular' and values['opc'] == '*':
            total = float(values['input1']) * float(values['input2'])
            window['display'].update(total)
        elif event == 'Calcular' and values['opc'] == '/':
            total = float(values['input1']) / float(values['input2'])
            window['display'].update(total)
        elif values['opc'] or values['opc'] == '':
            window['display'].update('Escolha uma operação válida')

sg.theme('Dark')

layout = [
    [sg.Text('', key='display')],
	[sg.Text('Primeiro número: '),sg.Input(''.replace(',','.'), size=7, key='input1')],
	[sg.Text('Segundo número:'),sg.Input(''.replace(',','.'), size=7, key='input2')],
	[sg.Text('Operação:'), sg.Combo(['+','-','*','/'], key='opc'),sg.Button('Calcular')],
]

window = sg.Window('Calculadora', layout)
test()
