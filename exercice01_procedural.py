textes = []
def charger (chemin) :
    global textes
    textes = open (chemin).read().split("\n\n")
def compter_mots () : return sum (len(t.split()) for t in textes)
def frequences () :
    freq = {}
    for t in textes :
        for m in t.lower().split() :
            freq[m] = freq.get(m, 0) + 1
    return freq