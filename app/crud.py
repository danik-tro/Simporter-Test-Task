from datetime import datetime, date

import numpy as np

from .database import SessionLocal, Data, engine
from .schema import TimelineQuery, Grouping, Type

from sqlalchemy import and_
import pandas as pd


def info():
    """
    Unique values for each attribute
    :return:
    """
    with SessionLocal() as session:
        return {name: [i[0] for i in session.query(column).distinct(column).all()]
                for column, name in zip(
                (Data.c.asin, Data.c.brand, Data.c.source, Data.c.stars),
                ('asin', 'brand', 'source', 'stars')
            )}


def aggregation(df: pd.DataFrame, query: TimelineQuery):
    """
    Aggregation of data depending on filters
    :param df: dataframe ready for grouping
    :param query: query params
    :return: Grouping data by a specified time interval
    """
    df = df.set_index(['timestamp'])
    df.index = pd.to_datetime(df.index, unit='s')

    freq = 'M'
    if query.Grouping == Grouping.weekly:
        freq = 'W'
    elif query.Grouping == Grouping.bi_weekly:
        freq = '2W'

    result = df.resample(freq).agg(
        {'id': 'count'})

    if query.Type == Type.cumulative:
        result.loc[:, 'id'] = np.cumsum(result.loc[:, ['id']].to_numpy())

    return {'timeline': [
        {"date": str(date), "value": value}
        for date, value in zip(result.index.date, result['id'].to_list())
    ]}


def timeline(query: TimelineQuery):
    """
    Preparing data for grouping. Applying Filters
    :param query: query params
    :return: Aggregated data
    """
    select_query = Data.select(
        and_(datetime(*query.start_date.timetuple()[:-4]).timestamp() <= Data.c.timestamp,
             datetime(*query.end_date.timetuple()[:-4]).timestamp() >= Data.c.timestamp)
    )

    if query.asin is not None:
        select_query = select_query.where(
            Data.c.asin.in_(query.asin)
        )

    if query.brand is not None:
        select_query = select_query.where(
            Data.c.brand.in_(query.brand)
        )

    if query.source is not None:
        select_query = select_query.where(
            Data.c.source.in_(query.source)
        )

    if query.stars is not None:
        select_query = select_query.where(
            Data.c.stars.in_(query.stars)
        )

    return aggregation(
        pd.read_sql(
            select_query,
            engine
        ),
        query
    )
