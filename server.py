from flask import Flask, request, jsonify
from secrets import token_hex
from ton_client.client import TonlibClientFutures
app = Flask(__name__)

ton = TonlibClientFutures()

@app.route('/api/gen-key',methods=["POST"])
def gen_key():
  seed = request.json['seed']
  res = ton.create_new_key(seed)
  return jsonify(res.result())

@app.route('/api/get-account-state',methods=["POST"])
def get_account_state():
  addr = request.json['address']
  res = ton.raw_get_account_state(addr)
  return jsonify(res.result())
