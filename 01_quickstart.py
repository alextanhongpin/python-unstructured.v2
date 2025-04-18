import marimo

__generated_with = "0.12.10"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md(
        r"""
        # Unstructured Quickstart

        This notebook will go through some basic features on unstructured.

        https://docs.unstructured.io/open-source/introduction/quick-start

        ## Goal

        - understand how unstructured works, and see how to incorporate that
        - understand the limitation

        ## Install

        - `brew install libmagic`
        """
    )
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""## Partition""")
    return


@app.cell
def _():
    from unstructured.partition.auto import partition

    elements = partition(filename="data/circuit-breaker.txt")
    elements
    return elements, partition


@app.cell
def _(partition):
    with open("data/circuit-breaker.txt", "rb") as f:
        f_elements = partition(file=f)

    f_elements
    return f, f_elements


@app.cell
def _(elements):
    print("\n\n".join([str(el) for el in elements][:10]))
    return


@app.cell
def _(partition):
    html_elements = partition(
        url="https://docs.unstructured.io/open-source/core-functionality/partitioning"
    )
    html_elements
    return (html_elements,)


@app.cell
def _(html_elements):
    for el in html_elements[:10]:
        print(el.to_dict())
    return (el,)


@app.cell
def _(partition):
    pdf_elements = partition(filename="data/2504.09858v1.pdf")
    pdf_elements
    return (pdf_elements,)


@app.cell
def _(pdf_elements):
    import json

    for it in pdf_elements[:10]:
        print(json.dumps(it.to_dict(), indent=2))
    return it, json


@app.cell
def _():
    {
        "type": "UncategorizedText",
        "element_id": "d087db2190f8497067f164abb53b6fb5",
        "text": "5 2 0 2",
        "metadata": {
            "coordinates": {
                "points": [
                    [16.34, 216.72000000000003],
                    [16.34, 256.72],
                    [36.34, 256.72],
                    [36.34, 216.72000000000003],
                ],
                "system": "PixelSpace",
                "layout_width": 612.0,
                "layout_height": 792.0,
            },
            "file_directory": "data",
            "filename": "2504.09858v1.pdf",
            "languages": ["eng"],
            "last_modified": "2025-04-18T16:20:31",
            "page_number": 1,
            "filetype": "application/pdf",
        },
    }
    {
        "type": "NarrativeText",
        "element_id": "862a98c365a201bf2348259fb71680d6",
        "text": "r p A 4 1",
        "metadata": {
            "coordinates": {
                "points": [
                    [16.34, 261.72000000000014],
                    [16.34, 317.82000000000005],
                    [36.34, 317.82000000000005],
                    [36.34, 261.72000000000014],
                ],
                "system": "PixelSpace",
                "layout_width": 612.0,
                "layout_height": 792.0,
            },
            "file_directory": "data",
            "filename": "2504.09858v1.pdf",
            "languages": ["eng"],
            "last_modified": "2025-04-18T16:20:31",
            "page_number": 1,
            "filetype": "application/pdf",
        },
    }
    {
        "type": "Title",
        "element_id": "ff33c3fe2fca1988b875689952ecf479",
        "text": "] I",
        "metadata": {
            "coordinates": {
                "points": [
                    [16.34, 327.82],
                    [16.34, 341.14],
                    [36.34, 341.14],
                    [36.34, 327.82],
                ],
                "system": "PixelSpace",
                "layout_width": 612.0,
                "layout_height": 792.0,
            },
            "file_directory": "data",
            "filename": "2504.09858v1.pdf",
            "languages": ["eng"],
            "last_modified": "2025-04-18T16:20:31",
            "page_number": 1,
            "filetype": "application/pdf",
        },
    }
    {
        "type": "Title",
        "element_id": "16fbe4eafce791ff389c407792fa6bff",
        "text": "A . s c [",
        "metadata": {
            "coordinates": {
                "points": [
                    [16.34, 341.14000000000004],
                    [16.34, 383.9],
                    [36.34, 383.9],
                    [36.34, 341.14000000000004],
                ],
                "system": "PixelSpace",
                "layout_width": 612.0,
                "layout_height": 792.0,
            },
            "file_directory": "data",
            "filename": "2504.09858v1.pdf",
            "languages": ["eng"],
            "last_modified": "2025-04-18T16:20:31",
            "page_number": 1,
            "filetype": "application/pdf",
        },
    }
    {
        "type": "UncategorizedText",
        "element_id": "beb83409f05e9adb94b9a291da1d8862",
        "text": "1 v 8 5 8 9 0 . 4 0 5 2 : v i X r a",
        "metadata": {
            "coordinates": {
                "points": [
                    [16.34, 393.9],
                    [16.34, 560.0],
                    [36.34, 560.0],
                    [36.34, 393.9],
                ],
                "system": "PixelSpace",
                "layout_width": 612.0,
                "layout_height": 792.0,
            },
            "file_directory": "data",
            "filename": "2504.09858v1.pdf",
            "languages": ["eng"],
            "last_modified": "2025-04-18T16:20:31",
            "page_number": 1,
            "parent_id": "16fbe4eafce791ff389c407792fa6bff",
            "filetype": "application/pdf",
        },
    }
    {
        "type": "Header",
        "element_id": "1d38058801008baa468d8db178718866",
        "text": "Preprint. Under review.",
        "metadata": {
            "coordinates": {
                "points": [
                    [108.0, 28.215853200000083],
                    [108.0, 38.178453200000035],
                    [212.53756179999996, 38.178453200000035],
                    [212.53756179999996, 28.215853200000083],
                ],
                "system": "PixelSpace",
                "layout_width": 612.0,
                "layout_height": 792.0,
            },
            "file_directory": "data",
            "filename": "2504.09858v1.pdf",
            "languages": ["eng"],
            "last_modified": "2025-04-18T16:20:31",
            "page_number": 1,
            "filetype": "application/pdf",
        },
    }
    {
        "type": "Title",
        "element_id": "d530bc848b502737ebf5340b3c4ce3a5",
        "text": "Reasoning Models Can Be Effective Without Thinking",
        "metadata": {
            "coordinates": {
                "points": [
                    [108.0, 81.6388892],
                    [108.0, 95.98508919999995],
                    [465.03387939999993, 95.98508919999995],
                    [465.03387939999993, 81.6388892],
                ],
                "system": "PixelSpace",
                "layout_width": 612.0,
                "layout_height": 792.0,
            },
            "file_directory": "data",
            "filename": "2504.09858v1.pdf",
            "languages": ["eng"],
            "last_modified": "2025-04-18T16:20:31",
            "page_number": 1,
            "parent_id": "1d38058801008baa468d8db178718866",
            "filetype": "application/pdf",
        },
    }
    {
        "type": "Title",
        "element_id": "2bd7b726fc091b9b1d78205855b613fd",
        "text": "Wenjie Ma1 Sewon Min1,2 Matei Zaharia1 1University of California, Berkeley {windsey,jingxuan.he,csnell22,tgriggs,sewonm,matei}@berkeley.edu",
        "metadata": {
            "coordinates": {
                "points": [
                    [113.97799999999995, 117.81659120000006],
                    [113.97799999999995, 164.13974440000004],
                    [432.78189999999995, 164.13974440000004],
                    [432.78189999999995, 117.81659120000006],
                ],
                "system": "PixelSpace",
                "layout_width": 612.0,
                "layout_height": 792.0,
            },
            "file_directory": "data",
            "filename": "2504.09858v1.pdf",
            "languages": ["eng"],
            "last_modified": "2025-04-18T16:20:31",
            "page_number": 1,
            "parent_id": "1d38058801008baa468d8db178718866",
            "filetype": "application/pdf",
        },
    }
    {
        "type": "Title",
        "element_id": "7a1ef03eab7a70ca4a0692e22cc4f22e",
        "text": "Jingxuan He1 Charlie Snell1 Tyler Griggs1",
        "metadata": {
            "coordinates": {
                "points": [
                    [180.06, 117.81659120000006],
                    [180.06, 129.5200516],
                    [391.02779999999996, 129.5200516],
                    [391.02779999999996, 117.81659120000006],
                ],
                "system": "PixelSpace",
                "layout_width": 612.0,
                "layout_height": 792.0,
            },
            "file_directory": "data",
            "filename": "2504.09858v1.pdf",
            "languages": ["eng"],
            "last_modified": "2025-04-18T16:20:31",
            "page_number": 1,
            "parent_id": "1d38058801008baa468d8db178718866",
            "filetype": "application/pdf",
        },
    }
    {
        "type": "Title",
        "element_id": "2c10adde28afb96e2f2caf8b7bf9a087",
        "text": "2Allen Institute for AI",
        "metadata": {
            "coordinates": {
                "points": [
                    [278.65799999999996, 142.1945912000001],
                    [278.65799999999996, 154.05745320000005],
                    [375.1359003999999, 154.05745320000005],
                    [375.1359003999999, 142.1945912000001],
                ],
                "system": "PixelSpace",
                "layout_width": 612.0,
                "layout_height": 792.0,
            },
            "file_directory": "data",
            "filename": "2504.09858v1.pdf",
            "languages": ["eng"],
            "last_modified": "2025-04-18T16:20:31",
            "page_number": 1,
            "parent_id": "1d38058801008baa468d8db178718866",
            "filetype": "application/pdf",
        },
    }
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
