# AI Text Humanizer

This project is an AI-based text humanizer built using Django, Python, and NLTK. It takes AI-generated text as input and humanizes it by correcting grammar, improving structure, and making it sound more natural. This project can be used to refine formal, robotic, or machine-generated content to appear more human-like.

## Features
- **Humanizes AI-generated text** by improving its flow and grammatical structure.
- **Provides an easy-to-use frontend interface** where users can input text and receive humanized output.
- **Utilizes NLTK** for sentence tokenization and **TextBlob** for grammar correction.

## Technologies Used
- **Backend**: Django, Python
- **Frontend**: HTML, CSS, JavaScript (Fetch API)
- **Text Processing**: NLTK, TextBlob
- **Database**: SQLite (for Django sessions)

## Installation Guide

### Step 1: Clone the repository
```bash
git clone https://github.com/yourusername/ai-text-humanizer.git
cd ai-text-humanizer
```
### Step 2: Set up a virtual environment
To avoid dependency conflicts, it is recommended to use a virtual environment.

For **Windows**:
```bash
python -m venv venv
venv\Scripts\activate
```
For **macOS/Linux**:
```bash
python3 -m venv venv
source venv/bin/activate
```
### Step 3: Install dependencies
```bash
pip install -r requirements.txt
```
### Step 4: Migrate the database
```bash
python manage.py migrate
```
### Step 5: Download NLTK punkt package
Ensure that the NLTK punkt package is installed by running the following:
```bash
import nltk
nltk.download('punkt')
```
### Step 6: Run the development server
```bash
python manage.py runserver
```
Your server should now be running at http://127.0.0.1:8000/.

### Step 7: Access the application
Visit the URL in your browser and input some AI-generated text to humanize it.
## API Endpoints

### POST `/humanize/`

#### Request Body:
```json
{
    "text": "AI-generated text here."
}
```
```json
{
    "humanized_text": "Refined human-like text."
}
```
 ## Contribution
If you would like to contribute to this project, feel free to fork the repository and submit a pull request. Any improvements or bug fixes are greatly appreciated!

### Steps to contribute:
1. **Fork** this repository.
2. **Clone** your fork to your local machine.
3. **Create a new branch**:
```bash
git checkout -b new-feature
```
4. Make your changes..
5. **Commit your changes**:
```bash
git commit -am 'Add new feature'
```
6. **Push to branch**:
```bash
git push origin new-feature
```
7. Create a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
