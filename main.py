import openai
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models import Question

OPENAI_API_KEY = ''
MODEL = 'gpt-3.5-turbo'
openai.api_key = OPENAI_API_KEY

app = FastAPI()
app.add_middleware(
    CORSMiddleware, 
    allow_origins='*',
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/question")
def read_root(params: Question):
    question = params.question
    prompt = params.feature
    #print(question, prompt)
    res = openai.ChatCompletion.create(
    model= MODEL,
    messages=[
        {"role": "system", "content": prompt},
        {"role": "user", "content": question},
        ]
    )

    answer = res.choices[0]['message']['content']
    return {"answer": answer}
