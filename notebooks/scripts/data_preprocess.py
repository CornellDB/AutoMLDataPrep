import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt')
w2v_model = None

def preprocess_text(text):
  """
  Pre-processes and cleans the data using basic NLP approaches.  
  
  Parameters: 
    text (str): The input text which needs pre-processing.
  
  Returns: 
    tokens (list): The list of tokens after the sentence is tokenized and processed.
  """
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