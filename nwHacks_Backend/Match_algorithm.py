from thefuzz import fuzz
from transformers import BertTokenizer, BertModel
import torch
import sklearn
from sklearn.metrics.pairwise import cosine_similarity
import nltk
from nltk.corpus import stopwords



def key_word_similarity(key_word_org, key_word_comp):
    similarity_score = fuzz.ratio(key_word_org, key_word_comp)
    return similarity_score

# the following code does not consider synonyms/semantics

# vectorizer = TfidfVectorizer(stop_words='english', lowercase=True)
# vectors = vectorizer.fit_transform([Mission_1, Company_1])

# similarity_matrix = cosine_similarity(vectors)

# similarity_score = similarity_matrix[0,1]
# print ("Similarity score of scikitlearn: " + str(similarity_score))


#; using bert embeddings for consideration of semantics (better for long sentences)
#; not great for short words (ie. key words)
nltk.download('stopwords')
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')

def mission_similarity(org_mission, company_mission):
    #; filter out stop words
    token_mission = tokenizer.encode(org_mission, return_tensors='pt')[0]
    filtered_mission = [token for token in token_mission[1:-1] if tokenizer.decode([token]).lower() not in stopwords.words('english')]

    #; filter out stop words
    token_company = tokenizer.encode(company_mission, return_tensors='pt')[0]
    filtered_company = [token for token in token_company[1:-1] if tokenizer.decode([token]).lower() not in stopwords.words('english')]


    with torch.no_grad():
        embeddings_mission = model(torch.tensor([filtered_mission])).last_hidden_state.mean(dim=1)
        embeddings_company = model(torch.tensor([filtered_company])).last_hidden_state.mean(dim=1)

    similarity_score = cosine_similarity(embeddings_mission, embeddings_company)[0,0]
    return similarity_score

# print("Similarity score using sklearn and bert: " + str(similarity_score * 100))