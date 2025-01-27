from flask import Flask, request, jsonify
import time

app = Flask(__name__)

transactions = {}

@app.route('/initiate-transaction', methods=['POST'])
def initiate_transaction():
    data = request.json
    transaction_id = f"{int(time.time())}"
    transactions[transaction_id] = {"status": "pending", "details": data}
    return jsonify({"transaction_id": transaction_id}), 201

@app.route('/verify-transaction/<transaction_id>', methods=['GET'])
def verify_transaction(transaction_id):
    transaction = transactions.get(transaction_id)
    if not transaction:
        return jsonify({"error": "Transaction not found"}), 404
    return jsonify({"transaction_id": transaction_id, "details": transaction["details"]})

@app.route('/transaction-status/<transaction_id>', methods=['GET'])
def transaction_status(transaction_id):
    transaction = transactions.get(transaction_id)
    if not transaction:
        return jsonify({"error": "Transaction not found"}), 404

    # Simulate status change
    if transaction["status"] == "pending":
        transaction["status"] = "processing"
    elif transaction["status"] == "processing":
        transaction["status"] = "processed"
    return jsonify({"transaction_id": transaction_id, "status": transaction["status"]})

if __name__ == '__main__':
    app.run(port=5000)
