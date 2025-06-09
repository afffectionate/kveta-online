from sanic import Sanic
from sanic import response
import regex

FOLDER = "zvířátka"
CONTEXT_SIZE = 50

app = Sanic("MyHelloWorldApp")
app.static('/static', './static')

def tokenize_text(text):
  tokenized_text = regex.split("\\W+", text)
  return tokenized_text

def get_types(tokens):
   types = list(set(tokens))
   return types

def get_word_lengths(my_list):
    lengths = []
    for item in my_list:
       lengths.append(len(item))
    return lengths

@app.route("/", methods=["GET"])
async def display_index_page(request):
    return await response.file("templates/index.html")

@app.route("/process", methods=["POST"])
async def calculate_shit(request): 
    file = request.files.get("file")
    file_content = file.body.decode('utf-8')
    tokens = tokenize_text(file_content)
    types = get_types(tokens)
    result_dict = {
        "tokens" : len(tokens),
        "types" : len(types),
        "ttr" : len(tokens)/len(types),
    }
    return response.json(result_dict)

if __name__ == "__main__":
    app.run()