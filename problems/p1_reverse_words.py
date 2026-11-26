
# P1: Reverse Word Order

sentence = input()

has_full_stop = sentence.endswith(".")

if has_full_stop:
    sentence = sentence[:-1]

words = sentence.split()
reversed_words = words[::-1]

result = " ".join(reversed_words)

if has_full_stop:
    result += "."

print(result)
