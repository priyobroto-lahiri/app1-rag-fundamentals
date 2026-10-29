# scratch/scratch_embeddings.py
"""
Component Sandbox 2: Vector Embeddings & Ingestion
Learn how to convert text chunks into high-dimensional vectors (embeddings)
and store/query them using a local vector database (ChromaDB).
"""

import chromadb
from sentence_transformers import SentenceTransformer

def main():
    # 1. Sample chunks (simulating output from Sandbox 1)
    documents = [
        "Retrieval-Augmented Generation (RAG) is an enterprise AI pattern that optimizes the output of a Large Language Model.",
        "RAG references an authoritative knowledge base outside of its training data sources before generating a response.",
        "Large Language Models (LLMs) are trained on vast volumes of data and use billions of parameters to generate original output.",
        "RAG extends the already powerful capabilities of LLMs to specific domains without the need to retrain the model."
    ]
    
    # We need unique IDs for each document in the vector database
    doc_ids = [f"chunk_{i}" for i in range(len(documents))]

    print("--- Step 1: Initializing Embedding Model ---")
    # We use a fast, lightweight open-source model from Hugging Face
    # all-MiniLM-L6-v2 produces 384-dimensional vectors.
    print("Loading SentenceTransformer model (this may take a few seconds on first run)...")
    model = SentenceTransformer('all-MiniLM-L6-v2')
    
    # TODO: GENERATE EMBEDDINGS
    # 1. Use the `model.encode()` method on your `documents` list.
    # 2. Assign the result to a variable called `embeddings`.
    # (This converts our human text into arrays of floating-point numbers that capture semantic meaning)
    
    # Write your embedding generation code here:
    embeddings = model.encode(documents).tolist()
    
    if embeddings is not None:
        print(f"Successfully generated {len(embeddings)} embeddings.")
        print(f"Dimension of each embedding: {len(embeddings[0])}\n")

    print("--- Step 2: Initializing ChromaDB ---")
    # Create an in-memory Chroma client for testing (analogous to H2 in-memory DB in Java)
    chroma_client = chromadb.PersistentClient(path="./my_vector_storage")
    
    # Create a collection (analogous to a Table in SQL or Collection in MongoDB)
    collection = chroma_client.create_collection(name="rag_sandbox_collection")
    
    # TODO: INGEST DATA INTO VECTOR DATABASE
    # 1. Use `collection.add()` to insert your data.
    # 2. You must provide 3 arguments: 
    #    - embeddings=embeddings.tolist() if it's a numpy array, or just embeddings if it's a list
    #    - documents=documents
    #    - ids=doc_ids
    
    # Write your database ingestion code here:
    collection.add(embeddings = embeddings,
                   documents = documents,
                   ids = doc_ids)
    
    print("--- Step 3: Semantic Search (Querying) ---")
    query_text = "Does RAG require retraining the AI model?"
    print(f"Query: '{query_text}'")
    
    # TODO: QUERY THE VECTOR DATABASE
    # 1. Generate the embedding for the `query_text` using `model.encode(query_text)`.
    # 2. Convert it to a list: query_embedding_list = query_embedding.tolist()
    # 3. Use `collection.query()` passing:
    #    - query_embeddings=[query_embedding_list]
    #    - n_results=2 (to get the top 2 matches)
    # 4. Print the result! (Look specifically at result['documents'])
    
    # Write your query logic below:
    query_embedding_list = model.encode(query_text).tolist()
    result = collection.query(
        query_embeddings=[query_embedding_list],
        n_results=2
    )
    print(result)
    
if __name__ == "__main__":
    main()
