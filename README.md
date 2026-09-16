# Natural Language Processing & Computer Vision Experiments

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Status-Active_Development-orange.svg)]()

A curated collection of practical implementations, algorithmic experiments, and foundational notebooks covering **Natural Language Processing (NLP)** and **Computer Vision (CV)**. This repository serves as a modular codebase for text preprocessing, web scraping, pattern extraction, feature engineering, word embeddings (Word2Vec, FastText, GloVe), and vision processing algorithms.

---

## Repository Structure

```text
nlp-vision-experiments/
│
├── Unit-01/
│   ├── Experiential Learning/                # Hands-on Jupyter notebooks & data extraction
│   │   ├── data/
│   │   │   ├── background.html               # Raw HTML sample data for DOM parsing
│   │   │   └── people_records_20.xlsx        # Structured tabular dataset for regex extraction
│   │   ├── 01-Web-Scraping.ipynb             # HTML scraping using BeautifulSoup & Requests
│   │   ├── 02-Web-Scraping-JSON.ipynb        # API JSON scraping & structured payload parsing
│   │   ├── 03-html-data-extraction.ipynb     # Target HTML tag extraction & cleaning
│   │   ├── 04-Tokenization.ipynb             # Linguistic tokenization via spaCy & NLTK
│   │   ├── 05-Regular-Expression.ipynb       # RegEx application on Excel tabular records
│   │   ├── 06-Stemming-Lemmatization.ipynb   # Morphological reduction & lemmatization
│   │   ├── 07-spaCy-NLP-Pipeline.ipynb       # POS tagging, NER, & spaCy pipeline workflows
│   │   ├── 08-Ngrams-and-TFIDF.ipynb         # CountVectorizer, N-gram matrices & TF-IDF scoring
│   │   └── 09-NLTK-Stemmers-and-Brown-Corpus.ipynb # Stemmer benchmarking & Brown Corpus analysis
│   │
│   └── NLP and Preprocessing techniques/
│       ├── 01-Python-basics-for-text/        # Foundation text manipulation & statistics
│       │   ├── 01-count-characters.py
│       │   ├── 02-count-words-remove-extra-spaces.py
│       │   ├── 03-count-sentences-and-reverse-them.py
│       │   ├── 04-convert-text-to-upper-and-lower.py
│       │   ├── 05-replace-words-and-count-vowels.py
│       │   ├── 06-count-digits-alphabets-spaces.py
│       │   ├── 07-find-frequency-of-every-word.py
│       │   ├── 08-find-the-longest-and-shortest-word.py
│       │   ├── 09-check-palindrome.py
│       │   ├── 10-remove-punctuation.py
│       │   ├── 11-remove-duplicate-words.py
│       │   ├── 12-find-most-frequent-word.py
│       │   ├── 13-extract-email-addresses.py
│       │   └── 14-mini-nlp-program.py
│       └── 02-Regular-Expressions/           # Advanced regex pattern matching & parsing
│
└── Unit-02/                                  # Word Embeddings & Vector Representations
    ├── 01-Gensim_Word2Vec_Demo.ipynb         # Word2Vec model training & embedding visualization
    ├── 02-CBOW.ipynb                         # Continuous Bag-of-Words (CBOW) architecture implementation
    ├── 03-word_similarity_gensim.ipynb       # Pre-trained GloVe embedding loading & vector similarity
    └── 04-fasttext_word_embeddings.ipynb     # Subword embedding modeling using FastText
```

---

## 🚀 Modules & Experiments Overview

### Unit 01: Core Preprocessing & Experiential NLP

Focuses on standardizing string inputs, tokenization, web data extraction, frequency distributions, and feature representation.

#### 1. Python Basics for Text
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
| [`09-check-palindrome.py`](Unit-01/NLP%20and%20Preprocessing%20techniques/01-Python-basics-for-text/09-check-palindrome.py) | Palindromic sequence detection | Two-pointer / sequence reversal |
| [`10-remove-punctuation.py`](Unit-01/NLP%20and%20Preprocessing%20techniques/01-Python-basics-for-text/10-remove-punctuation.py) | Punctuation stripping | `str.maketrans`, `string.punctuation` |
| [`11-remove-duplicate-words.py`](Unit-01/NLP%20and%20Preprocessing%20techniques/01-Python-basics-for-text/11-remove-duplicate-words.py) | Vocabulary deduplication | Ordered set preservation |
| [`12-find-most-frequent-word.py`](Unit-01/NLP%20and%20Preprocessing%20techniques/01-Python-basics-for-text/12-find-most-frequent-word.py) | Mode calculation for text tokens | Frequency sorting / `max()` |
| [`13-extract-email-addresses.py`](Unit-01/NLP%20and%20Preprocessing%20techniques/01-Python-basics-for-text/13-extract-email-addresses.py) | Basic pattern extraction | Token condition filtering |
| [`14-mini-nlp-program.py`](Unit-01/NLP%20and%20Preprocessing%20techniques/01-Python-basics-for-text/14-mini-nlp-program.py) | Integrated text pre-processing pipeline | Normalization, tokenization, frequency map |

#### 2. Experiential Learning Notebooks
| Notebook | Topic / Core Focus | Key Libraries |
| :--- | :--- | :--- |
| [`01-Web-Scraping.ipynb`](Unit-01/Experiential%20Learning/01-Web-Scraping.ipynb) | HTML Parsing & Web Data Scraping | `requests`, `BeautifulSoup` |
| [`02-Web-Scraping-JSON.ipynb`](Unit-01/Experiential%20Learning/02-Web-Scraping-JSON.ipynb) | API Endpoint Consumption & JSON Extraction | `requests`, `json` |
| [`03-html-data-extraction.ipynb`](Unit-01/Experiential%20Learning/03-html-data-extraction.ipynb) | Targeted HTML Tag Extraction & Cleaning | `BeautifulSoup` |
| [`04-Tokenization.ipynb`](Unit-01/Experiential%20Learning/04-Tokenization.ipynb) | Multi-Library Linguistic Tokenization | `spaCy`, `nltk` |
| [`05-Regular-Expression.ipynb`](Unit-01/Experiential%20Learning/05-Regular-Expression.ipynb) | Tabular Data Extraction & Pattern Matching | `pandas`, `re` |
| [`06-Stemming-Lemmatization.ipynb`](Unit-01/Experiential%20Learning/06-Stemming-Lemmatization.ipynb) | Stemming vs Lemmatization Benchmarks | `nltk` |
| [`07-spaCy-NLP-Pipeline.ipynb`](Unit-01/Experiential%20Learning/07-spaCy-NLP-Pipeline.ipynb) | End-to-End Pipeline: POS Tagging, NER, Lemmatization | `spaCy` (`en_core_web_sm`) |
| [`08-Ngrams-and-TFIDF.ipynb`](Unit-01/Experiential%20Learning/08-Ngrams-and-TFIDF.ipynb) | Bag of Words, N-gram Matrices & TF-IDF Scoring | `scikit-learn`, `pandas` |
| [`09-NLTK-Stemmers-and-Brown-Corpus.ipynb`](Unit-01/Experiential%20Learning/09-NLTK-Stemmers-and-Brown-Corpus.ipynb) | Porter/Snowball/Lancaster Comparison & Brown Corpus | `nltk.corpus` |

---

### Unit 02: Word Embeddings & Vector Representations

Explores distributed representation models for capturing semantic relationships and vector space similarities.

| Notebook | Focus Area | Technology / Framework |
| :--- | :--- | :--- |
| [`01-Gensim_Word2Vec_Demo.ipynb`](Unit-02/01-Gensim_Word2Vec_Demo.ipynb) | Custom Word2Vec Model Training & Vector Projections | `gensim.models.Word2Vec` |
| [`02-CBOW.ipynb`](Unit-02/02-CBOW.ipynb) | Continuous Bag-of-Words (CBOW) Architecture | `gensim`, `simple_preprocess` |
| [`03-word_similarity_gensim.ipynb`](Unit-02/03-word_similarity_gensim.ipynb) | Pre-trained GloVe Embeddings (`glove-wiki-gigaword-50`) | `gensim.downloader` |
| [`04-fasttext_word_embeddings.ipynb`](Unit-02/04-fasttext_word_embeddings.ipynb) | Subword-based FastText Vector Modeling | `gensim.models.FastText` |

---

## Usage & Setup

### Prerequisites
- Python 3.8 or higher installed on your system.

### Environment Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/Vaibhav-S-Gowda/nlp-vision-experiments.git
   cd nlp-vision-experiments
   ```

2. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   # Linux/macOS
   source .venv/bin/activate
   ```

3. Install required packages:
   ```bash
   pip install requests beautifulsoup4 pandas nltk spacy scikit-learn gensim
   python -m spacy download en_core_web_sm
   ```

### Running Scripts & Notebooks
- Run standalone Python scripts:
  ```bash
  python "Unit-01/NLP and Preprocessing techniques/01-Python-basics-for-text/14-mini-nlp-program.py"
  ```
- Launch Jupyter Notebooks:
  ```bash
  jupyter notebook
  ```

---

## Tech Stack

- **Languages:** Python 3.x
- **NLP & ML Libraries:** `spaCy`, `NLTK`, `scikit-learn`, `Gensim`
- **Data & Web Utilities:** `pandas`, `NumPy`, `BeautifulSoup4`, `requests`
- **Domain:** Natural Language Processing (NLP), Vector Semantics, Computer Vision (CV)

