import tkinter as tk

# создаем окно
window = tk.Tk()
window.title("Какая-то программа")
window.geometry("800x600")

label_usd = tk.Label(window, text='')
label_byn = tk.Label(window, text='')
label_cny = tk.Label(window, text='')
label_usd.pack()
label_byn.pack()
label_cny.pack()

# Функция, которая меняет текст
def change_label_text():
    rub = float(entry.get()) 
    usd = 97.75
    cny = 13.31
    byn = 38.73
    label_usd["text"] = str(round(rub / usd)) + " $(Доллар)"
    label_cny["text"] = str(round(rub / cny)) + " ¥(Юань)"
    label_byn["text"] = str(round(rub / byn)) + " Br(Белорусский рубль)"



# создаем виджет - окно ввода
entry = tk.Entry(window, font="Verdana", width=30)
entry.pack()

# создаем виджет - кнопку
button = tk.Button(window, text="Нажать",background="#00ff00",width="10", command=change_label_text)
button.pack()
    

# Создаем виджет - лейбл
label = tk.Label(window, font="Verdana")
label.pack()


# запускаем окно
window.mainloop()