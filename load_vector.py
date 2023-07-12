# Library Modules Needed: llama_index, pathlib, pypdf2
from pathlib import Path

import config
import openai
from llama_index import GPTVectorStoreIndex as GPTSimpleVectorIndex
from llama_index import download_loader

openai.api_key = config.OPENAI_KEY

PDFReader = download_loader("PDFReader")
loader = PDFReader()
documents = loader.load_data(file=Path("slack-chatgpt-qa-bot\ABS_Prof_Full.pdf"))
index = GPTSimpleVectorIndex.from_documents(documents)
index.storage_context.persist(
    persist_dir=r"C:\Users\DanielCantorBaez\Documents\SyncierGPT\slack-chatgpt-qa-bot\abs-prof-index"
)
