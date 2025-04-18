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
    return Path, chromadb, hashlib, mo, partition


@app.cell
def _(chromadb):
    chroma_client = chromadb.PersistentClient(path="./chroma_db")
    collection = chroma_client.get_or_create_collection(name="my_collection")
    return chroma_client, collection


@app.cell
def _(mo):
    filetypes = mo.ui.multiselect(options=[".txt", ".pdf"])
    filetypes
    return (filetypes,)


@app.cell
def _(Path, collection, filetypes, hashlib, partition):
    files = Path("data").glob("**/*")
    for file in files:
        if not file.suffix in filetypes.value:
            continue

        with open(str(file), "rb") as f:
            md5 = hashlib.md5(f.read()).hexdigest()
            print(md5)

        elements = partition(file)
        metadatas = [el.to_dict() for el in elements]
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
    return documents, elements, f, file, files, ids, md5, metadatas


@app.cell
def _(mo):
    text = mo.ui.text(label="Query")
    text
    return (text,)


@app.cell
def _(collection, mo, text):
    mo.stop(not text.value)

    results = collection.query(query_texts=[text.value], n_results=10)
    results
    return (results,)


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
