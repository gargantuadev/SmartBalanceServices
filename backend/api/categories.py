from flask import Blueprint, jsonify, request

# Create a blueprint for categories
categories_bp = Blueprint("categories", __name__)

# TODO: remove this, Temporary in-memory storage for categories
categories = []

@categories_bp.route('/get', methods=['GET'])
def get_categories():
    # TODO: this will need to be modified to get categories for a specific user
    return jsonify({"categories": categories})

@categories_bp.route('/add', methods=['POST'])
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
    return jsonify({"message": "Category created successfully", "category": new_category}), 201
