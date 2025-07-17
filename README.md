# 💬 Sentiment Analysis using VADER (NLTK)

This project is a simple command-line tool for **sentiment analysis** using the **VADER (Valence Aware Dictionary and sEntiment Reasoner)** model from the **NLTK** library.

It analyzes the sentiment of any input English text and classifies it as **Positive**, **Negative**, or **Neutral**, along with detailed polarity scores.

---

## 🚀 Features

- Uses **VADER lexicon** from `nltk.sentiment.vader`
- Outputs sentiment polarity scores (`pos`, `neu`, `neg`, `compound`)
- Classifies overall sentiment as:
  - 🔵 **Positive** (compound ≥ 0.05)
  - 🔴 **Negative** (compound ≤ -0.05)
  - ⚪ **Neutral** (otherwise)
- Simple command-line interface for interactive analysis

---

## 📦 Requirements

Install the required library:

```bash
pip install nltk

