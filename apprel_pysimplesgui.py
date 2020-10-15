import PySimpleGUI as sg

def troca(self):
    if self:
        self = 'Sim'
    else:
        self = 'Não'
    return self

class TelaPython:
    def __init__(self):
        sg.change_look_and_feel('DarkTeal7')
        # layout
        layout = [
            [sg.Text('Nome          ',size=(15,0)),sg.Input(size=(15,0),key='Nome')],
            [sg.Text('Idade         ',size=(15,0)),sg.Input(size=(15,0),key='Idade')],
            [sg.Text('Email',size=(15,0)),sg.Input(size=(15,0),key='Email')], 
            [sg.Text('Quais são suas principais características entre as listadas abaixo?')],
            [sg.Checkbox('Proativo ',key='Proativo'),sg.Checkbox('Inteligente',key='Inteligente'),sg.Checkbox('Humilde',key='Humilde')],
            [sg.Checkbox('Engraçado',key='Engraçado'),sg.Checkbox('Introvertido   ',key='Introvertido'),sg.Checkbox('Líder',key='Líder')],
            [sg.Text('Procura amigos?')],
            [sg.Radio('Sim','Amigos',key='simProcura'),sg.Radio('Não','Amigos',key='naoProcura')],
            [sg.Button('Enviar dados')],
            [sg.Output(size=(50,20))]
        ]
        # janela
        self.janela = sg.Window("Dados do usuário").layout(layout)

    def Iniciar(self):
        while True:
            # extrair os dados da tela
            self.button, self.values = self.janela.Read()
            Nome = self.values['Nome']
            Idade = self.values['Idade']
            Palavras_chave = self.values['pChave']
            Proativo = self.values['Proativo']
            Inteligente = self.values['Inteligente']
            Humilde = self.values['Humilde']
            Engraçado = self.values['Engraçado']
            Introvertido = self.values['Introvertido']
            Líder = self.values['Líder']
            ProcuraAmigos = self.values['simProcura']
            print(f'Nome: {Nome}')
            print(f'Idade: {Idade}')
            print(f'Palavra chave: {Palavras_chave}')
            Proativo = troca(Proativo)
            print(f'Proativo: {Proativo}')
            Inteligente = troca(Inteligente)
            print(f'Inteligente: {Inteligente}')
            Humilde = troca(Humilde)
            print(f'Humilde: {Humilde}')
            Engraçado = troca(Engraçado)
            print(f'Cheiroso: {Engraçado}')
            Introvertido = troca(Introvertido)
            print(f'Parceiro: {Introvertido}')
            Líder = troca(Líder)
            print(f'Líder: {Líder}')
            ProcuraAmigos = troca(ProcuraAmigos)
            print(f'Procura amigos: {ProcuraAmigos}')

tela = TelaPython()
tela.Iniciar()