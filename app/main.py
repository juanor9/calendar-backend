from fastapi import FastAPI
from dotenv import load_dotenv
from app.core.config import get_settings
from strawberry.fastapi import GraphQLRouter
from app.graphql.schema import schema

load_dotenv()
settings = get_settings()

# instancia FastAPI
app = FastAPI()

# ✅ monta GraphQL en /graphql
graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix="/graphql")

# endpoint de salud
@app.get("/health")
async def health():
    return {
        "status": "ok",
        "database_url": settings.database_url
    }
