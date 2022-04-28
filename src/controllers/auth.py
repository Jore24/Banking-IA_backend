from flask import request, jsonify
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash
from src.connection.db import db
from bson.objectid import ObjectId


def user_login():
    card = request.json['card']
    dni = request.json['dni']
    password = request.json['password']

    try:
        user = db.users.find_one({"card": card, "dni": dni})
        if user is None:
            return jsonify({"ok": bool("false"), "msg": "User not found"}), 404
        if not(check_password_hash(user['password'], password)):
            return jsonify({"msg": "Invalid password"}), 401

        response = {
            "ok": True,
            "id": str(user['_id']),
            "fullname": user['fullname'],
        }
        return response, 200
    except Exception as e:
        return jsonify({"ok": False, "msg": e}), 500


def user_register():
    img = request.file['img']
    card = request.json['card']
    fullname = request.json['fullname']
    email = request.json['email']
    dni = request.json['dni']
    password = request.json['password']
    print(img)
    try:
        user = db.users.find_one({"email": email})
        if user:
            return jsonify({"ok": False, "msg": "User already exists"}), 400

        hashed_password = generate_password_hash(password)
        db.users.insert_one(
            {"img": img, "card": card, "fullname": fullname, "email": email, "dni": dni, "password": hashed_password})

        return jsonify({"ok": True, "msg": "User created successfully"}), 201
    except Exception as e:
        return jsonify({"ok": False, "msg": e}), 500
