from flask import Flask, jsonify, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

############ Hack 1  ############
@app.route("/users", methods=["GET"])
def fn_get_users():
          
    
    return jsonify({
        "payload":"success"
    })

############ Hack 2  ############
@app.route("/user", methods=["POST"])
def fn_add_user():
    email = 'maria.perez@gmail.com'
    name = 'Maria'
    id = 1
    'INSERT INTO users (email, name, id) values (%s, %s, %s)'

    return jsonify({
        "payload":"success"
    })

############ Hack 3  ############
@app.route("/user", methods=["DELETE"])
def fn_delete_user():
    email = 'maria.perez@gmail.com'

    'DELETE FROM users WHERE email =%s', (email,)
    
    return jsonify({
        "payload":"success"
    })


############ Hack 4  ############
@app.route("/user", methods=["PUT"])
def fn_update_user():
    email = 'maria.perez@gmail.com'
    name = 'Maria'
    id = 1
    
    'UPDATE users set name =%s, email =%s, id =%s WHERE id = 1', (name, email, id,)
    return jsonify({
        "payload":"success",
        "error": False
    })

############ Hack 5  ############
@app.route("/api/v1/users", methods=["GET"])
def fn_consulta_users():
    email = 'maria.perez@gmail.com'
    'SELECT * FROM users WHERE email =%s', (email,)
       
    return jsonify({
        "payload":[]
    })

############ Hack 6  ############
@app.route('/api/v1/user', methods=['POST'])
def fn_api_user():
    email = request.args.get("email")
    name = request.args.get("name")


    return jsonify({
        "payload":{
            "email":email,
            "name":name,
        }
    })

############ Hack 7  ############

@app.route("/api/v1/user/add", methods=["POST"])
def fn_api_add():

    email = request.form.get("email")   
    name = request.form.get("name")
    id = request.form.get("id")
   

    return jsonify({
        "payload":  {
            'email':email,
            'name':name,
            'id':id,
        }
    })

############ Hack 8  ############
@app.route("/api/v1/user/create", methods=["POST"])
def fn_api_create():

    data = request.get_json()
    return jsonify({
        "payload":  {
            'email':data['email'],
            'name':data['name'],
            'id':data['id'],
        }
     })



if __name__ == "__main__":
    app.run(debug=True)