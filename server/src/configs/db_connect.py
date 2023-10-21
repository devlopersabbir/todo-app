from src.configs.databse import Base, engine


def db_connect():
    try:
        Base.metadata.create_all(bind=engine)
        print("Successfully connect db!")
    except Exception as err:
        print("Fail to connect!")
        print(err)
