from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from tensorflow.compat.v1 import reset_default_graph
import gpt_2_simple as gpt2

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/")
def index():
    return {"greeting": "Hello world"}

@app.get("/comedian")
def robecca_lines(prefix):
    reset_default_graph()
    sess = gpt2.start_tf_sess()
    gpt2.load_gpt2(sess, run_name='robecca')

    lines = gpt2.generate(sess,
              return_as_list=True,
              length=100, # output length
              run_name='robecca',
              prefix = str(prefix), #arg for text prompt
              temperature=0.8, #randomness
              nsamples=3, # amount of samples
              batch_size=3 # batch size
             )

    clean_lines = []
    for line in lines:
        if '. ' in line:
            line_list = line.split('. ')
            del line_list[-1]
            clean_line = '. '.join(line_list)
            clean_line = clean_line + '.'
            clean_lines.append(clean_line)
        else:
            clean_lines.append(line)

    return {
        "lines": clean_lines
        }
