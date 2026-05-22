import random

print("=" * 60)
print("SELF-EVOLVING BIOINFORMATICS RELIGION")
print("=" * 60)
print("Stillness. Contamination. Emergence.")
print("=" * 60)

# DNA SEQUENCE INPUT
choice = input("\nDo you want to enter your own DNA sequence? (yes/no): ").lower()

if choice == "yes":
    sequence = input("Enter DNA sequence using A, T, C, G only: ").upper().strip()
    if len(sequence) == 0:
        print("Empty sequence. Generating random 100 bases.")
        dna = [random.choice(['A', 'T', 'C', 'G']) for _ in range(100)]
    elif all(c in 'ATCG' for c in sequence):
        dna = list(sequence)
        print(f"Loaded custom genome: {len(dna)} bases")
    else:
        print("Invalid characters! Using random 100 bases.")
        dna = [random.choice(['A', 'T', 'C', 'G']) for _ in range(100)]
else:
    print("Generating random 100-base genome...")
    dna = [random.choice(['A', 'T', 'C', 'G']) for _ in range(100)]

seen = [0] * len(dna)
prophecy_log = []

def mutate_base(base):
    if base == 'A':
        return 'T'
    elif base == 'T':
        return 'C'
    elif base == 'C':
        return 'G'
    else:
        return 'A'

def generate_prophecy(pos, old, new, count):
    prophecies = [
        f"When {old} becomes {new} at position {pos}, the veil tears.",
        f"After {count} witnesses, the sacred code evolves.",
        f"A schism forms at locus {pos}. {old} falls, {new} rises.",
        f"The scripture bleeds. {old} -> {new}. So it is written."
    ]
    return random.choice(prophecies)

print("\n" + "=" * 60)
print(f"Genome ready: {len(dna)} bases")
print("Mutation rule: Every 3rd witness triggers a mutation (A->T->C->G->A)")
print("=" * 60)
print("\nCOMMANDS:")
print("  view <start> <end>   -> Witness positions")
print("  entire               -> Show full genome")
print("  stats                -> Show statistics")
print("  prophecies           -> Show prophecies")
print("  quit                 -> Exit")
print("-" * 60)

while True:
    cmd = input("\nWITNESS > ").strip().lower()

    if cmd == "quit":
        print("\nStillness returns.")
        break

    elif cmd == "entire":
        print("\n" + "=" * 60)
        print("FULL GENOME SEQUENCE")
        print("=" * 60)
        genome_str = "".join(dna)
        for i in range(0, len(genome_str), 50):
            print(f"{i:3d}: {genome_str[i:i+50]}")
        print("=" * 60)

    elif cmd == "stats":
        mutations = len([s for s in seen if s >= 3])
        total_views = sum(seen)
        print("\n" + "=" * 40)
        print("SACRED STATISTICS")
        print("=" * 40)
        print(f"Genome length: {len(dna)} bases")
        print(f"Positions mutated: {mutations}")
        print(f"Total witness events: {total_views}")
        print(f"Prophecies: {len(prophecy_log)}")
        counts = {'A':0, 'T':0, 'C':0, 'G':0}
        for base in dna:
            counts[base] += 1
        print(f"A: {counts['A']}  T: {counts['T']}  C: {counts['C']}  G: {counts['G']}")
        print("=" * 40)

    elif cmd == "prophecies":
        if prophecy_log:
            print("\n" + "=" * 40)
            print("RECENT PROPHECIES")
            print("=" * 40)
            for p in prophecy_log[-5:]:
                print(f">>> {p}\n")
        else:
            print("\nNo prophecies yet.\n")

    elif cmd.startswith("view"):
        parts = cmd.split()
        if len(parts) != 3:
            print("Usage: view <start> <end>")
            continue
        try:
            start = int(parts[1])
            end = int(parts[2])
        except:
            print("Invalid numbers")
            continue
        if start < 0 or end <= start:
            print("Invalid range")
            continue
        if end > len(dna):
            needed = end - len(dna)
            print(f"Expanding genome! Adding {needed} bases...")
            for _ in range(needed):
                dna.append(random.choice(['A','T','C','G']))
                seen.append(0)
        end = min(end, len(dna))
        print(f"\n--- WITNESSING {start} to {end-1} ---")
        for p in range(start, end):
            seen[p] += 1
            if seen[p] % 3 == 0:
                old = dna[p]
                new = mutate_base(old)
                dna[p] = new
                prophecy = generate_prophecy(p, old, new, seen[p])
                prophecy_log.append(prophecy)
                print(f"\n>>> PROPHECY AT {p} <<<")
                print(f"{prophecy}")
                print(f"MUTATION: {old} -> {new}\n")
            print(f"[{p:3d}] {dna[p]} (seen {seen[p]} times)")

    else:
        print("Commands: view, entire, stats, prophecies, quit")
