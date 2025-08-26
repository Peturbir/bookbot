def get_num_words(text: str) -> int:
    return len(text.split())

def count_characters(text: str) -> dict[str, int]:
    chars = {}
    for c in text.lower(): #convert any character to lowercase to avoid duplicates
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
    return chars

def sort_on(item: dict) -> int:
    return item["num"]

def sort_char_counts(char_counts: dict[str, int]) -> list[dict]:
    items = [{"char": ch, "num": n} for ch, n in char_counts.items()]
    items.sort(reverse=True, key=sort_on)
    return items
