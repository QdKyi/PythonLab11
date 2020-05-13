from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from src.main.models.ice_axe import IceAxe
import os
import json
import copy

with open('secret.json') as f:
    SECRET = json.load(f)

DB_URI = "mysql+mysqlconnector://{user}:{password}@{host}:{port}/{db}".format(
    user=SECRET["user"],
    password=SECRET["password"],
    host=SECRET["host"],
    port=SECRET["port"],
    db=SECRET["db"])

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)


class IceClimbingAxe(IceAxe, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price_in_uah = db.Column(db.Integer, unique=False)
    weight = db.Column(db.Integer, unique=False)
    year_of_production = db.Column(db.Integer, unique=False)
    producer_name = db.Column(db.String(32), unique=False)
    sport_type = db.Column(db.String(32), unique=False)
    sharpness = db.Column(db.Integer, unique=False)

    def __init__(self, price_in_uah=0, weight=0,
                 year_of_production=0, producer_name='N/A',
                 sport_type=None, sharpness=0):
        super().__init__(price_in_uah, weight, year_of_production, producer_name, sport_type, sharpness)


class IceClimbingAxeSchema(ma.Schema):
    class Meta:
        fields = ('price_in_uah', 'weight', 'year_of_production', 'producer_name', 'sport_type', 'sharpness')


ice_axe_schema = IceClimbingAxeSchema()
ice_axe_schemas = IceClimbingAxeSchema(many=True)


@app.route("/ice_axe", methods=["POST"])
def create_equip():
    price_in_uah = request.json['price_in_uah']
    weight = request.json['weight']
    year_of_production = request.json['year_of_production']
    producer_name = request.json['producer_name']
    sport_type = request.json['sport_type']
    sharpness = request.json['sharpness']
    ice_axe_equip = IceClimbingAxe(price_in_uah, weight, year_of_production, producer_name, sport_type, sharpness)
    db.session.add(ice_axe_equip)
    db.session.commit()
    return ice_axe_schema.jsonify(ice_axe_equip)


@app.route("/ice_axe", methods=["GET"])
def get_equip():
    all_ice_axe_equip = IceClimbingAxe.query.all()
    result = ice_axe_schemas.dump(all_ice_axe_equip)
    return jsonify({'ice_axe_equip': result})


@app.route("/ice_axe/<id>", methods=["GET"])
def get_all_equip(id):
    ice_axe_equip = IceClimbingAxe.query.get(id)
    if not ice_axe_equip:
        abort(404)
    return ice_axe_schema.jsonify(ice_axe_equip)


@app.route("/ice_axe/<id>", methods=["PUT"])
def equip_update(id):
    ice_axe_equip = IceClimbingAxe.query.get(id)
    if not ice_axe_equip:
        abort(404)
    old_equip = copy.deepcopy(ice_axe_equip)
    ice_axe_equip.price_in_uah = request.json['price_in_uah']
    ice_axe_equip.weight = request.json['weight']
    ice_axe_equip.year_of_production = request.json['year_of_production']
    ice_axe_equip.producer_name = request.json['producer_name']
    ice_axe_equip.sport_type = request.json['sport_type']
    ice_axe_equip.sharpness = request.json['sharpness']
    db.session.commit()
    return ice_axe_schema.jsonify(old_equip)


@app.route("/ice_axe/<id>", methods=["DELETE"])
def equip_delete(id):
    smart_extreme_sport_equip = IceClimbingAxe.query.get(id)
    if not smart_extreme_sport_equip:
        abort(404)
    db.session.delete(smart_extreme_sport_equip)
    db.session.commit()
    return ice_axe_schema.jsonify(smart_extreme_sport_equip)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, host='127.0.0.1')
