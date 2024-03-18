from flask import Flask, render_template, request
import socket

app = Flask(__name__)

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1) 
        result = sock.connect_ex((ip, port))
        sock.close()
        return result == 0
    except:
        return False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan():
    target_ip = request.form['ip']
    start_port = int(request.form['start_port'])
    end_port = int(request.form['end_port'])
    open_ports = []

    for port in range(start_port, end_port + 1):
        if scan_port(target_ip, port):
            open_ports.append(port)

    return render_template('index.html', ip=target_ip, open_ports=open_ports)

if __name__ == '__main__':
    app.run(debug=True)
