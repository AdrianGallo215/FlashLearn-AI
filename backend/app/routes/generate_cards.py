from ..main import app

@app.route('/generate_cards', methods=['POST'])
def generate_cards():
    data = request.get_json()

    