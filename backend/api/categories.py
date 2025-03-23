from flask import Blueprint, jsonify, request
from sqlalchemy.orm import Session
from .db import SessionLocal
from .models import Category

# Create a blueprint for categories
categories_bp = Blueprint("categories", __name__)


@categories_bp.route('/get', methods=['GET'])
def get_categories():
    user_email = request.args.get('userEmail')  # Assuming email comes from query param

    if not user_email:
        return jsonify({"error": "User email is required"}), 400

    with SessionLocal() as db:
        categories = db.query(Category).filter_by(user_email=user_email).all()
        result = [
            {
                "id": c.id,
                "name": c.name,
                "icon": c.icon,
                "color": c.color,
                "user_email": c.user_email
            }
            for c in categories
        ]
        return jsonify({"categories": result})


@categories_bp.route('/add', methods=['POST'])
def add_category():
    data = request.get_json()
    category_name = data.get('name')
    selected_icon = data.get('icon')
    selected_color = data.get('color')
    user_email = data.get('userEmail')

    if not category_name or not user_email or not selected_icon or not selected_color:
        return jsonify({"error": "Category name, icon, color and user email are required"}), 400

    new_category = Category(
        name=category_name,
        icon=selected_icon,
        color=selected_color,
        user_email=user_email
    )

    with SessionLocal() as db:
        db.add(new_category)
        db.commit()
        db.refresh(new_category)

        return jsonify({
            "message": "Category created successfully",
            "category": {
                "id": new_category.id,
                "name": new_category.name,
                "icon": new_category.icon,
                "color": new_category.color,
                "user_email": new_category.user_email
            }
        }), 201


"""@categories_bp.route('/add', methods=['POST'])
def add_category():
    # TODO: this will need to be modify with the user
    data = request.get_json()
    category_name = data.get('name')
    selected_icon = data.get('icon')
    selected_color = data.get('color')
    user_email = data.get('userEmail')

    if not category_name:
        return jsonify({"error": "Category name is required"}), 400

    new_category = {
        "name": category_name,
        "icon": selected_icon,
        "color": selected_color,
        "user_email": user_email
    }
    categories.append(new_category)
    
    return jsonify({"message": "Category created successfully", "category": new_category}), 201"""
