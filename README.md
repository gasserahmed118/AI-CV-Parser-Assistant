# 📄 AI CV Parser

A modern Streamlit web application that uses AI to parse and extract structured data from CV/resume PDFs automatically.

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-1.0+-red.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## ✨ Features

- 📤 **Easy Upload**: Simple drag-and-drop PDF upload interface
- 🤖 **AI-Powered**: Leverages AI models to intelligently extract CV information
- 📊 **Structured Output**: Extracts and displays:
  - Full Name
  - Email Address
  - Education Background
  - Skills (displayed as interactive chips)
  - Work Experience
- 🎨 **Modern UI**: Clean, dark-themed interface with gradient effects
- ⚡ **Real-time Processing**: Fast parsing with visual feedback

## 🛠️ Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Setup

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd cv-parser
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Configure API settings**

Edit the API configuration in `parser.py`:
```python
API_URL = "your-api-endpoint-here"
API_KEY = "your-api-key-here"
```

## 📦 Dependencies

Create a `requirements.txt` file with the following:

```
streamlit>=1.28.0
requests>=2.31.0
```

Install with:
```bash
pip install -r requirements.txt
```

## 🚀 Usage

1. **Start the Streamlit app**
```bash
streamlit run parser.py
```

2. **Access the application**

The app will automatically open in your default browser at `http://localhost:8501`

3. **Parse a CV**
   - Click on the file upload area
   - Select a PDF CV/resume
   - Click "Parse CV" button
   - View the extracted information

## 🔧 Configuration

### API Setup

The application requires a backend API endpoint for CV parsing. Configure in `parser.py`:

```python
API_URL = "https://your-api-endpoint.com/parse_cv"
API_KEY = "your_secret_key"
```

### API Response Format

The API should return JSON in the following format:

```json
{
  "parsed_cv": {
    "full_name": "John Doe",
    "email": "john.doe@example.com",
    "education": "Bachelor of Science in Computer Science, XYZ University",
    "skills": ["Python", "JavaScript", "Machine Learning", "Docker"],
    "experience": "Software Engineer at ABC Corp, Data Analyst at XYZ Inc"
  }
}
```

## 📁 Project Structure

```
cv-parser/
│
├── parser.py              # Main Streamlit application
├── cv-parser__1_.ipynb   # Jupyter notebook (development/testing)
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## 🎨 UI Features

- **Dark Theme**: Modern dark color scheme (#0d1117 background)
- **Skill Chips**: Interactive gradient skill badges with hover effects
- **Responsive Design**: Centered layout optimized for all screen sizes
- **Loading States**: Visual feedback during CV processing

## ⚙️ Customization

### Changing the Theme

Modify the CSS in the `st.markdown()` section of `parser.py`:

```python
st.markdown("""
<style>
body, .main {
    background-color: #0d1117;  /* Change background color */
    color: white;
}
/* ... more styles ... */
</style>
""", unsafe_allow_html=True)
```

### Timeout Settings

Adjust the API timeout in `parser.py`:

```python
response = requests.post(API_URL, files=files, headers=headers, timeout=400)
# Change timeout value (in seconds) as needed
```

## 🐛 Troubleshooting

### Common Issues

1. **Timeout Error**
   - Increase the timeout value in the request
   - Check if the API endpoint is responding

2. **JSON Parsing Error**
   - Verify the API response format
   - Check the debug info in the error expander

3. **Network Error**
   - Ensure the API URL is correct and accessible
   - Check your internet connection
   - Verify the API key is valid

## 📝 Error Handling

The application handles:
- Request timeouts
- Network errors
- Invalid JSON responses
- Missing API keys
- Malformed API responses

## 🔐 Security Notes

- Never commit your API keys to version control
- Use environment variables for sensitive configuration
- Consider implementing rate limiting
- Validate uploaded files before processing

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by AI for intelligent CV parsing

## 📧 Contact
   Author : Gasser Ahmed
For questions or support, please open an issue in the repository.

---

**Note**: Remember to set up your backend API endpoint before running the application.
