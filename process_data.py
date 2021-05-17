import pandas as pd

from app.database import SessionLocal, Data, engine


def process_data():
    data: pd.DataFrame = pd.read_excel('tmp/pydev_test_task_data2.xlsx')

    data = data.sort_values('timestamp')

    conn = engine.connect()
    Data.create(engine)

    with SessionLocal() as session:
        conn.execute(Data.insert(), data.to_dict('records'))
        session.commit()


if __name__ == "__main__":
    process_data()
