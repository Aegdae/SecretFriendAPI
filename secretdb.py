from sqlalchemy import create_engine

Database_engine = create_engine(
    "postgresql://postgres:jonnathas1524@127.0.0.1/Amigo_Secreto",
    pool_reset_on_return=None,
)