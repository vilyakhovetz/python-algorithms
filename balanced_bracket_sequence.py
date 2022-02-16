def is_bracket_sequence_balanced(seq):
    """
    Function to check if a bracket sequence is balanced
    Returns True if given sequence is balanced.
    """
    brackets = {')': '(', ']': '[', '}': '{'}
    opened = []
    for br in seq:
        if br in ['(', '[', '{']:
            opened.append(br)
        elif opened and brackets[br] != opened.pop():
            return False
    return len(opened) == 0


if __name__ == '__main__':
    my_seq1 = '([{}])'
    print(is_bracket_sequence_balanced(my_seq1), '-> True')
    my_seq2 = '([{})'
    print(is_bracket_sequence_balanced(my_seq2), '-> False')
    my_seq3 = '({[}])'
    print(is_bracket_sequence_balanced(my_seq3), '-> False')
    my_seq4 = '()[]{}'
    print(is_bracket_sequence_balanced(my_seq4), '-> True')
    my_seq5 = ''
    print(is_bracket_sequence_balanced(my_seq5), '-> True')
