from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route("/2023-10/marketing-solutions/portfolios", methods=["GET"])
def mock_portfolios():
    return jsonify({
        "data": [
            {"id": "1234", "attributes": {"name": "Advertiser A"}},
            {"id": "5678", "attributes": {"name": "Advertiser B"}}
        ]
    })

@app.route("/2023-10/audiences", methods=["POST"])
def mock_create_audience():
    body = request.json
    return jsonify({
        "data": {
            "id": "9999",
            "attributes": {"name": body['data']['attributes']['name'], "advertiserId": body['data']['attributes']['advertiserId']}
        }
    }), 201

@app.route("/2023-10/audiences", methods=["GET"])
def mock_search_audience():
    advertiser_id = request.args.get("advertiserIds")
    return jsonify({
        "data": [
            {"id": "1111", "attributes": {"name": "Segment A", "advertiserId": advertiser_id}},
            {"id": "2222", "attributes": {"name": "Segment B", "advertiserId": advertiser_id}}
        ]
    })

if __name__ == "__main__":
    app.run(port=5000)
