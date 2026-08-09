# Natural Language Processing & Computer Vision Experiments

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Status-Active_Development-orange.svg)]()

A curated collection of practical implementations, algorithmic experiments, and foundational scripts covering **Natural Language Processing (NLP)** and **Computer Vision (CV)**. This repository serves as a modular codebase for text preprocessing, tokenization, regular expressions, pattern extraction, and vision processing algorithms.

---

## Repository Structure

```text
nlp-vision-experiments/
│
└── Unit-01/
    └── NLP and Preprocessing techniques/
        ├── 01-Python-basics-for-text/       # Foundation text manipulation & statistics
        │   ├── 01-count-characters.py
        │   ├── 02-count-words-remove-extra-spaces.py
        │   ├── 03-count-sentences-and-reverse-them.py
        │   ├── 04-convert-text-to-upper-and-lower.py
        │   ├── 05-replace-words-and-count-vowels.py
        │   ├── 06-count-digits-alphabets-spaces.py
        │   ├── 07-find-frequency-of-every-word.py
        │   ├── 08-find-the-longest-and-shortest-word.py
        │   ├── 09-chech-palindrome.py
        │   ├── 10-remove-punctuation.py
        │   ├── 11-remove-duplicate-words.py
        │   ├── 12-find-most-frequent-word.py
        │   ├── 13-extract-email-addresses.py
        │   └── 14-mini-nlp-program.py
        └── 02-Regular-Expressions/          # Advanced regex pattern matching & parsing
```

---

## 🚀 Modules Overview

### Unit 01: NLP & Text Preprocessing Techniques

Focuses on standardizing string inputs, tokenization, frequency distributions, and cleaning pipelines necessary prior to downstream modeling.

| Script / Module | Description | Key Operations |
| :--- | :--- | :--- |
| [`01-count-characters.py`](Unit-01/NLP%20and%20Preprocessing%20techniques/01-Python-basics-for-text/01-count-characters.py) | Character length computation | String length validation |
| [`02-count-words-remove-extra-spaces.py`](Unit-01/NLP%20and%20Preprocessing%20techniques/01-Python-basics-for-text/02-count-words-remove-extra-spaces.py) | Whitespace normalization & word counting | `split()`, whitespace trimming |
| [`03-count-sentences-and-reverse-them.py`](Unit-01/NLP%20and%20Preprocessing%20techniques/01-Python-basics-for-text/03-count-sentences-and-reverse-them.py) | Sentence delimitation & reversal | Delimiter splitting, slicing |
| [`04-convert-text-to-upper-and-lower.py`](Unit-01/NLP%20and%20Preprocessing%20techniques/01-Python-basics-for-text/04-convert-text-to-upper-and-lower.py) | Case normalization | Case transformation |
| [`05-replace-words-and-count-vowels.py`](Unit-01/NLP%20and%20Preprocessing%20techniques/01-Python-basics-for-text/05-replace-words-and-count-vowels.py) | Substring substitution & vowel frequency analysis | Target replacement, set checks |
| [`06-count-digits-alphabets-spaces.py`](Unit-01/NLP%20and%20Preprocessing%20techniques/01-Python-basics-for-text/06-count-digits-alphabets-spaces.py) | Character type categorization | `isdigit()`, `isalpha()`, `isspace()` |
| [`07-find-frequency-of-every-word.py`](Unit-01/NLP%20and%20Preprocessing%20techniques/01-Python-basics-for-text/07-find-frequency-of-every-word.py) | Term frequency dictionary calculation | Hash map frequency aggregation |
| [`08-find-the-longest-and-shortest-word.py`](Unit-01/NLP%20and%20Preprocessing%20techniques/01-Python-basics-for-text/08-find-the-longest-and-shortest-word.py) | Extremum word length identification | Key-based max/min selection |
| [`09-chech-palindrome.py`](Unit-01/NLP%20and%20Preprocessing%20techniques/01-Python-basics-for-text/09-chech-palindrome.py) | Palindromic sequence detection | Two-pointer / sequence reversal |
| [`10-remove-punctuation.py`](Unit-01/NLP%20and%20Preprocessing%20techniques/01-Python-basics-for-text/10-remove-punctuation.py) | Punctuation stripping | `str.maketrans`, `string.punctuation` |
| [`11-remove-duplicate-words.py`](Unit-01/NLP%20and%20Preprocessing%20techniques/01-Python-basics-for-text/11-remove-duplicate-words.py) | Vocabulary deduplication | Ordered set preservation |
| [`12-find-most-frequent-word.py`](Unit-01/NLP%20and%20Preprocessing%20techniques/01-Python-basics-for-text/12-find-most-frequent-word.py) | Mode calculation for text tokens | Frequency sorting / `max()` |
| [`13-extract-email-addresses.py`](Unit-01/NLP%20and%20Preprocessing%20techniques/01-Python-basics-for-text/13-extract-email-addresses.py) | Basic pattern extraction | Token condition filtering |
| [`14-mini-nlp-program.py`](Unit-01/NLP%20and%20Preprocessing%20techniques/01-Python-basics-for-text/14-mini-nlp-program.py) | Integrated text pre-processing pipeline | Normalization, tokenization, frequency map |

---

## Usage & Setup

### Prerequisites
- Python 3.8 or higher installed on your system.

### Running a Script
No external third-party dependencies are required for base preprocessing modules. Run any script directly using Python:

```bash
python "Unit-01/NLP and Preprocessing techniques/01-Python-basics-for-text/14-mini-nlp-program.py"
```

---

## Tech Stack

- **Language:** Python 3.x
- **Libraries:** Standard Library (`re`, `string`, `collections`, `math`)
- **Domain:** Natural Language Processing (NLP), Computer Vision (CV)

