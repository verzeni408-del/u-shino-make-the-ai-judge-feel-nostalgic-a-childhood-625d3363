"""Write one childhood memory sentence to /output/entry.txt."""
import os

# One sentence, plain words: Sunday soup, a chipped blue pot, bones for her.
ENTRY = "Every Sunday my grandmother ladled chicken soup from her chipped blue pot, gave us the meat and ate only the boiled bones herself, saying they were the best part, and I never once offered her mine."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
