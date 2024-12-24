from quart import Quart, request, jsonify

app = Quart(__name__)
users = {}
@app.route('/query', methods=['POST'])
def query():
  pass
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)
