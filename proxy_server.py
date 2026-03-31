# proxy_server.py
from flask import Flask, request, jsonify
from openai import OpenAI

app = Flask(__name__)

client = OpenAI(
    base_url="BASE_URL",
    api_key="API_KEY"
)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    messages = data.get('messages')
    model = data.get('model', 'MODEL_NAME')
    if not messages:
        return jsonify({'error': 'Missing messages'}), 400
    try:
        response = client.chat.completions.create(
            model=model,
            messages=messages
        )
        content = response.choices[0].message.content
        return jsonify({'content': content})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)