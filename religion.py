import random

print("="*50)
print("SELF-EVOLVING BIOINFORMATICS RELIGION")
print("="*50)

dna = []
for i in range(100):
    dna.append(random.choice(['A','T','C','G']))

seen = [0] * 100

print("Commands: view 20 40, entire, stats, quit")

while True:
    cmd = input("> ")
    
    if cmd == "quit":
        print("Stillness returns.")
        break
    elif cmd == "entire":
        print("".join(dna))
    elif cmd == "stats":
        mutations = len([s for s in seen if s >= 3])
        print("Total views:", sum(seen))
        print("Mutations:", mutations)
    elif cmd.startswith("view"):
        parts = cmd.split()
        if len(parts) == 3:
            s = int(parts[1])
            e = int(parts[2])
            for p in range(s, e):
                seen[p] = seen[p] + 1
                if seen[p] % 3 == 0:
                    old = dna[p]
                    if old == 'A':
                        dna[p] = 'T'
                    elif old == 'T':
                        dna[p] = 'C'
                    elif old == 'C':
                        dna[p] = 'G'
                    else:
                        dna[p] = 'A'
                    print(">>> MUTATION at", p, ":", old, "->", dna[p])
                print("[", p, "]", dna[p], "(seen", seen[p], "times)")
        else:
            print("Use: view 20 40")
