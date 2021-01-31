def distance(strand_a, strand_b):
    if len(strand_a) == len(strand_b):
        hammingCounter = [strand_a[e] != strand_b[e] for e in range(len(strand_a))]
        return hammingCounter.count(True)
    else:
        raise ValueError("The Strings are unequal in length!")
