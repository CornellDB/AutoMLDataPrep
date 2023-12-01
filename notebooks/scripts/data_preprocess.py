import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download('stopwords')
nltk.download('wordnet')
w2v_model = None

def preprocess_text(text):
  tokens = nltk.word_tokenize(text)
  # Remove special characters
  tokens = [word for word in tokens if word.isalpha()]
  # Convert to lower case
  tokens = [word.lower() for word in tokens]
  # Remove stopwords
  stop_words = set(stopwords.words('english'))
  tokens = [word for word in tokens if word not in stop_words]
  # Lemmatize token
  lemmatizer = WordNetLemmatizer()
  tokens = [lemmatizer.lemmatize(word) for word in tokens]
  
  return tokens