#! python

# first task
def stat(alphab):
    def result(sequence):
        stat_table = {}
        for f in alphab:
            count = 0
            for i in sequence:
                if f == i:
                    count += 1
            perc = round(count / len(sequence), 3)
            stat_table[f] = perc
        return stat_table
    return result


# check
alphab = ['A', 'T', 'C', 'G',]
seq = 'ATTCGCCTGAAGACTCAGAGGCTAAAT'
func = stat(alphab)
func(seq)


# replacement (second task)
def rule_of_replacement(symbol):
    fromm = ['A', 'T', 'C', 'G',]
    to = ['T', 'A', 'G', 'C']
    str = ''
    if symbol in fromm:
        ind = fromm.index(symbol)
        str += to[ind]
    if symbol not in fromm:
        str += symbol
    return str


def replacement(func_r, sequence):
    new_seq = ''
    for f in sequence:
        new_seq += func_r(f)
    return new_seq

# check
seq = 'ATTCGCCTGAAGACTCAGAGGCTAAAT'
replacement(rule_of_replacement,seq)


# modified replacement (third task)
def rule_of_replacement2(symbol):
    fromm = ['AG', 'AC', 'AT', 'AA', 'TT', 'TC', 'TG', 'TA', 'CT', 'CC', 'CA', 'CG', 'GG', 'GC', 'GA', 'GT']
    to = ['T', 'A', 'G', 'C', 'T', 'A', 'G', 'C', 'T', 'A', 'G', 'C', 'T', 'A', 'G', 'C']
    str_ = ''
    if symbol in fromm:
        ind = fromm.index(symbol)
        str_ += to[ind]
    if symbol not in fromm:
        str_ += symbol
    return str_


def replacement2(func_r, sequence):
    new_seq = sequence[0]
    j, i = 0, 2
    while i < len(sequence):
        new_seq += func_r(sequence[j:i])
        j += 1
        i += 1
    return new_seq


# check
seq = 'ATTCGCCTGAAGACTCAGAGGCTAAAT'
replacement2(rule_of_replacement2,seq)