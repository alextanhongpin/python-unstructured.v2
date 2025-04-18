import marimo

__generated_with = "0.12.10"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md(
        r"""
        # Extraction

        https://docs.unstructured.io/open-source/core-functionality/extracting
        """
    )
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _():
    from unstructured.cleaners.extract import extract_datetimetz

    text = """from ABC.DEF.local ([ba23::58b5:2236:45g2:88h2]) by
      \n ABC.DEF.local2 ([ba23::58b5:2236:45g2:88h2%25]) with mapi id\
      n 32.88.5467.123; Fri, 26 Mar 2021 11:04:09 +1200"""

    # Returns datetime.datetime(2021, 3, 26, 11, 4, 9, tzinfo=datetime.timezone(datetime.timedelta(seconds=43200)))
    extract_datetimetz(text)
    return extract_datetimetz, text


@app.cell
def _():
    from unstructured.cleaners.extract import extract_email_address

    text_email = """Me me@email.com and You <You@email.com>
        ([ba23::58b5:2236:45g2:88h2]) (10.0.2.01)"""

    # Returns "['me@email.com', 'you@email.com']"
    extract_email_address(text_email)
    return extract_email_address, text_email


@app.cell
def _():
    from unstructured.cleaners.extract import extract_ip_address

    text_ip = """Me me@email.com and You <You@email.com>
      ([ba23::58b5:2236:45g2:88h2]) (10.0.2.01)"""

    # Returns "['ba23::58b5:2236:45g2:88h2', '10.0.2.01']"
    extract_ip_address(text_ip)
    return extract_ip_address, text_ip


@app.cell
def _():
    from unstructured.cleaners.extract import extract_ip_address_name

    text_ip_name = """from ABC.DEF.local ([ba23::58b5:2236:45g2:88h2]) by
      \n ABC.DEF.local2 ([ba23::58b5:2236:45g2:88h2%25]) with mapi id\
      n 32.88.5467.123; Fri, 26 Mar 2021 11:04:09 +1200"""

    # Returns "['ABC.DEF.local', 'ABC.DEF.local2']"
    extract_ip_address_name(text_ip_name)
    return extract_ip_address_name, text_ip_name


@app.cell
def _():
    from unstructured.cleaners.extract import extract_mapi_id

    text_mapi = """from ABC.DEF.local ([ba23::58b5:2236:45g2:88h2]) by
      \n ABC.DEF.local2 ([ba23::58b5:2236:45g2:88h2%25]) with mapi id\
      n 32.88.5467.123; Fri, 26 Mar 2021 11:04:09 +1200"""

    # Returns "['32.88.5467.123']"
    extract_mapi_id(text_mapi)
    return extract_mapi_id, text_mapi


@app.cell
def _():
    from unstructured.cleaners.extract import extract_ordered_bullets

    # Returns ("1", "1", None)
    extract_ordered_bullets("1.1 This is a very important point")
    return (extract_ordered_bullets,)


@app.cell
def _(extract_ordered_bullets):
    # Returns ("a", "1", None)
    extract_ordered_bullets("a.1 This is a very important point")
    return


@app.cell
def _():
    from unstructured.cleaners.extract import extract_text_after

    text_after = "SPEAKER 1: Look at me, I'm flying!"

    # Returns "Look at me, I'm flying!"
    extract_text_after(text_after, r"SPEAKER \d{1}:")
    return extract_text_after, text_after


@app.cell
def _():
    from unstructured.cleaners.extract import extract_text_before

    text_before = "Here I am! STOP Look at me! STOP I'm flying! STOP"

    # Returns "Here I am!"
    extract_text_before(text_before, r"STOP")
    return extract_text_before, text_before


@app.cell
def _():
    from unstructured.cleaners.extract import extract_us_phone_number

    # Returns "215-867-5309"
    extract_us_phone_number("Phone number: 215-867-5309")
    return (extract_us_phone_number,)


if __name__ == "__main__":
    app.run()
