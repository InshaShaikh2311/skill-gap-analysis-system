from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# ---------------- HOME ----------------
@app.route("/")
def home():

    return render_template("base.html")


# ---------------- PAST ----------------
@app.route("/past")
def past():

    df = pd.read_csv(
        "data/processed/industry_cleaned.csv"
    )

    table = df.head(20).to_html(
        classes="table",
        index=False
    )

    return render_template(
        "past.html",
        table=table
    )


# ---------------- GAP ----------------
@app.route("/gap")
def gap():

    df = pd.read_csv(
        "data/processed/gap_analysis.csv"
    )

    table = df.head(20).to_html(
        classes="table",
        index=False
    )

    return render_template(
        "gap.html",
        table=table
    )


# ---------------- FUTURE ----------------
@app.route("/future")
def future():

    df = pd.read_csv(
        "data/processed/future_predictions.csv"
    )

    table = df.to_html(
        classes="table",
        index=False
    )

    return render_template(
        "future.html",
        table=table
    )


# ---------------- RUN ----------------
if __name__ == "__main__":

    app.run(debug=False)