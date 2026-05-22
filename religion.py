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
        print(f"Total views: {sum(seen)}")
    elif cmd.startswith("view"):
        parts = cmd.split()
        if len(parts) == 3:
            s = int(parts[1])
            e = int(parts[2])
            for p in range(s, e):
                seen[p] += 1
                if seen[p] % 3 == 0:
                    old = dna[p]
                    new = random.choice([x for x in ['A','T','C','G'] if x != old])
                    dna[p] = new
                    print(f"MUTATION at {p}: {old}->{new}")
                print(f"[{p}] {dna[p]} (seen {seen[p]})")
