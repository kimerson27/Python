import xlwings, schedule
import time as TM
from apscheduler.schedulers.background import BackgroundScheduler
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from datetime import datetime, timedelta, time


# Глобальные переменные
FilePath = list()
WorkTimer:int=5
scheduler = BackgroundScheduler()
scheduler.start()  # ОБЯЗАТЕЛЬНО: запускаем планировщик при старте программы

def ChooseFile():
    global FilePath
    FilePath = filedialog.askopenfilenames(
        title='Выберите файл',
        filetypes=[
            ('Файлы Excel', '*.xlsx'),
            ('Файлы Excel 97-2003', '*.xls'),
            ('Все файлы', '*.*')
        ]
    )
    if FilePath:
        messagebox.showinfo(title='Файлы выбраны', message=f'Список выбран')
    else:
        messagebox.showwarning(title='Файлы не выбраны', message='Файлы не был выбраны.')

def RefreshFile():
    global WorkTimer
    app = xlwings.App(visible=False)
    if not FilePath:
        messagebox.showerror(title='Ошибка', message='Сначала выберите файлы!')
        return

    try:
        for files in FilePath:
            book = app.books.open(files)
            book.app.api.DisplayAlerts = False
            book.api.RefreshAll()
            app.calculate()
            TM.sleep(WorkTimer)
            book.save()
            book.close()
        app.quit()
            
        
        messagebox.showinfo(title='Успех', message='Файлы успешно обновлёны!')
    except FileNotFoundError:
        messagebox.showerror(title='Ошибка', message='Файлы не найдены. Проверьте путь.')
    except PermissionError:
        messagebox.showerror(title='Ошибка', message='Нет доступа к файлам. Проверьте права.')
    except Exception as e:
        messagebox.showerror(title='Ошибка', message=f'Произошла ошибка:\n{e}')

def StartTimer():
    global minutes
    
    # Запускает таймер с заданными параметрами
    if not FilePath:
        messagebox.showerror(title='Ошибка', message='Выберите файл перед запуском таймера!')
        return

    try:
        # Параметры расписания
        
        
        hoursINF=int(EnteryHours.get())
        StartTime=int(EnteryStart.get())
    
        start_date = datetime.now().replace(hour=StartTime,minute=0,second=0, microsecond=0) + timedelta(minutes=minutes.get())  # Старт через 10 сек
        end_date = datetime.combine(datetime.now().date(),time(hoursINF))       

        scheduler.add_job(
            func=RefreshFile,
            trigger='interval',
            minutes=60,
            start_date=start_date,
            end_date=end_date,
            timezone='Europe/Moscow',
            misfire_grace_time=30,
            coalesce=True,
            max_instances=3,
            id='excel_refresh_job'  # Уникальный ID для управления
        )
        messagebox.showinfo(
            title='Таймер запущен',
            message=f'Обновление каждые 60 мин\n'
                   f'Старт: {start_date.strftime("%H:%M")}\n'
                   f'Конец: {end_date.strftime("%H:%M")}'
        )
    except Exception as e:
        messagebox.showerror(title='Ошибка таймера', message=f'{e}')

def StopTimer():
    # Останавливает таймер
    try:
        scheduler.remove_job('excel_refresh_job')
        messagebox.showinfo(title='Таймер остановлен', message='Расписание отменено.')
    except:
        messagebox.showwarning(title='Нет таймера', message='Таймер не был запущен.')


def on_closing():
    # Обработчик закрытия окна
    if messagebox.askokcancel('Выход', 'Вы уверены, что хотите выйти?'):
        scheduler.shutdown()  # ОБЯЗАТЕЛЬНО: останавливаем планировщик
        window.destroy()

# Создание окна
window = tk.Tk()
window.title('TimerForExcel')
window.resizable (False, False)

#Переменная для RadioButton
minutes = tk.IntVar()
#Создание вкладок
notebook=ttk.Notebook(window)
notebook.grid(column=0,row=0)

#Создание фреймов
tab1=ttk.Frame(notebook)
tab2=ttk.Frame(notebook)


#Добавление вкладок
notebook.add(tab1,text='Главная вкладка')
notebook.add(tab2,text='Список файлов')


#ПЕРВАЯ ВКЛАДКА 
#Строка ввода начала таймера
LabelStart=tk.Label(tab1, text='Введите начальное\n время таймера')
LabelStart.grid(column=1,row=1)
EnteryStart=ttk.Spinbox(tab1, from_=0, to=23, width=10,state="readonly")
EnteryStart.set(8)
EnteryStart.grid(column=1,row=2)

#Строка ввода для end_time
LabelINFO = tk.Label(tab1, text='Введите время\n окончания таймера')
LabelINFO.grid(column=2, row=1)
EnteryHours = ttk.Spinbox(tab1, from_=0, to=23, width=10,state="readonly")
EnteryHours.set(16)
EnteryHours.grid(column=2, row=2)
   

# Кнопки
# Первая вкладка
StartButton = tk.Button(tab1, text='Выбрать файлы', command=ChooseFile, width=20)
StartButton.grid(column=2, row=3, padx=5,pady=5)

RefreshBTN = tk.Button(tab1, text='Обновить файлы', command=RefreshFile, width=20)
RefreshBTN.grid(column=2, row=4, padx=5,pady=5)

TimerBTN = tk.Button(tab1, text='Запустить таймер', command=StartTimer, width=20)
TimerBTN.grid(column=1, row=3, padx=5, pady=5)

StopBTN = tk.Button(tab1, text='Остановить таймер', command=StopTimer, width=20)
StopBTN.grid(column=1, row=4, padx=5, pady=5)

destroy = tk.Button(tab1, text='Закрыть', command=on_closing, width=20)
destroy.grid(column=1, row=5,columnspan=2)

# Вторая вкладка

TextInfo=tk.Text(tab2,wrap='word',width=40,height=10)
TextInfo.grid(column=0,row=0,sticky='nesw')

# Обработчик закрытия окна
window.protocol('WM_DELETE_WINDOW', on_closing)


window.mainloop()