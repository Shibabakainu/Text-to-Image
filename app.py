from flask import Flask, request, jsonify, render_template
import os
from StableDiffusion.sd_service import SDService
from translationAPI.translate_service import TranslateService  # Importing translation service

app = Flask(__name__)
sd_service = SDService()
translate_service = TranslateService()

# Define the path to the static folder
STATIC_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')

# Ensure that the static folder exists
if not os.path.exists(STATIC_FOLDER):
    os.makedirs(STATIC_FOLDER)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    prompt = request.form.get('prompt')
    
    if not prompt:
        return jsonify({"error": "No prompt provided"}), 400
    
    # Translate the prompt if it's in Japanese (or any other language)
    translated_prompt = translate_service.translate(prompt)['result']
    
    print("Original Prompt:", prompt)
    print("Translated Prompt:", translated_prompt)

    # Generate the image based on the translated prompt
    img = sd_service.create_img(translated_prompt)
    
    # Save the image to the static folder
    image_filename = 'generated_image.png'
    img_path = os.path.join(STATIC_FOLDER, image_filename)
    img.save(img_path)

    # Return the path to the image so it can be displayed on the frontend
    return jsonify({"image_path": f"/static/{image_filename}"})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
