import os

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI


def get_required_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise ValueError(f"Environment variable {name} is not set.")
    return value


def build_chain():
    os.environ["OPENAI_API_KEY"] = get_required_env("OPENAI_API_KEY")
    os.environ["LANGSMITH_API_KEY"] = get_required_env("LANGSMITH_API_KEY")
    os.environ.setdefault("LANGSMITH_TRACING", "true")
    os.environ.setdefault("LANGSMITH_PROJECT", "my-first-app")

    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

    prompt = ChatPromptTemplate.from_template(
        "Explain {topic} in simple words in 2 lines."
    )

    parser = StrOutputParser()
    return prompt | llm | parser


def main():
    chain = build_chain()
    response = chain.invoke({"topic": "LangSmith"})
    print("\nModel Response:\n")
    print(response)


if __name__ == "__main__":
    main()
