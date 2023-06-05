from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models import Question

app = FastAPI()
app.add_middleware(
    CORSMiddleware, 
    allow_origins='*',
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post('/question')
def sendquestion(question: Question):
    try:
        # generating answer for question
        question = question.question
        res = "answer the question"
    except HTTPException as e:
        print("Question not found")
    return {'result': res}