# NFA

```py
class NFA:
    current_state = None

    def __init__(self, states, alphabet, transition_function, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transition_function = transition_function
        self.start_state = start_state
        self.accept_states = accept_states

    def transition_with_input(self, input_value):
        result = set()
        for item in self.current_state:
            if (item, input_value) not in self.transition_function.keys():
                continue
            else:
                result = result | self.transition_function[(item, input_value)]

        self.current_state = result

    def in_accept_state(self):
        return self.current_state & self.accept_states

    def goto_initial_state(self):
        self.current_state = self.start_state

    def run_with_input_list(self, input_list):
        self.goto_initial_state()
        print("Trang thai bat dau la: ", self.current_state)
        print("Chuoi can kiem tra la: ", input_list)

        for inp in input_list:
            if inp not in self.alphabet:
                print("Ton tai ky tu khong thuoc bo chu cai")
                return
            else:
                self.transition_with_input(inp)

        return self.in_accept_state()


states = {0, 1, 2, 3, 4}
alphabet = {'0', '1'}
start_state = {0}
accept_state = {2, 4}
tf = dict()

tf[(0, '0')] = {0, 3}
tf[(0, '1')] = {0, 1}
tf[(1, '1')] = {2}
tf[(2, '0')] = {2}
tf[(2, '1')] = {2}
tf[(3, '0')] = {4}
tf[(4, '0')] = {4}
tf[(4, '1')] = {4}

nfa = NFA(states, alphabet, tf, start_state, accept_state)

text = str(input("Nhap vao chuoi can kiem tra: "))

print("Cac trang thai cua chuoi nam trong tap trang thai ket thuc la: ",
      nfa.run_with_input_list(text))
```
