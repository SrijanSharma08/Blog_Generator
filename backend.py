# backend.py
from functools import lru_cache
from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM


@lru_cache(maxsize=1)
def load_llm() -> OllamaLLM:
    """
    Load the Ollama LLM once and reuse it.
    """
    return OllamaLLM(
        model="llama3.1:8b",   # make sure you've done: ollama pull llama3.1:8b
        num_predict=1024,
        temperature=0.3,
    )


# Prompt template shared by the app
prompt = PromptTemplate(
    input_variables=["style", "text", "n_words", "tone"],
    template="""
Write a blog in a {style} style for the topic "{text}"
within approximately {n_words} words.
The overall tone of the writing should be {tone}.
Use clear headings, short paragraphs, and bullet points where useful.
Begin directly with a title for the blog.
""",
)


def generate_blog(topic: str, n_words: int, audience: str, tone: str) -> str:
    """
    Call the LLM and return a formatted blog.
    """
    llm = load_llm()
    final_prompt = prompt.format(
        style=audience,
        text=topic,
        n_words=n_words,
        tone=tone,
    )
    blog_raw = llm.invoke(final_prompt)
    return _format_blog(blog_raw)


def _format_blog(blog_text: str) -> str:
    """
    Light formatting: improves bullet spacing etc.
    """
    blog_text = blog_text.replace("• ", "\n\n• ")
    return blog_text
