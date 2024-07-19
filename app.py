# Import modules and packages
from flask import (
    Flask,
    request,
    render_template,
    url_for
)
import pickle
import numpy as np
import ipaddress
from scipy.spatial import distance

app = Flask(__name__)

@app.route('/')
def index():    
    return render_template('index.html')

@app.route('/', methods=['POST'])
def get_input_values():
    val = request.form['my_form']

@app.route('/predict', methods=['POST', 'GET'])
def predict():
    
    if request.method == 'GET':        
        return render_template('alerta.html')

    if request.method == 'POST':
        input_val = request.form

        if input_val != None:
            # collecting values
            vals = []
            valores = input_val.items()            
            for key, value in valores:                                 
                vals.append(value.strip())

            ips = ""
            vals = vals[0]
            direccionip = vals.split("\r\n")                          
            direccionips = ""

            if validate_ip_address(direccionip):
                direccionips = validate_ip_address(direccionip)        
                with open('ipbloqueadas.txt', 'a') as file:                       
                    for ip in direccionip:                   
                        file.write("\n"+ip)
            else:
                return render_template('error.html')

            return render_template(
                    'predict.html', result_value=f'Direccion IP : {direccionips}'
                )

def validate_ip_address(ip_string):
    try:        
        for x in ip_string:
            ip_object = ipaddress.ip_address(x.strip())                                
        return ip_string        
    except ValueError:             
        #return "El listado tiene un objeto incorrecto que no es una direccion IP valida. Por favor revisar"
        return False

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)