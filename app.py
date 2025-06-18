from flask import Flask, jsonify, request 
from productos import Productos
from flask_cors import CORS  
import random
app = Flask(__name__)
CORS(app) 

@app.route("/")
def home():
    return "Bienvenido a mi app !!!!!!"


@app.route("/listadoPro")
def listadoPro():
    return jsonify(Productos) 

@app.route("/registroPro", methods=["post"])
def registroPro():            
   
    if "nombre" in request.form and "precio" in request.form and "stock" in request.form:
        nombre = request.form["nombre"]
        precio = request.form["precio"]
        stock  = request.form["stock"]
        id      = random.randint(10,1000)
        # validar campos vacios
        # if nombre != "" and precio != ""
        Productos.append({
                        "id":id, 
                        "nombre":nombre, 
                        "precio":precio, 
                        "ip": request.remote_addr, 
                        "stock": stock})
        return jsonify({"mensaje":"Producto registrado correctamente"})
    else:
        return jsonify({"mensaje":"Faltan parametros en la peticion"}), 400
    
    


@app.route("/eliminarPro/<id>", methods=["delete"])
def eliminarPro(id):
    # if type(id) == int:
    try:
        id = int(id)
        for x in Productos:
            print(type(x["id"]))
            if x["id"] == id:
                Productos.remove(x)
                return jsonify({"mensaje":"Producto eliminado correctamente"})   
        
        return jsonify({"mensaje":"Producto no encontrado"})
    except:
        return jsonify({"mensaje":"id producto debe ser numerico"})

    # else:
    #     return jsonify({"mensaje":"id producto debe ser numerico"})


@app.route("/buscarPro/<id>")
def buscarPro(id):
    # if type(id) == int:
    try:
        id = int(id)
        for x in Productos:
            if x["id"] == id:
                # Productos.remove(x)
                return jsonify(x)   
        
        return jsonify({"mensaje":"Producto no encontrado"})
    except:
        return jsonify({"mensaje":"id producto debe ser numerico"})
    # else:
    #     return jsonify({"mensaje":"id producto debe ser numerico"})

@app.route("/editarPro/<id>", methods=["put"])
def editarPro(id):
    precio = request.form["precio"]
    stock  = request.form["stock"]
    nombre = request.form["nombre"]
    for x in Productos:
        if x["id"] == int(id):
            x["nombre"] = nombre
            x["precio"] = precio
            x["stock"]  = stock
            return jsonify({"mensaje":"Producto editado correctamente"})   
    
    return jsonify({"mensaje":"Producto no encontrado"})

# if __name__ == "__main__":
#     app.run(debug=True, port="3000", host="0.0.0.0")


# ip_cliente = request.remote_addr
