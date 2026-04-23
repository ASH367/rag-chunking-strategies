from langchain_community.document_loaders import PyPDFLoader
from langchain_experimental.text_splitter import SemanticChunker
from langchain_huggingface import HuggingFaceEmbeddings

file_path = "./sample/Ashish_Ubale_AI.pdf"
loader = PyPDFLoader(file_path)
docs = loader.load()

full_text = " ".join([doc.page_content for doc in docs])
print(f"Total characters: {len(full_text)}")

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# breakpoint_threshold_amount=95 means split when similarity drops in bottom 5%
# Lower number = more chunks, higher = fewer chunks
chunker = SemanticChunker(embeddings=embeddings, breakpoint_threshold_type="percentile", breakpoint_threshold_amount=95)
chunks = chunker.split_documents(docs)

print(f"Total chunks: {len(chunks)}")

for i, chunk in enumerate(chunks):
    print(f"\n--- Chunk {i+1} ({len(chunk.page_content)} chars) ---")
    print(chunk.page_content)

# Semantic chunking uses embedding models to measure similarity between sentences
# Splits when similarity drops below a percentile threshold — meaning shifts, not character counts
# Fewer, more meaningful chunks but slower — runs embeddings at index time