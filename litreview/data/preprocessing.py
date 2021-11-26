import pandas as pd
from nltk.corpus import stopwords
from nltk import word_tokenize
import nltk
import string
from unidecode import unidecode
#nltk.download('stopwords')
#nltk.download('punkt')
#nltk.download('wordnet')

stop_words = set(stopwords.words('english'))

# single steps
def lower_case(text):
    lowercased = text.lower()
    return lowercased

def remove_whitespaces(text):
    merged_spaces = text.replace(r"\s\s+",' ')
    return merged_spaces

def remove_special_characters(text):
    text = unidecode(text)
    return text

def remove_punctuation(text):
    for punctuation in string.punctuation:
        text = text.replace(punctuation, '')
    return text

def remove_stopwords(text):
    tokenized = word_tokenize(text)
    without_stopwords = [word for word in tokenized if not word in stop_words]
    return without_stopwords

# this function is not working
def remove_numbers(lst):
    for word in lst:
        if word.isdecimal():
            lst.remove(word)
    return lst

def preprocessing(csv_input):
    df = pd.read_csv(csv_input)
    df["clean_abstract"] = df["abstract"] + df["authors"] + df["title"]
    df['clean_abstract'] = df.clean_abstract.apply(lower_case)
    df['clean_abstract'] = df.clean_abstract.apply(remove_whitespaces)
    df['clean_abstract'] = df.clean_abstract.apply(remove_special_characters)
    df['clean_abstract'] = df.clean_abstract.apply(remove_punctuation)
    df['clean_abstract'] = df.clean_abstract.apply(remove_stopwords)
    df["clean_abstract_text"] = df["clean_abstract"].apply(lambda x: " ".join(x))

    return df

def input_preprocessing(text):
    text = lower_case(text)
    text = remove_whitespaces(text)
    text = remove_special_characters(text)
    text = remove_punctuation(text)
    text = remove_stopwords(text)
    text = " ".join(text)
    return text
