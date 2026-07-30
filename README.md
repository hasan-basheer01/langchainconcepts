# LangChain Assignment

This project is a simple LangChain application that uses OpenAI and LangSmith to generate a short explanation of a topic.

## Features

- Uses LangChain prompt templates
- Connects to OpenAI via the OpenAI API
- Sends tracing data to LangSmith
- Runs a simple chain that returns a text response

## Requirements

Make sure you have Python installed and install the required packages:

```bash
pip install langchain langchain-core langchain-community langchain-huggingface sentence-transformers faiss-cpu numpy langchain-openai langsmith
```

## Environment Variables

Create a `.env` file in the project root and add your keys:

```env
OPENAI_API_KEY=your_openai_api_key
LANGSMITH_API_KEY=your_langsmith_api_key
LANGSMITH_TRACING=true
LANGSMITH_PROJECT=my-first-app
```

> Keep your `.env` file private and do not upload it to GitHub.

## Run the Project

```bash
python main.py
```

## Project Structure

```text
Langchain-Assignment/
├── main.py
├── README.md
└── .env
```

## Notes

- The project is intended for learning and demonstration purposes.
- Make sure to add `.env` and `__pycache__/` to your `.gitignore` file.

## License

This project is for educational purposes.
