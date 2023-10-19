import tkinter as tk
import tkinter.ttk as ttk
import os

from video_converter import VideoConverterApp


class VideoConverterAndCutterApp(VideoConverterApp):
    def __init__(self):
        super().__init__()
        self.whattodo = ''
        self.crop_points = {'n': 'Don`t change size',
                            'lt': 'Left-top',
                            'c': 'Center',
                            'rt': 'Right-top',
                            'lb': 'Left-bottom',
                            'rb': 'Right-bottom'}

    def configure(self):
        super().configure()
        self.root.geometry('585x550')
        self.root.title('Video Converter And Cutter Developed by Valentin Kovalchuk')

    def add_GUI(self):
        super().add_GUI()

        self.bt_crop = tk.Button(self.root, text='  Crop  ', command=self.change_todo_to_crop,
                                bg=self.color.btn)
        self.bt_crop.place(y=40, x=430)
        self.bt_convert['command'] = self.change_todo_to_convert
        self.bt_convert['state'] = 'normal'
        self.list_format_file['state'] = 'disable'
        self.bt_do = tk.Button(self.root, text=' Confirm  ', command=self.do, state='disable',
                                 bg=self.color.btn)
        self.bt_do.place(y=100, x=487)

        self.add_input_crop_params_GUI()
        self.disable_input_crop_params()

        self.bt_delete_sound = tk.Button(self.root, text='Delete Sound', command=self.change_todo_to_delete_sound,
                               bg=self.color.btn)
        self.bt_delete_sound.place(y=70, x=445)
        self.bt_convert_to_gif_without_dithering = tk.Button(self.root, text='GIF Without Dithering', command=self.change_todo_to_convert_to_gif_without_dithering,
                                         bg=self.color.btn)
        self.bt_convert_to_gif_without_dithering.place(y=70, x=310)

        self.txt.place(y=135, x=10)

    def add_input_crop_params_GUI(self):
        lb_crop_params = tk.Label(text='Crop Parameters:', bg=self.color.app)
        lb_crop_params.place(y=70, x=10)
        tk.Label(text='X=', bg=self.color.app).place(y=100, x=10)
        tk.Label(text='Y=', bg=self.color.app).place(y=100, x=80)
        tk.Label(text='t=', bg=self.color.app).place(y=100, x=150)
        tk.Label(text='sec.', bg=self.color.app).place(y=100, x=203)
        self.input_x = tk.Entry(width=5)
        self.input_x.place(y=100, x=30)
        self.input_y = tk.Entry(width=5)
        self.input_y.place(y=100, x=100)
        self.input_t = tk.Entry(width=5)
        self.input_t.place(y=100, x=170)

        self.list_crop_point = ttk.Combobox(self.root, height=3, state='readonly')
        for v in self.crop_points.values():
            self.list_crop_point['values'] = (*self.list_crop_point['values'], v)
        self.list_crop_point.current(0)
        self.list_crop_point.place(y=100, x=250)
        self.disable_input_crop_params()

    def disable_input_crop_params(self):
        self.list_crop_point['state'] = 'disable'
        self.input_x['state'] = 'disable'
        self.input_x.delete(0, 'end')
        self.input_y['state'] = 'disable'
        self.input_y.delete(0, 'end')
        self.input_t['state'] = 'disable'

    def enable_input_crop_params(self):
        self.list_crop_point['state'] = 'normal'
        self.input_x['state'] = 'normal'
        self.input_x.insert(0, '2')
        self.input_y['state'] = 'normal'
        self.input_y.insert(0, '2')
        self.input_t['state'] = 'normal'

    def change_todo_to_convert(self):
        self.whattodo = 'convert'
        self.change_interface()

    def change_todo_to_crop(self):
        self.whattodo = 'crop'
        self.change_interface()

    def change_todo_to_delete_sound(self):
        self.whattodo = 'delete_sound'
        self.change_interface()

    def change_todo_to_convert_to_gif_without_dithering(self):
        self.whattodo = 'convert_to_gif_without_dithering'
        self.change_interface()

    def change_interface(self):
        if self.whattodo == 'crop':
            self.list_format_file['state'] = 'disable'
            self.bt_crop['state'] = 'disable'
            self.bt_convert['state'] = 'normal'
            self.enable_input_crop_params()
            self.bt_delete_sound['state'] = 'normal'
            self.bt_convert_to_gif_without_dithering['state'] = 'normal'
        elif self.whattodo == 'convert':
            self.list_format_file['state'] = 'normal'
            self.bt_convert['state'] = 'disable'
            self.bt_crop['state'] = 'normal'
            self.disable_input_crop_params()
            self.bt_delete_sound['state'] = 'normal'
            self.bt_convert_to_gif_without_dithering['state'] = 'normal'
        elif self.whattodo == 'delete_sound':
            self.list_format_file['state'] = 'disabled'
            self.bt_convert['state'] = 'normal'
            self.bt_crop['state'] = 'normal'
            self.disable_input_crop_params()
            self.bt_delete_sound['state'] = 'disabled'
            self.bt_convert_to_gif_without_dithering['state'] = 'normal'
        elif self.whattodo == 'convert_to_gif_without_dithering':
            self.list_format_file['state'] = 'disabled'
            self.bt_convert['state'] = 'normal'
            self.bt_crop['state'] = 'normal'
            self.disable_input_crop_params()
            self.bt_delete_sound['state'] = 'normal'
            self.bt_convert_to_gif_without_dithering['state'] = 'disabled'
        else:
            self.list_format_file['state'] = 'disable'
            self.bt_crop['state'] = 'normal'
            self.bt_convert['state'] = 'normal'
            self.disable_input_crop_params()
            self.bt_delete_sound['state'] = 'normal'
            self.bt_convert_to_gif_without_dithering['state'] = 'normal'

        if self.whattodo and self.path_output:
            self.bt_do['state'] = 'normal'
        else:
            self.bt_do['state'] = 'disable'

    def do(self):
        if self.whattodo == 'crop':
            self.crop()
        elif self.whattodo == 'convert':
            self.convert()
        elif self.whattodo == 'delete_sound':
            self.delete_sound()
        elif self.whattodo == 'convert_to_gif_without_dithering':
            self.convert_to_gif_without_dithering()

    def crop(self):
        """Performs cropping on files."""
        command = self.get_crop_command()

        for i in self.txt.get(1.0, 'end').split('\n'):
            if i:
                output_file = f"{self.path_output}/{os.path.basename(i).rsplit('.', 1)[0]}_cropped" \
                              f"{self.input_x.get()}_{self.input_y.get()}" \
                              f"{'' if not self.input_t.get() else f'_t{self.input_t.get()}'}." \
                              f"{os.path.basename(i).rsplit('.', 1)[1]}"

                self.txt.config(state='normal')
                self.txt.tag_add(i, 1.0, 'end')
                self.txt.tag_config(i, background=self.color.done, underline=1)

                try:
                    os.system(f'{self.util_ffmpeg_path} -i {i} {command} {output_file}')
                except:
                    self.txt.insert('end', '\nOops! Unable to crop the file: ')
                    self.txt.insert('end', '\n' + i)
            else:
                break
        self.txt.insert('end', '\nOperation completed')
        self.txt.config(state='disable')

    def get_crop_command(self) -> str:
        '''Generates a command for the program based on specified cropping parameters'''
        x = int(self.input_x.get())
        y = int(self.input_y.get())

        print(self.list_crop_point.get())
        crop_point = [i for i in self.crop_points if self.crop_points[i] == self.list_crop_point.get()][0]
        command = '-y'

        if crop_point == 'n':
            pass
        elif crop_point == 'lt':
            command += f' -vf crop={x}:{y}:0:0'
        elif crop_point == 'c':
            command += f' -vf crop={x}:{y}:in_w/2-{x}/2:in_h/2-{y}/2'
        elif crop_point == 'rt':
            command += f' -vf crop={x}:{y}:in_w-{x}:0'
        elif crop_point == 'lb':
            command += f' -vf crop={x}:{y}:0:in_h-{y}'
        elif crop_point == 'rb':
            command += f' -vf crop={x}:{y}:in_w-{x}:in_h-{y}'

        if self.input_t.get():
            command += f' -t {int(self.input_t.get())}'
        return command

    def open_dialog_window_for_output_path(self):
        super().open_dialog_window_for_output_path()
        self.change_interface()

    def delete_sound(self):
        '''Separates the audio track from the video file.'''
        for i in self.txt.get(1.0, 'end').split('\n'):
            if i:
                output_file = f"{self.path_output}/{os.path.basename(i).rsplit('.', 1)[0]}_without_sound." \
                              f"{os.path.basename(i).rsplit('.', 1)[1]}"

                self.txt.config(state='normal')
                self.txt.tag_add(i, 1.0, 'end')
                self.txt.tag_config(i, background=self.color.done, underline=1)

                try:
                    os.system(f'{self.util_ffmpeg_path} -i {i} -an -c copy {output_file}')
                except:
                    self.txt.insert('end', '\nOops! Unable to remove sound from the file: ')
                    self.txt.insert('end', '\n' + i)
            else:
                break
        self.txt.insert('end', '\nOperation completed')
        self.txt.config(state='disable')

    def convert_to_gif_without_dithering(self):
        '''Converts a video file to a GIF animation without dithering.'''
        for i in self.txt.get(1.0, 'end').split('\n'):
            if i:
                output_file = f"{self.path_output}/{os.path.basename(i).rsplit('.', 1)[0]}_without_dithering.gif"
                output_file_palette = f"{self.path_output}/{os.path.basename(i).rsplit('.', 1)[0]}_palette.png"

                self.txt.config(state='normal')
                self.txt.tag_add(i, 1.0, 'end')
                self.txt.tag_config(i, background=self.color.done, underline=1)
                try:
                    os.system(f'{self.util_ffmpeg_path} -i {i} -vf palettegen {output_file_palette}')
                    os.system(f'{self.util_ffmpeg_path} -i {i} -i {output_file_palette} -filter_complex "[0][1]paletteuse" -y {output_file}')
                except:
                    self.txt.insert('end', '\nOops! Unable to convert the file: ')
                    self.txt.insert('end', '\n' + i)
            else:
                break
        self.txt.insert('end', '\nOperation completed')
        self.txt.config(state='disable')