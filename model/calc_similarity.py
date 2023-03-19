import sklearn
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def text_similarity(text1, text2):
  # Convert the texts into TF-IDF vectors
  vectorizer = TfidfVectorizer()
  vectors = vectorizer.fit_transform([text1, text2])

  # Calculate the cosine similarity between the vectors
  similarity = cosine_similarity(vectors)
  return similarity

def calc_all_sim(errs, reqs):
  ''' 
    Calculate the similarity between all messages and all requirements.
    Input: list of error messages, list of requirements descriptions.
    Returns a dictionary of messages with their highest similarity score
  ''' 
  similarity_score = []
  max_sim = {}
  for m in errs:
    similarity_score = []
    if m not in max_sim:
      for r in reqs:
        similarity_score.append(text_similarity(m, r)[0][1])
      max_sim[m] = max(similarity_score)

  return max_sim