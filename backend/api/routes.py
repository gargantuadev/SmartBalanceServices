from flask import Blueprint, jsonify, request
#from .firestore_service import get_categories, add_category

api_bp = Blueprint("api", __name__)

@api_bp.route('/categories', methods=['GET'])
def get_categories_route():
    """Fetch all categories."""
    #categories = get_categories()
    categories = {}
    return jsonify({"categories": categories})

@api_bp.route('/categories', methods=['POST'])
def add_category_route():
    """Add a new category."""
    data = request.get_json()
    category_name = data.get('name')
    selected_icon = data.get('icon')
    selected_color = data.get('color')

    if not category_name:
        return jsonify({"error": "Category name is required"}), 400

    category_data = {
        "name": category_name,
        "icon": selected_icon,
        "color": selected_color
    }

    #new_category = add_category(category_data)
    new_category = category_data
    return jsonify({"message": "Category created successfully", "category": new_category}), 201
