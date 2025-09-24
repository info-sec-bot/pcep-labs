# Step 1 Normalize Input

def normalize(text:str)->str:
    text = text.strip()
    words = text.split()
    return " ".join(words).lower()

# Step 2: Basic Counts
def basic_count(text:str)->dict:
    counts = {"chars": 0, "letters": 0, "digits": 0, "spaces": 0}
    for char in text:
        counts["chars"] += 1
        if char.isalpha():
            counts["letters"] += 1
        if char.isdigit():
            counts["digits"] += 1
        if char.isspace():
            counts["spaces"] += 1
    return counts

# Step 3 Word Counting and Top-N
def word_frequencies(text:str)->dict:
    freqs = {}
    for raw in text.split():
        w = raw.strip(".,;:!?\"()[]{}")
        #print(w)
        # Remove common pronouns and prepositions from word frequency count
        if not w or w == "the" or w == "to" or w == "this" or w == "a" or w == "that" or w == "is" or w == "be" or w == "and" or w == "of" or w == "on" or \
                w == "at" or w == "his" or w == "had" or w == "him" or w == "in" or w == "with" or w == "as" or w == "it" or w == "he":
            continue
        freqs[w] = freqs.get(w, 0) + 1
    return freqs
# Return top frequency count
def top_n(freqs:dict, n:int = 5):
    return sorted(freqs.items(), key=lambda kv: (-kv[1], kv[0]))[:n]

def format_report(text:str)->str:
    norm = normalize(text)
    counts = basic_count(norm)
    freqs = word_frequencies(norm)
    top = top_n(freqs, 5)
    lines = []
    lines.append("=== Text Analyzer Report ===")
    lines.append(f"Original length: {len(text)} characters")
    lines.append("")
    lines.append("Counts")
    lines.append(f" Letters: {counts['letters']}")
    lines.append(f" Digits: {counts['digits']}")
    lines.append(f" Spaces: {counts['spaces']}")
    lines.append(f" Total: {counts['chars']}")
    lines.append("")
    lines.append("Top Words:")
    pair = []
    sorted_word = []
    sorted_list = []
    if top:
        i = 0
        b = i - 1
        res = []
        # j = 1
        # Create sorted_list with word,cnt - this is also where words and count are appended to lines (printed output)
        for word,cnt in top:
            pair=[(word,cnt)]
            sorted_list.append([word,cnt])
            lines.append(f"{word:<12} {cnt:> 3}")
        for i,item in enumerate(sorted_list):
            #print(f"count {i} = {sorted_list[i][1]} b {b} = {sorted_list[b][1]}")
            if sorted_list[i][1] == sorted_list[b][1]:
                sorted_word.append([sorted_list[i][0],sorted_list[i][1]])
                sorted_word.append([sorted_list[b][0],sorted_list[b][1]])
                # Using List Comprehension to remove duplicates when adding sets to compare to the list
                sorted_word.sort()
                [res.append(word) for word in sorted_word if word not in res]

            b+=1
        print(f"This is sorted ties 😎{sorted(res, key=lambda word: word[1], reverse=True)}")

    else:
        lines.append(" No words found")
    return "\n".join(lines)

if __name__ == "__main__":

    sample = input("Enter a sentence: ")
    #print("Your sentence as typed: ", sample)

    # Example strip function
    #print("Your sentence as striped and split: ", normalize(sample))

    # Example count function
    #print(basic_count(sample))

    # Example word frequencies
    #print(word_frequencies(sample))
    freqs = word_frequencies(sample)

    # Example top frequencies
    print(top_n(freqs, 5))

    print(format_report(sample))