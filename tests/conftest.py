# tests/conftest.py
import pytest
from fastapi.testclient import TestClient
from sqlmodel import Session, SQLModel, create_engine
from app.main import app
from app.core.config import get_settings
from app.db.session import get_session

# URL de la base de datos de pruebas
TEST_DATABASE_URL = "postgresql://testuser:testpass@localhost:5434/vana_planner_test"

# Crear un motor de base dedatos síncrono solo para la configuración/limpieza
engine = create_engine(TEST_DATABASE_URL)


# Fixture para crear una sesión de prueba y limpiar la base de datos
@pytest.fixture(name="session")
def session_fixture():
    SQLModel.metadata.create_all(engine)  # Crea las tablas
    with Session(engine) as session:
        yield session
    SQLModel.metadata.drop_all(engine)  # Borra las tablas después de las pruebas


# Fixture para el cliente de prueba de FastAPI
@pytest.fixture(name="client")
def client_fixture(session: Session):
    def get_session_override():
        return session

    # Reemplaza la dependencia get_session con la versión de prueba
    app.dependency_overrides[get_session] = get_session_override
    yield TestClient(app)
    
    # Limpia el override después de las pruebas
    app.dependency_overrides.clear()