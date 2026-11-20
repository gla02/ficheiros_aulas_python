import PySimpleGUI as sg

text1 = sg.popup_get_text('Por favor escreva: ')
print(text1)

text2 = sg.popup_get_text('Não escreva: ')
print(text2)

path = sg.popup_get_file('Select a file')
print(path)

for i in range(1000):
    sg.one_line_progress_meter(
        'progress_bar',
        i + 1,
        1000,
        'barra de progresso',
        'this bar moves from the bottom up',
    )

for i in range(1, 1000):
    sg.one_line_progress_meter(
        'progress_bar',
        i + 1,
        1000,
        'barra de progresso',
        'this bar moves from left to right',
        orientation='h',
        bar_color=("#202222", "#A0B489")
    )

sg.popup(
    'window',
    title='Hello',
    button_color=("#DADCE2", "#880707"),
    background_color="#F4E664",
    line_width=2,
    custom_text='texto'
)

text = "こんにちは"
sg.popup_scrolled(text,title='Hello')

sg.popup("Hello people")
sg.popup('Attention!')
sg.popup_ok('元気ですか?')
sg.popup_yes_no('Please answer yes or no')
sg.popup_cancel('Click on Cancelled')
sg.popup_ok_cancel('Click on OK or Cancel')
sg.popup_error('This Computer is about to explode!!')
sg.popup_auto_close('This window will close in a few seconds')

text = sg.popup_get_text('Password:', password_char='🤖')
sg.popup(f'Password:{text}')

class TelaPython:
    def __init__(self):
        #Layout
        Layout = [
        [sg.Text('Name'),sg.Input()],
        [sg.Text('Age'),sg.Input()],
        [sg.Button('Send data')]
        ]

        #Janela
        janela = sg.Window("User data").layout(Layout)

        #Extrair os dados da Tela
        self.button, self.values = janela.Read()
    
    def Iniciar(self):
        print(self.values)


tela = TelaPython()
tela.Iniciar()