
from flask import Flask, render_template, jsonify
from Controllers.fetch import setup_driver,fetch_trends

app = Flask(__name__)



@app.route("/")
def start():
    return render_template("index.html")

@app.route("/trends")
def find_trends():
    try:
        driver = setup_driver()
        trends = fetch_trends(driver)
        return jsonify(trends)
    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({"error": "Unable to fetch trends"}), 500

if __name__ == "__main__":
    app.run(debug=True)
