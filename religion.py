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
    cmd = input("\n> ")
    
    if cmd == "quit":
        print("Stillness returns.")
        break
    elif cmd == "entire":
        print("".join(dna))
    elif cmd == "stats":
        mutations = len([s for s in seen if s >= 3])
        print(f"Total views: {sum(seen)}")
        print(f"Mutations: {mutations}")
    elif cmd.startswith("view"):
        parts = cmd.split()
        if len(parts) == 3:
            s = int(parts[1])
            e = int(parts[2])
            for p in range(s, e):
                seen[p] = seen[p] + 1
                if seen[p] % 3 == 0:
                    old = dna[p]
                    choices = ['A','T','C','G']
                    choices.remove(old)
                    dna[p] = random.choice(choices)
                    print(f">>> MUTATION at {p}: {old} -> {dna[p]}")
                print(f"[{p}] {dna[p]} (seen {seen[p]} times)")
        else:
            print("Use: view 20 40")
    else:
        print("Commands: view 20 40, entire, stats, quit")
