from fastapi import FastAPI, HTTPException
import uuid0
from pydantic import BaseModel

from fastapi.middleware.cors import CORSMiddleware

from config import supabase

app = FastAPI()

origins = [
    "https://farmstack-ykusf.run.goorm.io",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_root():
    return {"Hello": "World"}

class CommentIn(BaseModel):
    name:str
    email:str
    body:str

class CommentOut(BaseModel):
    id:str
    createAt:str
        

@app.get("/comment")
async def select():
    try:
        res = supabase.table("comments").select("*").execute()
        if(res['status_code']==200):
            return res['data']
        else:
            data = res['data']
            return data['message']
        return "GOT"
    except:
        raise HTTPException(500, "Internal Server Error")

@app.post("/comment",response_model=CommentOut,status_code=201)
async def insert(commentIn:CommentIn):
    try:
        body = commentIn.dict()
        data = supabase.table("comments").insert(body).execute()
        uuid = uuid0.generate()
        commentOut = CommentOut(id=str(uuid.base62),createAt=str(uuid.datetime))
        return commentOut.dict()
    except:
        raise HTTPException(500, "Internal Server Error")

    
    
    
    
    
