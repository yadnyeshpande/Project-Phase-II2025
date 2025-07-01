# 🧠 Skin Lesion Classification Project

This project detects and classifies skin lesions using deep learning. It has two parts:

1. Model training using CNN, ResNet50, and VGG16.
2. A Flask web app that takes an image and predicts the skin lesion type.

---

## 🔧 Technologies Used

- Python
- TensorFlow / Keras
- OpenCV, NumPy, Pandas
- Flask
- HTML, CSS (Tailwind optional)
- Jupyter Notebook

---

## 📁 Folder Overview

### 1. SKIN-LESION (Training Folder)

- Jupyter notebooks for training (`resnet.ipynb`, `Skin_Lision.ipynb`)
- You need to run these notebooks to train and generate model files (`.h5`).

### 2. SKIN-LESION-WEBSITE (Web App)

- `app.py`: Flask app
- `model/`: (Empty) — Add your trained `.h5` models here after training
- `static/`: Images, CSS, and upload folder
- `templates/`: HTML files (UI pages)
- `requirements.txt`: Needed Python libraries

---

## 📅 Dataset Used

This project uses the **HAM10000** dataset: *"Human Against Machine with 10000 training images"*.

- 🔗 Dataset Link: [Kaggle - HAM10000 Skin Lesion Dataset](https://www.kaggle.com/datasets/kmader/skin-cancer-mnist-ham10000)
- 🔢 Total Images: 10,015
- 📆 Types of Skin Lesions:
  - Melanocytic nevi (nv)
  - Melanoma (mel)
  - Benign keratosis-like lesions (bkl)
  - Basal cell carcinoma (bcc)
  - Actinic keratoses (akiec)
  - Vascular lesions (vasc)
  - Dermatofibroma (df)

The dataset includes metadata such as age, sex, localization, and diagnosis type. It is widely used for skin cancer classification tasks.

---

## 💻 How to Run

### Step 1: Clone this repo

```bash
git clone https://github.com/yourusername/Skin-Lesion-Classification.git
cd SKIN-LESION-WEBSITE
```

### Step 2: Create a virtual environment (optional)

```bash
python -m venv myenv5
myenv5\Scripts\activate  # for Windows
```

### Step 3: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Train models (important!)

Go to the `SKIN-LESION` folder and run the Jupyter notebooks to train your models. After training, save your `.h5` files and place them in the `SKIN-LESION-WEBSITE/model/` folder.

### Step 5: Run the web app

```bash
python app.py
```

Then open your browser and go to:\
🔗 [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 📊 Model Performance

| Model    | Accuracy     |
| -------- | ------------ |
| CNN      | \~80%        |
| ResNet50 | \~96% ✅ Best |
| VGG16    | Good         |
| SVM      | Poor         |

---

## 📸 Web App Features

- Upload a skin lesion image
- Get prediction using the best model
- Simple user interface
- Pages: Home, Predict, About

---

## 📂 Full Folder Structure

```
Skin-Lesion-Classification/
🔼── SKIN-LESION/
│   🔼── .ipynb_checkpoints/
│   🔼── resnet.ipynb
│   🔼── Skin_Lision.ipynb

🔼── SKIN-LESION-WEBSITE/
│   🔼── app.py
│   🔼── requirements.txt
│   🔼── README.md
│   🔼── .gitignore
│
│   🔼── model/
│   │   (Place your trained .h5 files here)
│
│   🔼── myenv5/   (Virtual environment - not needed on GitHub)
│
│   🔼── static/
│   │   🔼── style.css
│   │   🔼── style2.css
│   │   🔼── images/
│   │   🔼── uploads/
│
│   🔼── templates/
│       🔼── index.html
│       🔼── predict.html
│       🔼── about.html
│       🔼── about.txt
```

---

## 👷 Authors

**Yadnyesh Pande**\
**Somesh Alone**\
**Pratik Papanwar**

> *Project done under the guidance of Prof. Savita S. Wagare*\
> 📧 [yadnyeshpande342@gmail.com](mailto\:yadnyeshpande342@gmail.com)\
> 📍 Nanded, Maharashtra, India

---

## 📜 License

This project is open-source and free to use.

