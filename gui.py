from tkinter import Tk, Frame, Label, Button, filedialog, messagebox, Listbox, Text, TOP, LEFT, BOTH, END

from nfa import NFA

COLOR_PRIMARY = '#3d7eff'
COLOR_SECONDARY = '#ff8b17'
COLOR_WHITE = '#ffffff'
COLOR_BLACK = '#000000'

FORMAT_FILE_MESSAGE = """File văn bản gồm các dòng sau:
1. Tập các trạng thái, mỗi trạng thái cách nhau 1 dấu cách
2. Tập các ký tự, mỗi ký tự cách nhau 1 dấu cách
3. Trạng thái bắt đầu
4. Tập các trạng thái kết thúc, mỗi trạng thái cách nhau 1 dấu cách
5. Các dòng còn lại là danh sách các hàm sinh
    Với mỗi dòng:
        - Ký tự đầu là trạng thái
        - Ký tự thứ 2 là nhãn
        - Các ký tự còn lại là tập các trạng thái khi đọc vào nhãn

Ghi chú: Ký hiệu " thay thế cho epsilon
"""


class GUI:
    nfa = None

    def __init__(self) -> None:
        self.window = Tk()

        self.frame = Frame(self.window)
        self.top_frame = Frame(self.frame)
        self.body_frame = Frame(self.frame)
        self.test_frame = Frame(self.frame)

        self.open_file_button = Button(self.top_frame)

        self.states_list = Frame(self.body_frame)
        self.alphabet_list = Frame(self.body_frame)
        self.accept_states_list = Frame(self.body_frame)
        self.start_state = Frame(self.body_frame)
        self.function_list = Frame(self.body_frame)

        self.string_input = Text(self.test_frame)
        self.test_button = Button(self.test_frame)

        self.config_title()
        self.config_frame()
        self.config_open_file_button()
        self.config_list()
        self.config_test()

        self.config_window()

    def config_frame(self):
        self.frame.pack(side=TOP)
        self.frame.config(width=800, height=600, bg=COLOR_WHITE)

        self.top_frame.pack(side=TOP)
        self.top_frame.config(width=600, pady=10, bg=COLOR_WHITE)

        self.body_frame.pack(side=TOP)
        self.body_frame.config(width=600, pady=10, bg=COLOR_WHITE)

        self.test_frame.pack(side=TOP)
        self.test_frame.config(width=600, pady=10, bg=COLOR_WHITE)

    def config_title(self):
        Label(self.frame, text='eNFA Programing', bg=COLOR_PRIMARY,
              fg=COLOR_WHITE, pady=10, width=800, font=('Arial', 17)).pack(side=TOP)

    def config_open_file_button(self):
        self.open_file_button.pack(side=LEFT, fill=BOTH)
        self.open_file_button.config(
            text="Nhập văn phạm", bg=COLOR_SECONDARY, borderwidth=0, fg=COLOR_WHITE, padx=10, pady=10, command=self.open_file)

        Button(self.top_frame, text="?", padx=10, pady=10,
               bg=COLOR_BLACK, fg=COLOR_WHITE, borderwidth=0, command=self.show_file_format).pack(side=LEFT)

    def config_list(self):
        self.states_list.pack(side=LEFT)
        self.alphabet_list.pack(side=LEFT)
        self.start_state.pack(side=LEFT)
        self.accept_states_list.pack(side=LEFT)
        self.function_list.pack(side=LEFT)

        Label(self.states_list, text="Các trạng thái",
              padx=5, pady=5).pack(side=TOP)

        self.states_listbox = Listbox(self.states_list)
        self.states_listbox.pack(side=TOP)

        Label(self.alphabet_list, text="Các ký tự",
              padx=5, pady=5).pack(side=TOP)

        self.alphabet_listbox = Listbox(self.alphabet_list)
        self.alphabet_listbox.pack(side=TOP)

        Label(self.accept_states_list, text="Các trạng thái kết thúc",
              padx=5, pady=5).pack(side=TOP)

        self.accept_states_listbox = Listbox(self.accept_states_list)
        self.accept_states_listbox.pack(side=TOP)

        Label(self.start_state, text="Trạng thái bắt đầu",
              padx=5, pady=5).pack(side=TOP)

        self.start_state_listbox = Listbox(self.start_state)
        self.start_state_listbox.pack(side=TOP)

        Label(self.function_list, text="Hàm chuyển trạng thái",
              padx=5, pady=5).pack(side=TOP)

        self.function_listbox = Listbox(self.function_list)
        self.function_listbox.pack(side=TOP)

    def config_test(self):
        Label(self.test_frame, text="Chuỗi cần kiểm tra",
              width=800).pack(side=TOP)

        self.string_input.pack(side=TOP)
        self.string_input.config(height=10)

        self.test_button.pack(side=TOP)
        self.test_button.config(
            text="Kiểm tra", padx=10, pady=10, bg=COLOR_PRIMARY, fg=COLOR_WHITE, command=self.on_test)

    def config_window(self):
        self.window.title('eNFA Program - Dev by Minh Thang & Truc Mai')
        self.window.geometry('800x600')
        self.window.mainloop()

    def open_file(self):
        filename = filedialog.askopenfilename(
            title="Chọn file để nhập văn phạm")

        if not filename:
            return

        file_data = open(filename, 'r').read().split('\n')

        states = set(file_data[0]).difference(' ')
        file_data.pop(0)

        alphabet = set(file_data[0]).difference(' ')
        file_data.pop(0)

        start_state = set(file_data[0]).difference(' ')
        file_data.pop(0)

        accept_states = set(file_data[0]).difference(' ')
        file_data.pop(0)

        tf = dict()

        for func in file_data:
            func = func.split(' ')
            state = func[0]
            label = func[1]
            func.pop(0)
            func.pop(0)
            tf[(state, label)] = set(func)

        self.nfa = NFA(states, alphabet, tf, start_state, accept_states)
        self.update()

    def show_file_format(self):
        messagebox.showinfo(title="Định dạng file",
                            message=FORMAT_FILE_MESSAGE)

    def on_test(self):

        if not self.nfa:
            return messagebox.showwarning('Không thể thực hiện kiểm tra', 'Vui lòng nhập văn phạm trước khi kiểm tra chuỗi')

        def handle_error(error): return messagebox.showerror('Lỗi', error)

        res = self.nfa.run_with_input_list(
            self.string_input.get('1.0', END).replace('\n', ''), on_error=handle_error)
        message = ""
        show = messagebox.showinfo

        if res:
            message += "Chuỗi được chấp nhận bởi NFAe"
        else:
            message += "Chuỗi không được chấp nhận bởi NFAe"
            show = messagebox.showwarning

        show(title="Kiểm tra chuỗi", message=message)
        pass

    def update(self):
        self.states_listbox.delete(0, self.states_listbox.size())

        for state in self.nfa.states:
            self.states_listbox.insert(0, state)

        self.alphabet_listbox.delete(0, self.alphabet_listbox.size())

        for alp in self.nfa.alphabet:
            self.alphabet_listbox.insert(0, alp)

        self.accept_states_listbox.delete(0, self.accept_states_listbox.size())

        for state in self.nfa.accept_states:
            self.accept_states_listbox.insert(0, state)

        self.start_state_listbox.delete(0, self.start_state_listbox.size())

        for state in self.nfa.start_state:
            self.start_state_listbox.insert(0, state)

        self.function_listbox.delete(0, self.function_listbox.size())

        for key in self.nfa.transition_function.keys():
            self.function_listbox.insert(
                0, str(key) + " -> " + str(self.nfa.transition_function[key]))


if __name__ == "__main__":
    gui = GUI()
