# Interactive-AI-Image-Generator


## Overview
The **AI Image Generator** is a web application that allows users to generate images based on text prompts using a model hosted on Hugging Face's API. Users can enter their prompts, view the generated images, and download them directly from the application.

## Features
- **Interactive UI:** A clean, responsive user interface designed with HTML and CSS.
- **Text-to-Image Generation:** Generates images based on user-provided prompts.
- **Image Download:** Option to download the generated image.
- **Dynamic Background Animation:** Visually appealing gradient animations for enhanced user experience.

## Tech Stack
- **Backend:** Flask (Python)
- **Frontend:** HTML, CSS, JavaScript
- **API Integration:** Hugging Face Inference API

## Prerequisites
Before you begin, ensure you have met the following requirements:
- Python 3.7 or later installed on your system.
- Hugging Face API key.
- Flask and other dependencies installed (listed in `requirements.txt`).

## Installation

### Clone the repository:
```bash
git clone https://github.com/your-username/ai-image-generator.git
```

### Navigate to the project directory:
```bash
cd ai-image-generator
```
### Create and activate a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate
```
You can copy and paste this into your `README.md` file.
Let me know if you need further edits!

### Install Dependencies:
```bash
pip install -r requirements.txt
```

###  Configuration
- Replace the API_KEY variable in app.py with your Hugging Face API key.
- API_KEY = "your_huggingface_api_key"

### Usage

1. Start the Flask development server:
  ```bash
  python app.py
```
2. Open your browser and navigate to:
 ```bash
  http://127.0.0.1:5000
```

-  1.Enter a prompt in the text field and click "Generate Image".
-  2.View the generated image and download it if desired.


├── static
│   ├── styles.css      
│   └── [generated_images]
├── templates
│   └── index.html       
├── app.py               
├── requirements.txt      
└── README.md            

## Contributing

Contributions are welcome! To contribute:

1. **Fork this repository**.

2. **Create a branch**:
   ```bash
   git checkout -b feature-name
``

3. **Make your changes and commit them:**:
   ```bash
   git commit -m 'Add feature-name'
``
4.** Push to the original branch::**:
   ```bash
  git push origin feature-name
```
5.**Create a pull request.**


## License

This project is licensed under the **MIT License**. See the `LICENSE` file for details.

## Acknowledgments

- **Hugging Face** for providing the inference API.
- **Flask documentation** for guidance on building web applications.
- **Unsplash** for inspiration on image handling.

## Contact

For any questions or feedback, please contact:

- **Email:** [harshapappu665@gmail.com](mailto:your-email@example.com)
- **GitHub:** [sriharsha665](https://github.com/your-username)




