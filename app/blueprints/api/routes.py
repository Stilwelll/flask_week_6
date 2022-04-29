from . import api
from .auth import basic_auth, token_auth
from flask import jsonify, request
from app.blueprints.phonebook.models import PhoneBook


@api.route('/token')
@basic_auth.login_required
def get_token():
    user = basic_auth.current_user()
    token = user.get_token()
    return jsonify({'token': token, 'expiration': user.token_expiration})


# Get all posts
@api.route('/posts')
def get_posts():
    posts = PhoneBook.query.all()
    return jsonify([p.to_dict() for p in posts])


# Get a single post by id
@api.route('/posts/<int:post_id>')
def get_single_post(post_id):
    post = PhoneBook.query.get_or_404(post_id)
    return jsonify(post.to_dict())


# Create a post
@api.route('/posts/create', methods=['POST'])
@token_auth.login_required
def create_post():
    if not request.is_json:
        return jsonify({'error': 'Your request content-type must be application/json'}), 400
    # Get data from request body
    data = request.json
    # Check to make sure all required fields are present
    for field in ['title', 'body']:
        if field not in data:
            # if not return a 400 response with error
            return jsonify({'error': f'{field} must be in request body'}), 400
    # Get fields from data dict
    title = data['title']
    body = data['body']
    user_id = token_auth.current_user().id
    new_post = PhoneBook(title=title, body=body, user_id=user_id)
    return jsonify(new_post.to_dict())


@api.route('/posts/update/<int:post_id>', methods=['GET','PUT'])
@token_auth.login_required
def update_post(post_id):
    post = PhoneBook.query.get_or_404(post_id)
    if not request.is_json:
        return jsonify({'error': 'Your request content-type must be application/json'}), 400
    if post.author != token_auth.current_user():
        print('hello world')
        return jsonify({'error': 'you do not have access to edit this post'})
    data = request.json
    post.update(**data)

    return jsonify(post.to_dict())

@api.route('/posts/delete/<int:post_id>', methods=['DELETE'])
@token_auth.login_required
def delete_post(post_id):
    post = PhoneBook.query.get_or_404(post_id)
    print(post)
    if not request.is_json:
        return jsonify({'error': 'Your request content-type must be application/json'}), 400
    if post.author != token_auth.current_user():
        print('hello world')
        return jsonify({'error': 'you do not have access to delete this post'})
    else:
        post.delete()

    return jsonify({"deleted": "Post has been deleted."})