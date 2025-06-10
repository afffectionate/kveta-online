from sanic import Sanic
from sanic import response
import spacy
from collections import Counter

app = Sanic("MyHelloWorldApp")
app.static('/static', './static')

nlp = spacy.load("en_core_web_sm")

def preprocess_text(text):
    doc = nlp(text)
    return doc

def tokenize_text(doc):
    tokenized_text = [token.text for token in doc if not token.is_space and not token.is_punct]
    return tokenized_text

def get_types(tokens):
    types = list(set(tokens))
    return types

def get_word_lengths(list_of_tokens):
    lengths = [len(token) for token in list_of_tokens]
    return lengths

def get_sentence_lengths(doc):
    list_of_tokenized_sentences = [tokenize_text(sentence) for sentence in doc.sents]
    sentence_lengths = [len(item) for item in list_of_tokenized_sentences]
    return sentence_lengths

def get_lemmas(doc):
    lemmas = [token.lemma_ for token in doc if not token.is_space and not token.is_punct and not token.is_stop]
    return lemmas

def get_word_frequencies(lemmas):
    return Counter(lemmas).most_common(50)

def get_hapaxy(tokens):
    freq = Counter(tokens)
    return [word for word, count in freq.items() if count == 1]
    
@app.route("/", methods=["GET"])
async def display_index_page(request):
    return await response.file("templates/index.html")

@app.route("/process", methods=["POST"])
async def calculate_shit(request): 
    file = request.files.get("file")
    file_content = file.body.decode('utf-8')

    doc = preprocess_text(file_content)
    tokens = tokenize_text(doc)
    types = get_types(tokens)

    result_dict = {
        "tokens" : len(tokens),
        "types" : len(types),
        "ttr" : len(tokens)/len(types),
        "wordLengths" : get_word_lengths(tokens),
        "sentenceLengths" : get_sentence_lengths(doc),
        "hapaxLegomena" : get_hapaxy(tokens),
        "wordCloudData" : get_word_frequencies(get_lemmas(doc))
    }
    return response.json(result_dict)

if __name__ == "__main__":
    app.run()