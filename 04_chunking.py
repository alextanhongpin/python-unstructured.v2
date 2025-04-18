import marimo

__generated_with = "0.12.10"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md(
        r"""
        # Chunking

        https://docs.unstructured.io/open-source/core-functionality/chunking
        """
    )
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _():
    import json
    from unstructured.partition.html import partition_html


    url = "https://docs.unstructured.io/open-source/core-functionality/chunking"
    elements_basic = partition_html(url=url, chunking_strategy="basic")
    for eb in elements_basic[:10]:
        print(json.dumps(eb.to_dict(), indent=2))
    return eb, elements_basic, json, partition_html, url


@app.cell
def _(json, partition_html, url):
    elements_by_title = partition_html(url=url, chunking_strategy="by_title")
    for et in elements_by_title[:10]:
        print(json.dumps(et.to_dict(), indent=2))
    return elements_by_title, et


@app.cell
def _(mo):
    mo.md(r"""## Calling a chunking function""")
    return


@app.cell
def _(json, partition_html, url):
    from unstructured.chunking.basic import chunk_elements

    elements = partition_html(url=url)
    chunks = chunk_elements(elements)

    for ch in chunks[:10]:
        print(json.dumps(ch.to_dict(), indent=2))
    return ch, chunk_elements, chunks, elements


@app.cell
def _(elements, json):
    from unstructured.chunking.title import chunk_by_title

    chunks_title = chunk_by_title(elements)

    for ch_title in chunks_title[:10]:
        print(json.dumps(ch_title.to_dict(), indent=2))
    return ch_title, chunk_by_title, chunks_title


@app.cell
def _(chunks_title):
    print(chunks_title[0].metadata.orig_elements)
    return


@app.cell
def _(chunks_title):
    print(chunks_title[0].text)
    return


if __name__ == "__main__":
    app.run()
