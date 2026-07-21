#!/usr/bin/python3

import csv
import json
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

def read_json(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)

def read_csv(filename):
    products = []
    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            row["id"] = int(row["id"])
            row["price"] = float(row["price"])
            products.append(row)
    return products

def read_sqlite(filename):
    conn = sqlite3.connect(filename)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Products")
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]

@app.route("/products")
def products():
    source = request.args.get("source")
    product_id = request.args.get("id")

    try:
        if source == "json":
            product_list = read_json("products.json")
        elif source == "csv":
            product_list = read_csv("products.csv")
        elif source == "sql":
            product_list = read_sqlite("products.db")
        else:
            return render_template(
                "product_display.html",
                error="Wrong source",
                products=[]
            )
    except sqlite3.Error:
        return render_template(
            "product_display.html",
            error="Database error",
            products=[]
        )
    if product_id is not None:
        try:
            product_id = int(product_id)
        except ValueError:
            return render_template(
                "product_display.html",
                error="Product not found",
                products=[]
            )
        product_list = [
            product for product in product_list
            if product["id"] == product_id
        ]
        if not product_list:
            return render_template(
                "product_display.html",
                error="Product not found",
                products=[]
            )
    return render_template(
        "product_display.html",
        products=product_list,
        error=None
    )

if __name__ == "__main__":
    app.run(debug=True, port=5000)