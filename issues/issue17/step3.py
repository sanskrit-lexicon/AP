import os

SANHW1_PATH = "/Users/dhaval/Documents/GithubRepos/sanskrit-lexicon/hwnorm1/sanhw1/sanhw1.txt"
INPUT_PATH = "log2.tsv"
OUTPUT_PATH = "log3.tsv"


def load_sanhw1_words(filepath):
    words = set()
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if ":" in line:
                word = line.split(":")[0]
                words.add(word)
    return words


def main():
    sanhw1_words = load_sanhw1_words(SANHW1_PATH)
    print(f"Loaded {len(sanhw1_words)} words from sanhw1.txt")

    with open(INPUT_PATH, "r", encoding="utf-8") as f:
        lines = f.readlines()

    found_in_sanhw1 = 0
    not_found_in_sanhw1 = 0

    with open(OUTPUT_PATH, "w", encoding="utf-8") as out:
        header = lines[0].strip() + "\tin_sanhw1\n"
        out.write(header)

        for line in lines[1:]:
            line = line.strip()
            if not line:
                continue
            parts = line.split("\t")
            resolution = parts[3]
            if resolution == "None":
                in_sanhw1 = False
            else:
                in_sanhw1 = resolution in sanhw1_words
                if not in_sanhw1:
                    if resolution.endswith("H"):
                        in_sanhw1 = resolution[:-1] in sanhw1_words
                    elif resolution.endswith("m"):
                        in_sanhw1 = resolution[:-1] in sanhw1_words
            if in_sanhw1:
                found_in_sanhw1 += 1
            else:
                not_found_in_sanhw1 += 1
            out.write(line + f"\t{in_sanhw1}\n")

    total = found_in_sanhw1 + not_found_in_sanhw1
    print(f"Found in sanhw1: {found_in_sanhw1}")
    print(f"Not found in sanhw1: {not_found_in_sanhw1}")
    print(f"Total: {total}")
    print(f"Written to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
