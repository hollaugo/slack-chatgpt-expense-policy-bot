#Library Modules Needed: llama_index, pathlib, pypdf2
from llama_index import GPTSimpleVectorIndex
from pathlib import Path
from llama_index import download_loader

PDFReader = download_loader("PDFReader")
loader = PDFReader()
documents = loader.load_data(file=Path("expense-policy.pdf"))
index = GPTSimpleVectorIndex.from_documents(documents)
index.save_to_disk("expense-policy-index")




