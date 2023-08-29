from tkinter import Tk, Label, Entry, Button
import datetime

parciais = [1.50, 1.75, 2.00]


def convert_duracao(seconds):  # Função para converter o tempo informado em segundos
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    return "%d:%02d:%02d" % (hour, minutes, seconds)


def convert(segundos_totais, hora_inicio, index):
    novo_horario = datetime.timedelta(seconds=segundos_totais) + hora_inicio
    duracao = convert_duracao(segundos_totais)
    return f'Com {parciais[index]:,.2f} esse curso vai durar {duracao} e terminar às {novo_horario.strftime("%H:%M")}'


def calcular():  # Calcular as parciais

    minutos = int(min_entry.get())
    segundos = int(seg_entry.get())

    seg_totais = (minutos * 60) + segundos  # cria a quantidade total de segundos do tempo de curso

    novos_segundos = []
    for item in range(0, parciais.__len__()):  # cria uma lista com os segundos de cada opção de velocidade
        novos_segundos.append(seg_totais / parciais[item])

    hora = datetime.datetime.now()  # captura o horário do sistema

    retorno = ''
    for item in range(0, parciais.__len__()):
        retorno = retorno + (convert(novos_segundos[item], hora, item) + '\n')

    txt_resultado['text'] = retorno


if __name__ == '__main__':
    window = Tk()
    window.title("Cálculo de Tempo de Curso")
    window.config(padx=80, pady=100)

    # Labels
    min_label = Label(text="Tempo em minutos:")
    min_label.grid(row=2, column=0)

    seg_label = Label(text="Tempo em segundos:")
    seg_label.grid(row=4, column=0)

    # Entries
    min_entry = Entry(width=3)
    min_entry.grid(row=2, column=1, columnspan=2)

    seg_entry = Entry(width=3)
    seg_entry.grid(row=4, column=1, columnspan=2)

    min_entry.focus()
    calcula_button = Button(text="CALCULAR", width=10, command=calcular)
    calcula_button.grid(row=5, column=1, columnspan=1)

    txt_resultado = Label(text='')
    txt_resultado.grid(column=0, row=20, columnspan=2)

    window.mainloop()
