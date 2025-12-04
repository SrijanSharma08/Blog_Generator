# Blog Generator

This project is an AI-powered blog generation application built using Python, Streamlit, and a custom backend. Users can input a topic, style, or keywords, and the system generates a complete blog article. The project is modular, lightweight, and easy to deploy.

## Features

- Generates blog articles based on user prompts.
- Supports local LLMs (Ollama) and cloud-based Gemini API.
- Streamlit-based user interface.
- Clear separation of backend logic and UI.
- Easy deployment on Streamlit Cloud or local environments.

## Project Structure

.
├── backend.py
├── ui.py
├── requirements.txt
├── .gitignore
└── myenv/ (ignored)

## Installation and Setup

### 1. Clone the repository

git clone https://github.com/SrijanSharma08/Blog_Generator.git
cd Blog_Generator

### 2. Create and activate a virtual environment

python -m venv myenv
myenv/Scripts/activate   (Windows)

### 3. Install dependencies

pip install -r requirements.txt

### 4. Run the application

streamlit run ui.py

## Model Usage

### Option 1: Local model (Ollama)

- Works without an internet connection.
- No API key required.

### Option 2: Gemini API

Requires a Gemini API key.

Set the key on Linux/Mac:

export GEMINI_API_KEY="your_api_key_here"

On Windows CMD:

set GEMINI_API_KEY=your_api_key_here

## How It Works

1. User enters a topic into the Streamlit UI.
2. The UI sends the input to backend.py.
3. Backend interacts with the selected model (Ollama or Gemini).
4. The model generates a blog article.
5. The UI displays the output.

## Deployment

### Deploy on Streamlit Cloud

1. Push project to GitHub.
2. Visit https://share.streamlit.io
3. Connect your repository.
4. Select ui.py as the entry file.
5. Deploy.

## Requirements

Example dependencies:

streamlit
requests

Add any additional libraries used in backend.py.

## Contributing

Contributions are welcome. For major changes, open an issue to discuss your ideas.

## License

This project is open-source and free to modify.
