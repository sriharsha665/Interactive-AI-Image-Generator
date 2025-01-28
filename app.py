import os
import requests
from flask import Flask, render_template, request, send_file
from time import time

app = Flask(__name__)

# Hugging Face API Key
API_URL = "https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-dev"
API_KEY = "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"

# Function to query Hugging Face API
def query_huggingface_api(prompt):
    headers = {"Authorization": f"Bearer {API_KEY}"}
    payload = {"inputs": prompt}
    response = requests.post(API_URL, headers=headers, json=payload)
    
    if response.status_code != 200:
        raise Exception(f"Error: {response.json()}")
    
    return response.content  # Assuming binary image data is returned.

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        prompt = request.form.get("prompt")
        if not prompt:
            return render_template("indexx.html", error="Prompt cannot be empty.")

        try:
            # Generate image from the Hugging Face API
            image_data = query_huggingface_api(prompt)
            
            # Save the image with a unique filename
            timestamp = int(time())
            image_filename = f"generated_image_{timestamp}.png"
            image_path = os.path.join("static", image_filename)
            with open(image_path, "wb") as f:
                f.write(image_data)

            # Pass image URL with a cache-busting query string
            image_url = f"/static/{image_filename}?v={timestamp}"
            return render_template("indexx.html", image_url=image_url)

        except Exception as e:
            return render_template("indexx.html", error=f"Error: {e}")

    return render_template("indexx.html")

@app.route("/download/<filename>")
def download_image(filename):
    file_path = os.path.join("static", filename)
    return send_file(file_path, as_attachment=True)

if __name__ == "__main__":
    # Bind to 0.0.0.0 and use the PORT environment variable
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)
