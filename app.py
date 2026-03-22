from flask import Flask, render_template, jsonify, abort

from data import MODULES

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/modules")
def get_modules():
    summary = []
    for slug, m in MODULES.items():
        summary.append({
            "slug": slug,
            "name": m["name"],
            "domain": m["domain"],
            "tagline": m["tagline"],
            "color": m["color"],
            "description": m["description"],
        })
    return jsonify(summary)


@app.route("/api/modules/<slug>")
def get_module(slug):
    module = MODULES.get(slug)
    if not module:
        abort(404)
    return jsonify(module)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
