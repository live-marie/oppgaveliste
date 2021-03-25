

class Oppgave:
    def __init__(self, navn):
        self.navn = navn
        self.gjort = False

antall_oppgaver = int( input("hvor mange oppgaver skal listen ha? "))
print(antall_oppgaver)

oppgaver = []
for i in range (antall_oppgaver):
    oppgave_navn = input("hva skal oppgaven hete? ")
    oppgave = Oppgave(oppgave_navn)
    oppgaver.append (oppgave)

for o in oppgaver:
    print(o.navn)

def skriv_til_fil(filnavn):
    fil = open(filnavn, "a")
    for oppgave in oppgaver:
        fil.write(oppgave.navn + "\n")
    fil.close()

skriv_til_fil("oppgaver til liste.txt")



