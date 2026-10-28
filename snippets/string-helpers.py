"""Python string helpers from the log. Run: python snippets/string-helpers.py"""


def reverse_words(s):
    return " ".join(reversed(s.split()))


def is_pangram(s):
    return set("abcdefghijklmnopqrstuvwxyz") <= set(s.lower())


if __name__ == "__main__":
    print(reverse_words("learn something every day"))
    print(is_pangram("The quick brown fox jumps over the lazy dog"))
