

antall_oppgaver = int( input("hvor mange oppgaver skal listen ha? "))
print(antall_oppgaver)

oppgaver = []
for i in range (antall_oppgaver):
    oppgave_navn = input("hva skal oppgaven hete? ")
    oppgaver.append (oppgave_navn)
print(oppgaver)

def skriv_til_fil(filnavn):
    fil = open(filnavn, "a")
    for oppgave in oppgaver:
        fil.write(oppgave)
    fil.close()

skriv_til_fil("oppgaver til liste.txt")


