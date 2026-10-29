# scratch/scratch_chunking.py
"""
Component Sandbox 1: Text Chunking & Sliding Window Overlap
Learn the mechanics of splitting long text into manageable chunks with overlap
to prevent losing semantic context at boundary splits.
"""

from typing import List


def chunk_text(text: str, chunk_size: int = 150, chunk_overlap: int = 30) -> List[str]:
    """
    Split input text into overlapping chunks using a sliding window approach.
    
    Args:
        text (str): The raw input document text.
        chunk_size (int): The maximum character length of each chunk.
        chunk_overlap (int): The number of characters to overlap between consecutive chunks.
        
    Returns:
        List[str]: A list of string chunks.
    """
    # Defensive guard: Overlap cannot be greater than or equal to chunk size
    if chunk_overlap >= chunk_size:
        raise ValueError("chunk_overlap must be strictly less than chunk_size")

    chunks: List[str] = []
    start = 0
    text_length = len(text)

    # TODO: Implement the sliding window loop
    # 1. While start < text_length:
    # 2.   Calculate end = start + chunk_size
    # 3.   Extract the substring: chunk = text[start:end]
    # 4.   Strip any leading/trailing whitespace: clean_chunk = chunk.strip()
    # 5.   If clean_chunk is not empty, append it to chunks
    # 6.   Advance the window: start = start + (chunk_size - chunk_overlap)
    #
    # Write your sliding window implementation below:
    while start < text_length:
        end= (start + chunk_size)
        chunk = (text[start:end]).strip()
        if chunk:
            chunks.append(chunk)
        start = end - chunk_overlap
    return chunks


def chunk_text_word_aware(text: str, chunk_size: int = 150, chunk_overlap: int = 30) -> List[str]:
    """
    Split text into overlapping chunks, ensuring chunks don't break words in half.
    """
    if chunk_overlap >= chunk_size:
        raise ValueError("chunk_overlap must be strictly less than chunk_size")

    chunks: List[str] = []
    start = 0
    text_length = len(text)

    while start < text_length:
        end = start + chunk_size
        
        # TODO: OPTIMIZATION 1 - Prevent cutting words at the end of the chunk
        # 1. If 'end' is less than text_length, we might be cutting a word in half.
        # 2. Use `text.rfind(' ', start, end)` to find the index of the last space in our current window.
        # 3. If a space is found (result is not -1), update 'end' to be that space's index.
        # 
        # Write your 'end' adjustment logic below:
        if( end < text_length ):
            space_idx = text.rfind(' ',start,end)
            if(space_idx!=-1):
                 end = space_idx            
            

        chunk = text[start:end].strip()
        if chunk:
            chunks.append(chunk)
            
        # TODO: OPTIMIZATION 2 - Prevent starting mid-word in the overlap
        # 1. Calculate the initial next start: next_start = end - chunk_overlap
        # 2. To avoid starting mid-word, find the last space BEFORE next_start:
        #    space_idx = text.rfind(' ', 0, next_start)
        # 3. Update 'start' to space_idx (if found and > start) OR next_start (if not found or stuck).
        #
        # Write your 'start' adjustment logic below:
        
        # (Remove this break once implemented to avoid infinite loops during testing)
        next_start = end - chunk_overlap
        space_idx = text.rfind(' ',0,next_start)
        if(space_idx!=-1 and space_idx>start):
            start = space_idx
        else:
            start = next_start

    return chunks


if __name__ == "__main__":
    sample_document = (
        "Retrieval-Augmented Generation (RAG) is an enterprise AI pattern that optimizes the output "
        "of a Large Language Model. RAG references an authoritative knowledge base outside of its "
        "training data sources before generating a response. Large Language Models (LLMs) are trained "
        "on vast volumes of data and use billions of parameters to generate original output for tasks "
        "like answering questions, translating languages, and completing sentences. RAG extends the "
        "already powerful capabilities of LLMs to specific domains or an organization's internal "
        "knowledge base, all without the need to retrain the model. It is a cost-effective approach to "
        "improving LLM output so it remains relevant, accurate, and useful in various contexts."
    )

    print("=" * 60)
    print("SANDBOX 1: Testing Naive Sliding Window")
    print("=" * 60)
    result_chunks = chunk_text(sample_document, chunk_size=120, chunk_overlap=25)
    for idx, chunk in enumerate(result_chunks[:2], 1):
        print(f"--- Chunk #{idx} (Length: {len(chunk)} chars) ---")
        print(f'"{chunk}"\n')
        
    print("=" * 60)
    print("OPTIMIZATION: Testing Word-Aware Sliding Window")
    print("=" * 60)
    word_aware_chunks = chunk_text_word_aware(sample_document, chunk_size=120, chunk_overlap=25)
    
    if not word_aware_chunks or len(word_aware_chunks) == 1:
         print("[!] chunk_text_word_aware returned incomplete chunks. Complete the # TODO blocks to test.")
    else:
        for idx, chunk in enumerate(word_aware_chunks, 1):
            print(f"--- Optimized Chunk #{idx} (Length: {len(chunk)} chars) ---")
            print(f'"{chunk}"\n')
