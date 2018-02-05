def ADD(A, B):
    return A + B


def SUB(A, B):
    return A - B


def SHIFTL(A, B):
    return A * B


def SHIFTR(A, B):
    return A / B


def AND(A, B):
    return (A and B)


def OR(A, B):
    return (A or B)


def sau(opcode, A, B):
    result = {
        0: 'NOP',
        1: ADD(A, B),
        2: SUB(A, B),
        3: SHIFTL(A, B),
        4: SHIFTR(A, B),
        5: AND(A, B),
        6: OR(A, B),
        7: 'NOP'
    }
    return result.get(opcode)
