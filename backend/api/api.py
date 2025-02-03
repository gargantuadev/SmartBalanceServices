from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests

categories = []  # Temporary in-memory storage

@app.route('/categories', methods=['GET'])
def get_categories():
    return jsonify({"categories": categories})

@app.route('/categories', methods=['POST'])
def add_category():
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
