# 🦋 Corfu Butterflies Explorer

**Butterfly Explorer** is an interactive Streamlit application that allows users to explore butterfly species based on their visual traits like color, pattern, and extra features. It uses natural language processing (NLP) with spaCy to interpret search queries and match butterfly attributes accordingly.

> 🧠 Built with Python, Pandas, Streamlit & spaCy  
> 🐛 Inspired by and based on the butterfly data from [Corfu Butterfly Conservation](https://www.corfubutterflyconservation.org/butterflies.php)

---

## 🚀 Features

- 🔎 **Smart Search**: Use natural language (e.g. _"blue with red dots"_) to find butterflies.
- 🎨 **Visual Filters**: Filter butterflies by color, wing pattern, or unique features.
- 🖼️ **Image Gallery**: Browse butterfly images with details shown as captions.
- ⚙️ **spaCy-powered NLP**: Extracts and matches relevant keywords from user queries.

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/kyprosantreou/Corfu_Butterflies.git
cd Corfu_Butterflies
```

```bash
pip install -r requirements.txt
```

#### Then download the spaCy language model:
```bash
python -m spacy download en_core_web_sm
```
### 🧪 Run the App
```bash
streamlit run main.py
```

## 🌍 Data Source & Credits
This project uses butterfly information inspired by the
Corfu Butterfly Conservation project — a valuable resource for butterfly biodiversity on the island of Corfu, Greece.

🦋 Special thanks to their team for documenting butterfly species and making this data accessible for conservation and education.

## 🧪 Test the Program online: 
[Corfu Butterflies Explorer](https://corfu-butterflies.onrender.com/)

## 🧑‍💻 Creator
**Designed and developed by Kypros Andreou.**

