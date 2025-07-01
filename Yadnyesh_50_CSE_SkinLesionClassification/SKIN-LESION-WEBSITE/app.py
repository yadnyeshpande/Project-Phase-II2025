
from flask import Flask, render_template, request, send_file, session, redirect, url_for
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

import numpy as np
import os
import io
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['UPLOAD_FOLDER'] = 'static/uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Load trained model and class labels
model = load_model('model/resnet50_skin_best.h5')
class_labels = ['akiec', 'bcc', 'bkl', 'df', 'mel', 'nv', 'vasc']
CONFIDENCE_THRESHOLD = 70  # 👈 You can adjust this value if needed

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# About route
@app.route('/about')
def about():
    return render_template('about.html')

# Prediction route
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        files = request.files.getlist('images')
        patient_name = request.form.get('patient_name')
        patient_age = request.form.get('patient_age')
        blood_group = request.form.get('blood_group')
        results = []

        for file in files:
            if file:
                filename = secure_filename(file.filename)
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(file_path)

                # Preprocess image
                img = image.load_img(file_path, target_size=(224, 224))
                img_array = image.img_to_array(img)
                img_array = np.expand_dims(img_array, axis=0)
                img_array = img_array / 255.0

                # Predict
                prediction = model.predict(img_array)
                confidence = float(np.max(prediction)) * 100
                predicted_index = np.argmax(prediction)

                # ✅ Check confidence threshold
                if confidence < CONFIDENCE_THRESHOLD:
                    predicted_class = "Unknown / Not a skin lesion"
                else:
                    predicted_class = class_labels[predicted_index]

                results.append({
                    'label': predicted_class,
                    'confidence': round(confidence, 2),
                    'image': filename
                })

        # Store results and patient info in session
        session['report_data'] = {
            'name': patient_name,
            'age': patient_age,
            'blood_group': blood_group,
            'predictions': results
        }

        return render_template('predict.html', results=results)

    return render_template('predict.html')

# Download PDF report route
@app.route('/download_report')
def download_report():
    data = session.get('report_data')
    if not data:
        return redirect(url_for('predict'))

    buffer = io.BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter

    y = height - 50

    # Title
    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(50, y, "Skin Lesion Detection Report")
    y -= 40

    # Patient Info
    pdf.setFont("Helvetica", 12)
    pdf.drawString(50, y, f"Patient Name: {data['name']}")
    y -= 20
    pdf.drawString(50, y, f"Age: {data['age']}")
    y -= 20
    pdf.drawString(50, y, f"Blood Group: {data['blood_group']}")
    y -= 30

    # Table Headers
    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(50, y, "Predicted Disease")
    pdf.drawString(300, y, "Confidence (%)")
    y -= 20

    # Prediction Results
    pdf.setFont("Helvetica", 12)
    for item in data['predictions']:
        if y < 80:
            pdf.showPage()
            y = height - 50

        pdf.drawString(50, y, item['label'])
        pdf.drawString(300, y, f"{item['confidence']}%")
        y -= 20

    pdf.save()
    buffer.seek(0)

    return send_file(buffer, as_attachment=True, download_name="prediction_report.pdf", mimetype='application/pdf')

# Run app
if __name__ == '__main__':
    app.run(debug=True)
