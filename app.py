from flask import Flask, render_template, request, send_file
import asyncio
import os

from agent.agent_ppt import run_ppt_agent

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        topic = request.form.get("topic")

        # Run your agent
        asyncio.run(run_ppt_agent(topic))

        # Find latest PPT
        folder = "presentations"
        files = sorted(
            [f for f in os.listdir(folder) if f.endswith(".pptx")],
            key=lambda x: os.path.getmtime(os.path.join(folder, x)),
            reverse=True
        )

        latest_file = os.path.join(folder, files[0])

        return send_file(latest_file, as_attachment=True)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)