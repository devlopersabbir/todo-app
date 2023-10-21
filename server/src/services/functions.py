from sqlalchemy.orm import Session


def find_by_name(query_db: Session, query_model, name: str):
    return query_db.query(query_model).filter(query_model.name == name).first()
