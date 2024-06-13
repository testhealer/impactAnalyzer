import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

# Ensure the necessary resources are downloaded
nltk.download('punkt')
nltk.download('stopwords')

def extract_keywords(text):
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text)
    filtered_words = [word for word in words if word.lower() not in stop_words and word not in string.punctuation]
    return filtered_words
