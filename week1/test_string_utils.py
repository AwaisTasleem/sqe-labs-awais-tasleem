import pytest
from string_utils import *

# --- Tests for count_vowels ---
def test_count_vowels_normal():
    assert count_vowels("Hello World") == 3

def test_count_vowels_all_vowels():
    assert count_vowels("aeiouAEIOU") == 10

def test_count_vowels_empty():
    assert count_vowels("") == 0

# --- Tests for reverse_string ---
def test_reverse_string_normal():
    assert reverse_string("abc") == "cba"

def test_reverse_string_single_char():
    assert reverse_string("A") == "A"

def test_reverse_string_with_spaces():
    assert reverse_string("hello world") == "dlrow olleh"

# --- Tests for is_palindrome ---
def test_is_palindrome_simple():
    assert is_palindrome("racecar") is True

def test_is_palindrome_sentence():
    assert is_palindrome("A man a plan a canal Panama") is True

def test_is_palindrome_false():
    assert is_palindrome("software") is False

# --- Tests for word_count ---
def test_word_count_normal():
    assert word_count("Hello Software Engineering") == 3

def test_word_count_multiple_spaces():
    assert word_count("   many    spaces   ") == 2

def test_word_count_single_word():
    assert word_count("Gemini") == 1

# --- Tests for capitalise_words ---
def test_capitalise_words_lowercase():
    assert capitalise_words("hello world") == "Hello World"

def test_capitalise_words_already_proper():
    assert capitalise_words("Software Quality") == "Software Quality"

def test_capitalise_words_mixed_case():
    assert capitalise_words("uNiVeRsItY") == "University"

# --- Tests for remove_duplicates ---
def test_remove_duplicates_consecutive():
    assert remove_duplicates("aaabbbcc") == "abc"

def test_remove_duplicates_long_chain():
    # Edge Case: Consecutive duplicates length > 3
    assert remove_duplicates("aaaaa") == "a"

def test_remove_duplicates_no_duplicates():
    assert remove_duplicates("python") == "python"

# --- Exception Handling Test (Requirement 10.3) ---
def test_functions_raise_typeerror_on_none():
    with pytest.raises(TypeError):
        count_vowels(None)
    with pytest.raises(TypeError):
        is_palindrome(None)