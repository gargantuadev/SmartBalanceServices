from flask import Blueprint, jsonify, request, current_app
from flask_sqlalchemy import SQLAlchemy

# Create a blueprint for categories
categories_bp = Blueprint("categories", __name__)

# Get the SQLAlchemy instance from the app
db = current_app.config["DB"]

# Define the Category model
class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # Unique ID
    user_email = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    icon = db.Column(db.String(100))
    color = db.Column(db.String(20))

    # Unique constraint to prevent duplicate categories per user
    __table_args__ = (db.UniqueConstraint('user_email', 'name', name='unique_user_category'),)

    def to_dict(self):
        return {
            "id": self.id,
            "user_email": self.user_email,
            "name": self.name,
            "icon": self.icon,
            "color": self.color
        }

# Get all categories for a specific user
@categories_bp.route('/get', methods=['GET'])
def get_categories():
    user_email = request.args.get("userEmail")
    if not user_email:
        return jsonify({"error": "User email is required"}), 400

    categories = Category.query.filter_by(user_email=user_email).all()
    return jsonify({"categories": [category.to_dict() for category in categories]})

# Add a new category (Enforcing Unique Constraint)
@categories_bp.route('/add', methods=['POST'])
def add_category():
    data = request.get_json()
    category_name = data.get('name')
    selected_icon = data.get('icon')
    selected_color = data.get('color')
    user_email = data.get('userEmail')

    if not category_name or not user_email:
        return jsonify({"error": "Category name and user email are required"}), 400

    # Check if the category already exists for this user
    existing_category = Category.query.filter_by(user_email=user_email, name=category_name).first()
    if existing_category:
        return jsonify({"error": "Category already exists for this user"}), 409  # HTTP 409 Conflict

    try:
        new_category = Category(
            name=category_name, 
            icon=selected_icon, 
            color=selected_color, 
            user_email=user_email
        )
        db.session.add(new_category)
        db.session.commit()
        return jsonify({"message": "Category created successfully", "category": new_category.to_dict()}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "An error occurred while creating the category", "details": str(e)}), 500

# Delete a category
@categories_bp.route('/delete', methods=['DELETE'])
def delete_category():
    data = request.get_json()
    category_name = data.get("name")
    user_email = data.get("userEmail")

    if not category_name or not user_email:
        return jsonify({"error": "Category name and user email are required"}), 400

    category = Category.query.filter_by(user_email=user_email, name=category_name).first()

    if not category:
        return jsonify({"error": "Category not found"}), 404

    db.session.delete(category)
    db.session.commit()
    return jsonify({"message": "Category deleted successfully"}), 200

# Update a category
@categories_bp.route('/update', methods=['PUT'])
def update_category():
    data = request.get_json()
    category_name = data.get("name")
    user_email = data.get("userEmail")
    new_icon = data.get("icon")
    new_color = data.get("color")

    if not category_name or not user_email:
        return jsonify({"error": "Category name and user email are required"}), 400

    category = Category.query.filter_by(user_email=user_email, name=category_name).first()

    if not category:
        return jsonify({"error": "Category not found"}), 404

    category.icon = new_icon if new_icon else category.icon
    category.color = new_color if new_color else category.color

    db.session.commit()
    return jsonify({"message": "Category updated successfully", "category": category.to_dict()}), 200



"""from flask import Blueprint, jsonify, request

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
    return jsonify({"message": "Category created successfully", "category": new_category}), 201"""
