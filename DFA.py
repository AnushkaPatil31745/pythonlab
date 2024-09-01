class DFA:
    def _init_(self):
        self.current_state = 'q0'
    
    def transition(self, input_char):
        if self.current_state == 'q0':
            if input_char == 'a':
                self.current_state = 'q0'
            elif input_char == 'b':
                self.current_state = 'q1'
        elif self.current_state == 'q1':
            if input_char == 'a':
                self.current_state = 'q0'
            elif input_char == 'b':
                self.current_state = 'q1'

    def accepts(self, string):
        self.current_state = 'q0'

        for char in string:
            self.transition(char)

        return self.current_state == 'q0'

def test_dfa(string):
    dfa = DFA()
    if dfa.accepts(string):
        return "Accepted"
    else:
        return "Rejected"

print(test_dfa("ab"))  
print(test_dfa("aba"))  
print(test_dfa("bbbbba"))  
print(test_dfa("bbb"))  
