from quart import Quart, request, jsonify
from quart_cors import cors
from gen_krl import gen_krl
import threading
import copy
from arg import args
from user import User
from typing import Dict
from uuid import UUID
from api_type import *
from time import sleep

app = Quart(__name__)
app = cors(app, allow_origin="*")  # 启用cors, 允许所有来源
krl = gen_krl()
users: Dict[UUID, User] = dict()


@app.route('/', methods=['GET'])
async def helloworld():
  return jsonify({"res": "welcome"}), 200


@app.route('/create_user', methods=['POST'])
async def create_user():
  user = User(copy.deepcopy(krl))
  users[user.id] = user
  user.thread = threading.Thread(target=user.interpreter.run)
  user.thread.start()
  # sleep for a while
  while not user.interpreter.is_output_ready():
    sleep(0.1)
  return jsonify({
      "user_id": str(user.id),
      "res": user.interpreter.get_output(),
  }), 200


@app.route('/run', methods=['POST'])
async def run():
  """
Handle POST requests to the /run endpoint.

This asynchronous function processes user input, interacts with the user's interpreter,
and returns the output once it is ready.

Request Body:
-------------
- data (UserInput): A JSON object containing the following fields:
  - user_id (str): The unique identifier of the user.
  - input (str): The input string to be processed by the user's interpreter.

Returns:
--------
- Response (json): A JSON response containing the following fields:
  - res (str): The output from the user's interpreter.
  - code (int): Status code (0 for success).
  - msg (str): A message indicating the success of the operation.

Status Code:
------------
- 200: If the request is processed successfully.

Raises:
-------
- KeyError: If the user_id is not found in the users dictionary.
- Exception: If there is an error during the processing of the input.
"""
  data: UserInput = await request.get_json()
  user_id = data["user_id"]
  user = users[UUID(user_id)]
  user.interpreter.put_input(data["input"])
  # sleep for a while
  while not user.interpreter.is_output_ready():
    sleep(0.1)
  res: Response = {
      "res": user.interpreter.get_output(),
      "code": 0,
      "msg": "success"
  }
  return jsonify(res), 200


if __name__ == '__main__':
  app.run(host=args.host, port=args.port, debug=args.debug)
