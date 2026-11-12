from fastapi import FastAPI
klu=FastAPI(title="AI-Tutor",
            description="AI Tutor Pbl project",
            version="1.0.0")
@klu.get("/")
def home():
    return {"message":"Welcome to AI Tutor Project"}
@klu.get("/demo")
def demo():
    return {"message":"KL University"}
@klu.get("/ask question")
def ask():
    return {"message":"What is LLM","Answer":"LLM is a Large Language Model"}
@klu.get("/student")
def student():
    return {"id":1,"name":"ram","gender":"male","course":"dsa"}   
@klu.get("/students")
def getstudents():
    return [{"id":1,"name":"ram","gender":"male","course":"dsa"},
            {"id":2,"name":"klu","gender":"male","course":"dsa"},
            {"id":3,"name":"seetha","gender":"female","course":"dsa"}]