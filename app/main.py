import os
from fastapi import FastAPI

app = FastAPI(
    title="DevOps FastAPI Lab",
    description="API de exemplo para o LAB9 - CI/CD com Homologação e Produção",
    version="1.0.0",
)

ENVIRONMENT = os.getenv("ENVIRONMENT", "local")


@app.get("/")
def read_root():
    return {
        "message": "API FastAPI rodando com sucesso!",
        "environment": ENVIRONMENT,
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "environment": ENVIRONMENT,
    }
