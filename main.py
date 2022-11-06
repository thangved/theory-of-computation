from tkinter import *
from tkinter import messagebox, filedialog

from classes.nfa import NFA
from constants import *


class GUI:
    nfa = None

    def __init__(self):
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
        self.frame.config(
            width=WINDOW_INIT_WIDTH,
            height=WINDOW_INIT_HEIGHT, bg=COLOR_WHITE
        )

        self.top_frame.pack(side=TOP)
        self.top_frame.config(
            width=WINDOW_INIT_HEIGHT,
            pady=10, bg=COLOR_WHITE
        )

        self.body_frame.pack(side=TOP)
        self.body_frame.config(
            width=WINDOW_INIT_HEIGHT,
            pady=10, bg=COLOR_WHITE
        )

        self.test_frame.pack(side=TOP)
        self.test_frame.config(
            width=WINDOW_INIT_HEIGHT,
            pady=10, bg=COLOR_WHITE
        )

    def config_title(self):
        Label(
            self.frame, text='NFAε Programing', bg=COLOR_PRIMARY,
            fg=COLOR_WHITE, pady=10, width=WINDOW_INIT_WIDTH, font=('Arial', 17)
        ).pack(side=TOP)

    def config_open_file_button(self):
        self.open_file_button.pack(side=LEFT, fill=BOTH)
        self.open_file_button.config(
            text="Nhập văn phạm", bg=COLOR_SECONDARY, borderwidth=0, fg=COLOR_WHITE, padx=10, pady=10, command=self.open_file)

        Button(
            self.top_frame, text="?", padx=10, pady=10,
            bg=COLOR_BLACK, fg=COLOR_WHITE, borderwidth=0, command=self.show_file_format
        ).pack(side=LEFT)

    def config_list(self):
        self.states_list.pack(side=LEFT)
        self.alphabet_list.pack(side=LEFT)
        self.start_state.pack(side=LEFT)
        self.accept_states_list.pack(side=LEFT)
        self.function_list.pack(side=LEFT)

        Label(
            self.states_list, text=STATES,
            padx=5, pady=5
        ).pack(side=TOP)

        self.states_listbox = Listbox(self.states_list)
        self.states_listbox.pack(side=TOP)

        Label(
            self.alphabet_list, text=ALPHABETS,
            padx=5, pady=5
        ).pack(side=TOP)

        self.alphabet_listbox = Listbox(self.alphabet_list)
        self.alphabet_listbox.pack(side=TOP)

        Label(
            self.accept_states_list, text=ACCEPT_STATES,
            padx=5, pady=5
        ).pack(side=TOP)

        self.accept_states_listbox = Listbox(self.accept_states_list)
        self.accept_states_listbox.pack(side=TOP)

        Label(
            self.start_state, text=START_STATES,
            padx=5, pady=5
        ).pack(side=TOP)

        self.start_state_listbox = Listbox(self.start_state)
        self.start_state_listbox.pack(side=TOP)

        Label(
            self.function_list, text=TRANSITION_FUNCTIONS,
            padx=5, pady=5
        ).pack(side=TOP)

        self.function_listbox = Listbox(self.function_list)
        self.function_listbox.pack(side=TOP)

    def config_test(self):
        Label(
            self.test_frame, text=STR_NEED_TEST,
            width=WINDOW_INIT_WIDTH
        ).pack(side=TOP)

        self.string_input.pack(side=TOP)
        self.string_input.config(height=10)

        self.test_button.pack(side=TOP)
        self.test_button.config(
            text=CHECK, padx=10, pady=10, bg=COLOR_PRIMARY, fg=COLOR_WHITE, borderwidth=0, command=self.on_test)

    def config_window(self):
        self.window.title(WIN_TITLE)
        self.window.geometry(WINDOW_RESOLUTION)
        self.window.mainloop()

    def open_file(self):
        filename = filedialog.askopenfilename(title=SELECT_FILE_TO_IMPORT_FA)

        if not filename:
            return

        file_data = open(filename, 'r').read().split('\n')

        try:
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
            self.update_lists()
        except:
            messagebox.showerror(READ_FILE_ERROR, FILE_NOT_MATCH_FORMAT)

    def show_file_format(self):
        messagebox.showinfo(title=FILE_FORMAT, message=FORMAT_FILE_MESSAGE)

    def on_test(self):

        if not self.nfa:
            return messagebox.showwarning(CANNOT_TEST, PLEASE_IMPORT_FA)

        def handle_error(error): return messagebox.showerror(ERROR, error)

        res = self.nfa.run_with_input_list(
            self.string_input.get('1.0', END).replace('\n', ''), on_error=handle_error)
        message = ""
        show = messagebox.showinfo

        if res:
            message += FA_ACCEPTED_STR
        else:
            message += FA_NOT_ACCEPT_STR
            show = messagebox.showwarning

        show(title=CHECK_STR, message=message)
        pass

    def update_lists(self):

        def func_to_str(key):
            return str(key) + " -> " + str(self.nfa.transition_function[key])

        self.update_list(self.nfa.states, self.states_listbox)
        self.update_list(self.nfa.alphabet, self.alphabet_listbox)
        self.update_list(self.nfa.accept_states, self.accept_states_listbox)
        self.update_list(self.nfa.start_state, self.start_state_listbox)
        self.update_list(self.nfa.transition_function, self.function_listbox)
        self.update_list(
            self.nfa.transition_function.keys(),
            self.function_listbox, func_to_str
        )

    def update_list(self, data: list, listbox: Listbox, get_data=lambda item: item):
        listbox.delete(0, listbox.size())

        for item in data:
            listbox.insert(0, get_data(item))


if __name__ == "__main__":
    gui = GUI()
