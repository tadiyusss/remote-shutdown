from flask import Flask, render_template, request
import os
import sys

app = Flask(__name__)
pin = '0115'


@app.route('/')
def index():
    return render_template('dashboard.html')

@app.route('/shutdown', methods=['POST'])
def shutdown():
    if request.form.get('pin') == pin:
        os.system('shutdown -s -t {}'.format(int(request.form.get('time'))))
        return {
            'status': 'Shutting down'
        }
    else:
        return {
            'status': 'Invalid pin'
        }
if '-d' in sys.argv: 
    app.run(host='0.0.0.0', port=5000, debug=True)
else:
    app.run(host='0.0.0.0', port=5000)