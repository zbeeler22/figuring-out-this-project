from flask import Blueprint, request, jsonify, make_response, current_app, app
import json
from src import db


socialuser = Blueprint('socialuser', __name__)

# Get all usernames from the DB
@socialuser.route('/socialuser/allUsers', methods=['GET'])
def get_usernames():
    cursor = db.get_db().cursor()
    cursor.execute('select username from user')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Get all information for user with particular UserId
@socialuser.route('/socialuser/<UserId>', methods=['GET'])
def get_user_info(UserId):
    cursor = db.get_db().cursor()
    cursor.execute('select * from user where UserId = {0}'.format(UserId))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response 

# Get all posts for user with particular UserId
@socialuser.route('/socialuser/getposts/<UserId>', methods=['GET'])
def get_post_info(UserId):
    cursor = db.get_db().cursor()
    cursor.execute('select * from post where UserId = {0}'.format(UserId))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response 

# Get blocking status given a FollowerId
@socialuser.route('/socialuser/blocked/<FollowerId>', methods=['GET'])
def get_blocked(FollowerId):
    cursor = db.get_db().cursor()
    cursor.execute('select blocking_status from friend where FollowerId= {0}'.format(FollowerId))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response 

# Get photos given a PostId
@socialuser.route('/socialuser/photos/<PostId>', methods=['GET'])
def get_photos(PostId):
    cursor = db.get_db().cursor()
    cursor.execute('select photo from pictures where PostId= {0}'.format(PostId))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response 

# Get comments given a PostId
@socialuser.route('/socialuser/comments/<PostId>', methods=['GET'])
def get_comments(PostId):
    cursor = db.get_db().cursor()
    cursor.execute('select text from comment where PostId= {0}'.format(PostId))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response 

# Get comments given a PostId
@socialuser.route('/socialuser/reactions/<PostId>', methods=['GET'])
def get_reactions(PostId):
    cursor = db.get_db().cursor()
    cursor.execute('select type from reaction where PostId= {0}'.format(PostId))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Post information about new user
@socialuser.route('/socialuser', methods=['POST'])
def add_new_user():
     
     # collecting data from the request object
     the_data = request.json
     current_app.logger.info(the_data)


     # extracting the variable
     username = the_data['username']
     first_name = the_data['first_name']
     last_name = the_data['last_name']
     email = the_data['email']
     password = the_data['password']
     bio = the_data['bio']
     profile_pic = the_data ['profile_pic']
     
     # constructing the query
     query = 'insert into user (username, first_name, last_name, email, password, bio, profile_pic) values ("'
     query += username + '", "'
     query += first_name + '", "'
     query += last_name + '", "'
     query += email + '", "'
     query += password + '", "'
     query += bio + '", "'
     query += profile_pic + '")'
     current_app.logger.info(query) 
     
     # executing and committing the insert statement
     cursor = db.get_db().cursor()
     cursor.execute(query)
     db.get_db().commit()

     return 'Success!'

# Put - Update user bio given UserId
@socialuser.route('/socialuser/bio/<UserId>', methods=['PUT'])
def update_bio(UserId):
     
    # collecting data from the request object
    the_data = request.json
     
    # extracting the variable
    bio = the_data['bio']

    # constructing the query
    query = 'UPDATE user SET bio = %s WHERE UserId = %s'

    current_app.logger.info(query)

    # executing and committing
    cursor = db.get_db().cursor()
    cursor.execute(query, (bio, UserId))
    db.get_db().commit()

    # Return updated user data
    return 'User bio updated successfully!'

if __name__ == '__main__':
    app.run(debug=True)

# Delete user given a UserId
@socialuser.route('/socialuser/deleteuser/<UserId>', methods=['DELETE'])
def delete_user(UserId):
    # constructing the query
    query = 'DELETE FROM user WHERE UserId = %s'

    current_app.logger.info(query)

    # executing and committing
    cursor = db.get_db().cursor()
    cursor.execute(query, (UserId))
    db.get_db().commit()

    # Return updated user data
    return 'User deleted successfully!'


