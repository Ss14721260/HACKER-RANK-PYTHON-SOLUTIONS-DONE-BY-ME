def mutate_string(string, position, character):
    p=list(string)
    p[position]=character
    return "".join(p)

