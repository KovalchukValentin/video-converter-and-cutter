import tkinter as tk
from tkinter import filedialog
import tkinter.ttk as ttk
import os

from services import Color


class VideoConverterApp:
    def __init__(self):
        self.root = tk.Tk()
        self.color = Color()
        self.path_output = ''
        self.list_format = ['avi', 'gif']
        self.util_ffmpeg_path = f'{os.path.dirname(os.path.abspath(__file__))}/ffmpeg/bin/ffmpeg.exe'

        self.configure()

    def configure(self):
        self.root.configure(bg=self.color.app)
        self.root.resizable(False, False)
        self.root.geometry('585x500')
        self.root.title('Video Converter Developed by Valentin Kovalchuk')

    def add_GUI(self):
        lb_info = tk.Label(text='Select one or multiple files:', bg=self.color.app)
        lb_info.place(y=10, x=10)

        bt_input = tk.Button(self.root, text='   ...   ', command=self.open_dialog_window_for_input_files,
                             bg=self.color.btn)
        bt_input.place(y=10, x=207)

        self.txt = tk.Text(width=70, state='disable', bg=self.color.textfield)
        self.txt.place(y=80, x=10)

        lb_output = tk.Label(text='Select a directory for saving files:', bg=self.color.app)
        lb_output.place(y=10, x=300)

        bt_output = tk.Button(self.root, text='   ...   ', command=self.open_dialog_window_for_output_path,
                              bg=self.color.btn)
        bt_output.place(y=10, x=535)

        self.lb_format_info = tk.Label(text='Choose the output format:', bg=self.color.app)
        self.lb_format_info.place(y=40, x=10)

        self.list_format_file = ttk.Combobox(self.root,
                                             values=self.list_format,
                                             height=3, state='readonly')
        self.list_format_file.current(0)
        self.list_format_file.place(y=40, x=250)

        self.bt_convert = tk.Button(self.root, text='Convert', command=self.convert, state='disable',
                                    bg=self.color.btn)
        self.bt_convert.place(y=40, x=487)

    def run(self):
        self.add_GUI()
        self.root.mainloop()

    def open_dialog_window_for_input_files(self):
        '''
            Opens a dialog window to select input files
        '''

        fd = tk.filedialog.askopenfilenames(title="Choose media files",
                                            multiple=True)
        if not fd:
            return

        self.txt.config(state='normal')
        self.txt.delete(1.0, 'end')
        for i in fd:
            self.txt.insert('end', i + '\n')
            if self.path_output == '':
                self.path_output = os.path.dirname(i)
        self.txt.insert('end', '\nEnd of the list\n')
        self.txt.config(state='disable')
        self.bt_convert.config(state='normal')

    def open_dialog_window_for_output_path(self):
        '''
            Opens a dialog window to select the output path for saving files
        '''
        self.path_output = tk.filedialog.askdirectory(title='Select a directory to save files')
        self.txt.config(state='normal')
        self.txt.insert('end', '\n' + 'Save to: ' + '\n' + self.path_output + '\n')
        self.txt.config(state='disable')

    def convert(self):
        '''
            Performs conversion
        '''

        if not os.path.isfile(self.util_ffmpeg_path):
            self.txt.config(state='normal')
            self.txt.insert('end', '\n' + f'File not found: {self.util_ffmpeg_path}')
            self.txt.insert('end', '\nMake sure it is available.')
            self.txt.config(state='disable')
            return

        for i in self.txt.get(1.0, 'end').split('\n'):
            if i:
                output_file = (self.path_output
                               + '/' + os.path.basename(i).rsplit('.', 1)[0]
                               + '.' + self.list_format_file.get())
                self.txt.config(state='normal')
                self.txt.tag_add(i, 1.0, 'end')
                self.txt.tag_config(i, background=self.color.done, underline=1)

                try:
                    os.system(self.util_ffmpeg_path + ' -i ' + i + ' ' + output_file)
                except:
                    self.txt.insert('end', '\nOops! Unable to convert the file: ')
                    self.txt.insert('end', '\n' + i)
            else:
                break
        self.txt.insert('end', '\nOperation completed')
        self.txt.config(state='disable')