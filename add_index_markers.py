import re
import os

# Mapping of names found in text to their standardized Index entry
CHARACTER_MAP = {
    r'\bElizabeth\b': 'Bennet, Elizabeth',
    r'\bLizzy\b': 'Bennet, Elizabeth',
    r'\bJane\b': 'Bennet, Jane',
    r'\bMary\b': 'Bennet, Mary',
    r'\bKitty\b': 'Bennet, Catherine (Kitty)',
    r'\bCatherine Bennet\b': 'Bennet, Catherine (Kitty)',
    r'\bLydia\b': 'Bennet, Lydia',
    r'\bMr\. Bennet\b': 'Bennet, Mr.',
    r'\bMrs\. Bennet\b': 'Bennet, Mrs.',
    r'\bMr\. Darcy\b': 'Darcy, Fitzwilliam',
    r'\bDarcy\b': 'Darcy, Fitzwilliam',
    r'\bMr\. Bingley\b': 'Bingley, Charles',
    r'\bBingley\b': 'Bingley, Charles',
    r'\bMiss Bingley\b': 'Bingley, Caroline',
    r'\bCaroline Bingley\b': 'Bingley, Caroline',
    r'\bMr\. Wickham\b': 'Wickham, George',
    r'\bWickham\b': 'Wickham, George',
    r'\bMr\. Collins\b': 'Collins, William',
    r'\bCollins\b': 'Collins, William',
    r'\bLady Catherine\b': 'de Bourgh, Lady Catherine',
    r'\bCharlotte Lucas\b': 'Collins, Charlotte (Lucas)',
    r'\bCharlotte\b': 'Collins, Charlotte (Lucas)',
    r'\bSir William\b': 'Lucas, Sir William',
    r'\bLady Lucas\b': 'Lucas, Lady',
    r'\bMr\. Gardiner\b': 'Gardiner, Mr.',
    r'\bMrs\. Gardiner\b': 'Gardiner, Mrs.',
    r'\bGeorgiana\b': 'Darcy, Georgiana',
    r'\bColonel Fitzwilliam\b': 'Fitzwilliam, Colonel',
}

def add_index_markers(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Sort keys by length descending to match longer names first (e.g., "Mr. Bennet" before "Bennet")
    sorted_names = sorted(CHARACTER_MAP.keys(), key=len, reverse=True)

    def replacement_func(match):
        name = match.group(0)
        # Find the standardized entry for this specific match
        for pattern in sorted_names:
            if re.fullmatch(pattern, name):
                index_entry = CHARACTER_MAP[pattern]
                # Avoid double indexing if already present
                if f'\\index{{{index_entry}}}' in match.string[match.start():match.end() + 20]:
                    return name
                return f'{name}\\index{{{index_entry}}}'
        return name

    # Regex to find names while avoiding already indexed parts or metadata
    # This is a simplified approach; in a real scenario, we'd avoid code blocks, etc.
    for pattern in sorted_names:
        # Only index if not followed by another \index
        # We use a negative lookahead to prevent double-indexing if the script is run twice
        compiled_pattern = re.compile(f'({pattern})(?!\\s*\\\\index)')
        content = compiled_pattern.sub(lambda m: f'{m.group(1)}\\index{{{CHARACTER_MAP[pattern]}}}', content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Successfully processed {file_path}")

if __name__ == "__main__":
    target_file = 'ebook.md'
    if os.path.exists(target_file):
        add_index_markers(target_file)
    else:
        print(f"Error: {target_file} not found.")
