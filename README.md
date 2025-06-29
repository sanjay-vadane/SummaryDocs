# OpenAI Document Summarizer

This project is an application that utilizes OpenAI's API to summarize documents. It provides both a command-line interface and a Streamlit web interface for users to easily summarize their documents.

## Project Structure

```
openai-summarizer
├── src
│   ├── main.py          # Entry point for the command-line application
│   ├── summarizer.py    # Contains the Summarizer class for text summarization
│   ├── utils.py         # Utility functions for loading and saving documents
│   └── streamlit_app.py  # Streamlit application for a user-friendly interface
├── requirements.txt      # Lists the project dependencies
└── README.md             # Project documentation
```

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd openai-summarizer
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your OpenAI API key:**
   Make sure to set your OpenAI API key as an environment variable:
   ```bash
   export OPENAI_API_KEY='your-api-key'  # On Windows use `set OPENAI_API_KEY='your-api-key'`
   ```

## Usage

### Command-Line Interface

To run the command-line application, execute the following command:

```bash
python src/main.py
```

You will be prompted to enter the path to the document you want to summarize and the path to save the summary.

### Streamlit Interface

To run the Streamlit application, execute the following command:

```bash
streamlit run src/streamlit_app.py
```

This will open a web interface in your default browser where you can upload a document, view the summary, and download it.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.