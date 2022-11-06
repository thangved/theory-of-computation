EPSILON = '"'


class NFA:
    current_state = None

    def __init__(self, states: set, alphabet: set, transition_function: dict, start_state, accept_states: set):
        self.states = states
        self.alphabet = alphabet
        self.transition_function = transition_function
        self.start_state = start_state
        self.accept_states = accept_states

    def transition_with_input(self, current_state: set, input_value):
        result = set()
        for item in current_state:
            if (item, input_value) not in self.transition_function.keys():
                continue
            else:
                result = result | self.transition_function[(item, input_value)]

        return result

    def in_accept_state(self):
        return self.current_state & self.accept_states

    def goto_initial_state(self):
        self.current_state = self.start_state

    def run_with_input_list(self, input_list: str, on_error: lambda e: None):
        self.goto_initial_state()

        current_states = set()

        for state in self.current_state:
            current_states = self.eCLOSURE(state)

        for inp in input_list:
            if inp not in self.alphabet:
                on_error("Ký tự '" + inp + "' không thuộc bộ chữ cái")
                return

            res = set()

            next_states = self.transition_with_input(current_states, inp)

            for state in next_states:
                res |= self.eCLOSURE(state)

            current_states = res

        self.current_state = current_states

        return self.in_accept_state()

    def eCLOSURE(self, state):
        result = set()

        stack = []
        stack.append(state)

        while stack:
            top = stack.pop()
            if top in result:
                continue

            result |= {top}

            if (top, EPSILON) in self.transition_function.keys():
                res = self.transition_function[(top, '"')]
                for e in res:
                    stack.append(e)

        return result


# states = {0, 1, 2, 3, 4}
# alphabet = {'0', '1'}
# start_state = {0}
# accept_state = {2, 4}
# tf = dict()

# tf[(0, '0')] = {0, 3}
# tf[(0, '1')] = {0, 1}
# tf[(1, '1')] = {2}
# tf[(2, '0')] = {2}
# tf[(2, '1')] = {2}
# tf[(3, '0')] = {4}
# tf[(4, '0')] = {4}
# tf[(4, '1')] = {4}
