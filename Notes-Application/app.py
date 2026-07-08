from flask import Flask, render_template, request, jsonify
from models.notes import create_notes_table, create_note

create_notes_table()

app = Flask(__name__)

@app.route("/")
@app.route("/form")
def form_page():
    return render_template("notes.html")


@app.route("/api/form", methods=["POST"])
def form_route():
    data = request.get_json()
    if data is None:
        return jsonify({"error":"Invalid JSON payload."}), 400

    title = data.get("title")
    content = data.get("content")

    if title and content:
        create_note(title, content)
        return jsonify({"success":"Note successfully added."}), 200
    
    return jsonify({"error":"Please fill in all the fields!"}), 400


app.run(debug=True)