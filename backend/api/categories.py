from flask import Blueprint, jsonify, request

# Create a blueprint for categories
categories_bp = Blueprint("categories", __name__)

# Temporary in-memory storage for categories
categories = []

@categories_bp.route('/get-categories', methods=['GET'])
def get_categories():
    """Fetch all categories."""
    return jsonify({"categories": categories})

@categories_bp.route('/add-category', methods=['POST'])
def add_category():
    """Add a new category."""
    data = request.get_json()
    category_name = data.get('name')
    selected_icon = data.get('icon')
    selected_color = data.get('color')

    if not category_name:
        return jsonify({"error": "Category name is required"}), 400

    new_category = {
        "name": category_name,
        "icon": selected_icon,
        "color": selected_color
    }
    categories.append(new_category)
    return jsonify({"message": "Category created successfully", "category": new_category}), 201
