import random

class Recurrence:

    def __init__(self, recurrence, base):
        self.L, self.c_i = self.parse_recurrence(recurrence)
        self.base = self.parse_base(base)

    def parse_recurrence(self, recurrence):
        rec = recurrence.replace(" ", "").split("+")
        c_i = []
        for elem in rec:
            c_i.append(int(elem[0]))
        return len(c_i), c_i

    def parse_base(self, base):
        ba = base.replace(" ", "").split(",")
        b = []
        for elem in ba:
            b.append(int(elem))
        return b

    def nth_element(self, n):
        temp = []
        for elem in self.base:
            temp.append(elem)
        elem = len(temp)
        while(elem < n):
            next_elem = 0
            offset = len(self.c_i)
            length = offset
            while(offset > 0):
                next_elem += self.c_i[length - offset] * temp[elem - offset]
                offset -= 1
            temp.append(next_elem)
            elem += 1
        return temp[n-1]

    def decomposition(self, m, j):
        decomp = ""
        l = 1
        length = j
        count = 0
        while(m != 0):
            G_j = self.nth_element(j)
            x = int(m/G_j)
            if(l < self.L):
                y = min(x, self.c_i[l-1])
            elif(l==self.L):
                y = min(x, self.c_i[l-1]-1)
            decomp += str(y)
            m = m - y * G_j
            j -= 1
            if(y == self.c_i[l-1]):
                l += 1
            else:
                l = 1
            count += 1
        if(len(decomp) < length):
            decomp += "0" * (length - len(decomp))
        return decomp

    def random_sequence(self, seq_length, word_length):
        start, end = self.nth_element(word_length), self.nth_element(word_length + 1)
        decompositions = []
        for x in range(start, end): # does not include in
            decompositions.append(self.decomposition(x, word_length))
        print(decompositions)
        seq = ""
        while(len(seq) < seq_length):
            seq += random.choice(decompositions)
        return seq

class SequenceAnalyzer:

    def __init__(self, seq):
        self.seq = seq

    def frequencies(self):
        freq = [0] * 10
        for elem in seq:
            freq[int(elem)] += 1
        for x in range(10):
            print(x, freq[x])
        return freq

if __name__ == '__main__':
    rec = Recurrence("1n + 1(n-1)", "1, 2") # firt input is recurrence and second input are the base cases
    # for Gn+1 = 7Gn + 8Gn-1 and base case of G1=2 and G2=3, Recurrence("7n + 8(n-1)", "2, 3")
    seq = rec.random_sequence(100, 6)
    sa = SequenceAnalyzer(seq)
    sa.frequencies()

