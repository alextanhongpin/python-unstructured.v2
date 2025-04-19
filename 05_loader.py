import marimo

__generated_with = "0.12.10"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md(
        r"""
        # Loader

        Simple directory loader
        """
    )
    return


@app.cell
def _():
    import marimo as mo
    from pathlib import Path
    import hashlib
    import chromadb
    from unstructured.partition.auto import partition
    import bm25s
    from unstructured.chunking.basic import chunk_elements
    return Path, bm25s, chromadb, chunk_elements, hashlib, mo, partition


@app.cell
def _(chromadb):
    # chroma_client = chromadb.PersistentClient(path="./chroma_db")
    chroma_client = chromadb.Client()
    collection = chroma_client.get_or_create_collection(name="my_collection")
    return chroma_client, collection


@app.cell
def _(mo):
    filetypes = mo.ui.multiselect(options=[".txt", ".pdf"])
    filetypes
    return (filetypes,)


@app.cell
def _(Path, bm25s, chunk_elements, collection, filetypes, hashlib, partition):
    files = Path("data").glob("**/*")
    for file in files:
        if not file.suffix in filetypes.value:
            continue

        with open(str(file), "rb") as f:
            md5 = hashlib.md5(f.read()).hexdigest()
            print(md5)

        elements = partition(file)
        metadatas = [el.to_dict() for el in chunk_elements(elements)]
        metadatas = [
            dict(
                element_id=md.get("element_id", ""),
                text=md.get("text", ""),
                filename=md.get("filename", ""),
                filetype=md.get("filetype", ""),
                last_modified=md.get("last_modified", ""),
                language=md.get("languages", ["english"])[0],
            )
            for md in metadatas
        ]
        ids = [el["element_id"] for el in metadatas]
        documents = [el["text"] for el in metadatas]

        collection.add(documents=documents, ids=ids, metadatas=metadatas)

        # Index bm25
        corpus = documents
        retriever = bm25s.BM25(corpus=corpus)
        retriever.index(bm25s.tokenize(corpus))

        print('indexed')
    return (
        corpus,
        documents,
        elements,
        f,
        file,
        files,
        ids,
        md5,
        metadatas,
        retriever,
    )


@app.cell
def _(mo):
    text = mo.ui.text(label="Query")
    text
    return (text,)


@app.cell
def _(collection, mo, text):
    query = text.value
    mo.stop(not query)

    embedding_results = collection.query(query_texts=[query], n_results=5)
    embedding_results
    return embedding_results, query


@app.cell
def _(bm25s, query, retriever):
    results, scores = retriever.retrieve(bm25s.tokenize(query), k=5)
    results, scores
    return results, scores


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
