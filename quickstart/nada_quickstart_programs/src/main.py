from nada_dsl import *

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if len(self.stack) == 0:
            return None  # or raise an exception
        return self.stack.pop()

def nada_main():
    # Define the parties involved
    party1 = Party(name="Party1")
    party2 = Party(name="Party2")
    party3 = Party(name="Party3")
    
    # Define secret inputs for the stack operations from each party
    push_values = [
        SecretInteger(Input(name="push1", party=party1)),
        SecretInteger(Input(name="push2", party=party2)),
        SecretInteger(Input(name="push3", party=party3))
    ]
    
    # Initialize the stack
    stack = Stack()
    
    # Perform stack operations
    for value in push_values:
        stack.push(value)
    
    # Perform pop operations
    pop1 = stack.pop()
    pop2 = stack.pop()
    pop3 = stack.pop()
    
    # Output the popped values to Party3
    return [
        Output(pop1, "pop1_output", party3),
        Output(pop2, "pop2_output", party3),
        Output(pop3, "pop3_output", party3)
    ]
