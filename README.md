# Sentiment-and-Subjectivity-Analyzer
# Sentiment and Subjectivity Analyzer

This project is a Python-based tool that analyzes the sentimentality and subjectivity of a given text. It can process text either from a URL or directly pasted by the user. The analysis uses the `TextBlob` and `newspaper` libraries to extract and process the text, and `nltk` for text tokenization.

## Features

- Fetch text content from a URL
- Analyze user-pasted text
- Determine sentiment polarity and subjectivity
- Interpret and display the sentiment polarity and subjectivity in user-friendly terms

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/sentiment-analyzer.git
    cd sentiment-analyzer
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the script:

    ```bash
    python sentiment_analyzer.py
    ```

2. Follow the prompts to either enter a URL or paste your own text.

3. The script will display the sentiment polarity and subjectivity of the text.

## Example

When prompted, enter 'URL' or 'Text'. For a URL, provide the link to the article you want to analyze. For direct text input, paste the text into the console. The output will look something like this:


Do you want to enter a URL or paste your own text? (Enter 'URL' or 'Text'): URL
Paste the URL you want to know the sentimentality and subjectivity of: https://example.com/article

Text for Analysis:
<First 500 characters of the article>

Sentiment Analysis:
Polarity: 0.1 (Positive)
Subjectivity: 0.4 (Objective)


## Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature/YourFeature`).
6. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [TextBlob](https://textblob.readthedocs.io/en/dev/)
- [newspaper3k](https://newspaper.readthedocs.io/en/latest/)
- [nltk](https://www.nltk.org/)

