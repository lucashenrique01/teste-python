from flask import Flask, request
from flask_sslify import SSLify
import ssl

app = Flask(__name__)
sslify = SSLify(app)

@app.route('/process-json', methods=['POST'])
def process_json():
    try:
        data = request.get_json()  # Obtém o JSON enviado na requisição
        print("JSON Recebido:")
        print(data)
        return {"message": "JSON recebido com sucesso!"}
    except Exception as e:
        return {"error": str(e)}, 400

if __name__ == '__main__':
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    context.load_cert_chain('cert.pem', 'key.pem')  # Substitua pelos caminhos para o seu certificado e chave
    app.run(host='0.0.0.0', port=443, ssl_context=context)
