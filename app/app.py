from flask import Flask, request, jsonify
from flask_pydantic import validate

from .crud import info, timeline
from .schema import TimelineQuery


app = Flask(__name__)


@app.route('/api/info')
def api_info():
    """
    :return: Returning existing filters and their values
    """
    return jsonify(info())


@app.route('/api/timeline', methods=['GET'])
@validate(query=TimelineQuery)
def api_timeline(query: TimelineQuery):
    """
    :return: Grouping data using filters
    """

    return jsonify(timeline(query))


@app.errorhandler(404)
def error(e):
    return jsonify({'message': 'not path'})
