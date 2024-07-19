from nada_dsl import *

def nada_main():
    # Define the parties involved
    party1 = Party(name="Party1")
    party2 = Party(name="Party2")
    party3 = Party(name="Party3")
    party4 = Party(name="Party4")
    
    # Define secret inputs from each party
    a = SecretInteger(Input(name="A", party=party1))
    b = SecretInteger(Input(name="B", party=party2))
    c = SecretInteger(Input(name="C", party=party3))

    # Perform computations
    sum_result = a + b
    product_result = sum_result * c

    # Output the results to Party4
    return [
        Output(sum_result, "sum_output", party4),
        Output(product_result, "product_output", party4)
    ]
