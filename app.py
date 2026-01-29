from flask import Flask, render_template, request
from agent import analyze_trip
from data.city_cost_data import get_all_countries

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        return render_template(
            "select_city.html",
            country=request.form["country"],
            days=request.form["days"],
            budget=request.form["budget"],
            style=request.form["style"],
            cities=["Capital City"]  # placeholder (logic-safe)
        )

    return render_template("index.html", countries=get_all_countries())

@app.route("/analyze", methods=["POST"])
def analyze():
    result = analyze_trip(
        request.form["country"],
        request.form["city"],
        int(request.form["days"]),
        int(request.form["budget"]),
        request.form["style"]
    )

    return render_template(
        "result.html",
        country=request.form["country"],
        city=request.form["city"],
        days=request.form["days"],
        budget=request.form["budget"],
        style=request.form["style"],
        result=result
    )

if __name__ == "__main__":
    app.run(debug=True)
