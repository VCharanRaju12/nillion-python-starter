from nada_dsl import *

class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

def insert(head, data):
    new_node = Node(data)
    if not head:
        return new_node
    current = head
    while current.next:
        current = current.next
    current.next = new_node
    return head

def print_linked_list(head, party):
    current = head
    index = 0
    outputs = []
    while current:
        outputs.append(Output(current.data, f"node_{index}", party))
        current = current.next
        index += 1
    return outputs

def nada_main():
    # Define the parties involved
    party1 = Party(name="Party1")
    party2 = Party(name="Party2")
    party3 = Party(name="Party3")
    
    # Define secret inputs for the linked list nodes from each party
    node1 = SecretInteger(Input(name="node1", party=party1))
    node2 = SecretInteger(Input(name="node2", party=party2))
    node3 = SecretInteger(Input(name="node3", party=party3))
    node4 = SecretInteger(Input(name="node4", party=party1))
    
    # Insert nodes into the linked list
    head = None
    head = insert(head, node1)
    head = insert(head, node2)
    head = insert(head, node3)
    head = insert(head, node4)
    
    # Output the linked list nodes to Party3
    outputs = print_linked_list(head, party3)
    return outputs
