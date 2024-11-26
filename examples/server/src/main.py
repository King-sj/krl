from quart import Quart, request, jsonify

app = Quart(__name__)

# 存储数据的简单字典
data_store = {}


@app.route('/data', methods=['POST'])
async def post_data():
  data = await request.json
  print("data is :",data)
  key = data.get('key')
  value = data.get('value')
  if key and value:
    data_store[key] = value
    return jsonify({"message": "Data stored successfully"}), 201
  else:
    return jsonify({"error": "Invalid data"}), 201

@app.route('/data/<key>', methods=['GET'])
async def get_data(key):
  value = data_store.get(key)
  if value:
    return jsonify({key: value}), 200
  else:
    return jsonify({"error": "Not found"}), 404

@app.route('/weather', methods=['GET'])
async def weather():
  return jsonify({"climate": "好", "temp":"适宜"}), 200


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)
