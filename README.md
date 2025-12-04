Blog Generator – AI-Powered Content Creation Tool

This project is an AI-powered blog generation application built with Python, Streamlit, and a custom backend.
Users can enter a topic, style, or keywords, and the application will generate a complete blog article.

The system is lightweight, modular, and easy to deploy.

Features

AI-generated blog articles from a topic or prompt

Supports local LLMs (Ollama) or cloud-based Gemini API

Clean and simple Streamlit interface

Modular structure with separate backend and UI

Easy to install and deploy on Streamlit Cloud or locally

Project Structure
.
├── backend.py          # Blog generation logic and model interface
├── ui.py               # Streamlit-based user interface
├── requirements.txt    # Dependencies
├── .gitignore
└── myenv/ (ignored)

Installation and Setup
1. Clone the repository
git clone https://github.com/SrijanSharma08/Blog_Generator.git
cd Blog_Generator

2. Create and activate a virtual environment
python -m venv myenv
myenv/Scripts/activate  # Windows

3. Install dependencies
pip install -r requirements.txt

4. Run the Streamlit application
streamlit run ui.py

Model Options
Option 1: Local model (Ollama)

No API key needed

Works offline

Suitable for local development

Option 2: Gemini API

Requires a Google Gemini API key

Higher-quality outputs

Set the API key:

export GEMINI_API_KEY="your_api_key_here"


(Windows CMD)

set GEMINI_API_KEY=your_api_key_here

How It Works

User inputs a topic or prompt in the Streamlit interface.

The UI sends the request to backend.py.

The backend communicates with the selected LLM.

The model returns a generated blog article.

The UI displays the blog in a readable format.

Deployment
Deploy on Streamlit Cloud

Push the project to GitHub

Visit https://share.streamlit.io

Connect your GitHub repository

Select ui.py as the entrypoint

Deploy the app

I can help configure requirements, environment variables, and deployment settings if needed.

Requirements

Typical dependencies (based on your setup):

streamlit
requests


Include any additional libraries you use in your backend.

Contributing

Contributions are welcome.
For major changes, please open an issue to discuss your proposed improvements.

License

This project is open-source and free to modify and use.
