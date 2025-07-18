from dotenv import load_dotenv
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from app.core.config import get_settings
from app.graphql.schema import schema
from fastapi import Response

load_dotenv()
settings = get_settings()

# instancia FastAPI
app = FastAPI()

# ✅ monta GraphQL en /graphql
graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix="/graphql")

# endpoint de salud
@app.get("/health")
async def health() -> Response:
    return {
        "status": "ok",
        "database_url": settings.database_url
    }
