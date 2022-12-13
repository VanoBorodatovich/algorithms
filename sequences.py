#! python

class Sequences:
    def __init__(self, name, sequence, missing_value):
        self.sequence = sequence
        self.name = name
        self.missing_value = missing_value
        self.rna_amiv_dic = {'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L', 'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L', 'AUU': 'I',
'AUC': 'I', 'AUA': 'I', 'AUG': 'M', 'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V', 'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P', 'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T', 'GCU': 'A', 'GCC': 'A',
'GCA': 'A', 'GCG': 'A', 'UAU': 'Y', 'UAC': 'Y', 'UAA': 'stop', 'UAG': 'stop', 'UGA': 'stop', 'CAU': 'H', 'CAC': 'H', 'CAA': 'Q',
'CAG': 'Q', 'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K', 'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E', 'UGU': 'C', 'UGC': 'C',
'UGG': 'W', 'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R', 'AGA': 'R', 'AGG': 'R', 'AGU': 'S', 'AGC': 'S', 'GGU': 'E', 'GGC': 'E',
'GGA': 'E', 'GGG': 'E'}

    def __str__(self):
      return '>' + self.name + '\n' + self.sequence

    def __len__(self):
        return len(self.sequence)

    def make_bigger(self, fromm, to):
        print('all ' + ''.join(fromm)+ ' will become ' + ''.join(to[0:len(to)-1]))
        str = ''
        for f in self.sequence:
            if f in fromm:
                ind = fromm.index(f)
                str += to[ind]
            if f not in fromm:
                str += f
        return str

    def alphabet(self, alphab):
        unexpected = []
        righ = True
        for f in (self.sequence):
            if f not in alphab:
                righ = False
                unexpected.append(f)
        if unexpected != []:
            print('unexpected symbols:' + ' '.join(unexpected) + '; your sequence will not be accepted')
        return righ

    def stats(self, args):
        stat_table = {}
        for f in args:
            count = 0
            for i in self.sequence:
                if f == i:
                    count += 1
            perc = round(count / len(self.sequence), 3)
            stat_table[f] = perc
        return stat_table

    def weight(self, alphab, mass_tab):
        weight = 0
        for f in alphab:
            count = 0
            ind = alphab.index(f)
            for i in self.sequence:
                if f == i:
                    count += 1
            weight += count * mass_tab[ind]
        return weight


class DNA(Sequences):
    def __init__(self, name, sequence, missing_value):
        super().__init__(name, sequence, missing_value)
        self.alphab = ['A', 'T', 'C', 'G', self.missing_value]
        self.small_alphab = ['a', 't', 'c', 'g']
        self.sequence = Sequences.make_bigger(self, fromm=self.small_alphab, to=self.alphab)
        if not Sequences.alphabet(self, alphab=self.alphab):
            self.sequence = None
        self.mass_tab = [313.2, 304.2,  289.2, 329.2, 0]
        self.reverse = ['T', 'A', 'G', 'C', self.missing_value]

    def stats(self):
        return super().stats(self.alphab)

    def weight(self):
        print('Exact molecular weight of ssDNA')
        return super().weight(self.alphab, self.mass_tab) + 79

    def complement(self):
        return Sequences.make_bigger(self, self.alphab, self.reverse)

    def transcription(self):
        print('assumed your sequence is 5-3 string of dna')
        seq = ''
        for f in self.sequence:
            if f == 'T':
                seq += 'U'
            else:
                seq += f
        return seq


class RNA(Sequences):
    def __init__(self, name, sequence, missing_value):
        super().__init__(name, sequence, missing_value)
        self.alphab = ['A', 'U', 'C', 'G', self.missing_value]
        self.small_alphab = ['a', 'u', 'c', 'g']
        self.sequence = Sequences.make_bigger(self, fromm=self.small_alphab, to=self.alphab)
        if not Sequences.alphabet(self, alphab=self.alphab):
            self.sequence = None
        self.mass_tab = [329.2, 306.2, 305.2, 345.2]
        self.reverse = ['U', 'A', 'G', 'C', self.missing_value]

    def stats(self):
        return super().stats(self.alphab)

    def weight(self):
        print('Exact molecular weight of ssRNA')
        return super().weight(self.alphab, self.mass_tab) + 159

    def complement(self):
        return Sequences.make_bigger(self, self.alphab, self.reverse)

    def translation(self):
        protein = ''
        i, j = 0, 3
        while j <= len(self.sequence):
            if self.sequence[i:j] not in self.rna_amiv_dic:
                protein += '-'
            else:
                protein += self.rna_amiv_dic[self.sequence[i:j]]
            i += 3
            j += 3
        return protein


class Protein(Sequences):
    def __init__(self, name, sequence, missing_value):
        super().__init__(name, sequence, missing_value)
        self.alphab = ['A', 'R', 'N', 'D', 'C', 'E', 'Q', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V', self.missing_value]
        self.small_alphab = ['a', 'r', 'n', 'd', 'c', 'e', 'q', 'g', 'h', 'i', 'l', 'k', 'm', 'f', 'p', 's', 't', 'w', 'y', 'v']
        self.sequence = Sequences.make_bigger(self, fromm=self.small_alphab, to=self.alphab)
        if not Sequences.alphabet(self, alphab=self.alphab):
            self.sequence = None
        self.mass_tab = [71.08, 156.2, 114.1, 115.1, 103.1, 129.1, 128.1, 57.05, 137.1, 113.2, 113.2, 128.2, 131.2, 147.2, 97.12, 87.08, 101.1, 186.2, 163.2, 99.13, 0]

    def stats(self):
        return super().stats(self.alphab)

    def weight(self):
        print('Average mass among isotopes')
        return super().weight(self.alphab, self.mass_tab)


fromm = ['AG', 'AC', 'AT', 'AA', 'TT', 'TC', 'TG', 'TA', 'CT', 'CC', 'CA', 'CG', 'GG', 'GC', 'GA', 'GT']
to = ['TA', 'CT', 'CC', 'CA', 'CG', 'GG', 'GC', 'GA', 'GT', 'AC', 'AT', 'AA', 'TT', 'TC', 'TG', 'AG']
seq = 'AGTGATGGTACTG'
def strange_replacenment(seq, fromm, to):
    res = ''
    j, i = 0, 2
    while i < len(seq):
        ind = fromm.index(str(seq[j:i]))
        res += to[ind]
        j += 2
        i += 2
    return res