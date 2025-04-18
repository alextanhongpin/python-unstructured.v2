import marimo

__generated_with = "0.12.10"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md(
        r"""
        # Cleaning

        https://docs.unstructured.io/open-source/core-functionality/cleaning
        """
    )
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _():
    from unstructured.cleaners.core import replace_unicode_quotes

    replace_unicode_quotes("Philadelphia Eaglesâ\x80\x99 victory")
    return (replace_unicode_quotes,)


@app.cell
def _(replace_unicode_quotes):
    # Returns "“A lovely quote!”"
    replace_unicode_quotes("\x93A lovely quote!\x94")
    return


@app.cell
def _(replace_unicode_quotes):
    # Returns ""‘A lovely quote!’"
    replace_unicode_quotes("\x91A lovely quote!\x92")
    return


@app.cell
def _(replace_unicode_quotes):
    from unstructured.documents.elements import Text

    element = Text("Philadelphia Eaglesâ\x80\x99 victory")
    element.apply(replace_unicode_quotes)
    print(element)
    return Text, element


@app.cell
def _(Text):
    import re

    remove_citations = lambda text: re.sub("\[\d{1,3}\]", "", text)

    element_nocitation = Text(
        "[1] Geolocated combat footage has confirmed Russian gains in the Dvorichne area northwest of Svatove."
    )
    element_nocitation.apply(remove_citations)
    print(element_nocitation)
    return element_nocitation, re, remove_citations


@app.cell
def _():
    from unstructured.cleaners.core import bytes_string_to_string

    text = "Hello ð\x9f\x98\x80"
    # The output should be "Hello 😀"
    bytes_string_to_string(text, encoding="utf-8")
    return bytes_string_to_string, text


@app.cell
def _(bytes_string_to_string, mo):
    mo.stop(True)

    from unstructured.partition.html import partition_html

    text_html = """\n<html charset="utf-8"><p>Hello 😀</p></html>"""
    elements = partition_html(text=text_html)
    elements[0].apply(bytes_string_to_string)
    # The output should be "Hello 😀"
    elements[0].text
    return elements, partition_html, text_html


@app.cell
def _():
    from unstructured.cleaners.core import clean_bullets

    # Returns "An excellent point!"
    clean_bullets("● An excellent point!")

    # Returns "I love Morse Code! ●●●"
    clean_bullets("I love Morse Code! ●●●")
    return (clean_bullets,)


@app.cell
def _():
    from unstructured.cleaners.core import clean_dashes

    # Returns "ITEM 1A: RISK FACTORS"
    clean_dashes("ITEM 1A: RISK-FACTORS\u2013")
    return (clean_dashes,)


@app.cell
def _():
    from unstructured.cleaners.core import clean_non_ascii_chars

    text_non_ascii = "\x88This text contains ®non-ascii characters!●"

    # Returns "This text contains non-ascii characters!"
    clean_non_ascii_chars(text_non_ascii)
    return clean_non_ascii_chars, text_non_ascii


@app.cell
def _():
    from unstructured.cleaners.core import clean_ordered_bullets

    # Returns "This is a very important point"
    clean_ordered_bullets("1.1 This is a very important point")
    return (clean_ordered_bullets,)


@app.cell
def _(clean_ordered_bullets):
    # Returns "This is a very important point ●"
    clean_ordered_bullets("a.b This is a very important point ●")
    return


@app.cell
def _():
    from unstructured.cleaners.core import clean_postfix

    text_postfix = "The end! END"

    # Returns "The end!"
    clean_postfix(text_postfix, r"(END|STOP)", ignore_case=True)
    return clean_postfix, text_postfix


@app.cell
def _():
    from unstructured.cleaners.core import clean_prefix

    text_prefix = "SUMMARY: This is the best summary of all time!"

    # Returns "This is the best summary of all time!"
    clean_prefix(text_prefix, r"(SUMMARY|DESCRIPTION):", ignore_case=True)
    return clean_prefix, text_prefix


@app.cell
def _():
    from unstructured.cleaners.core import clean_trailing_punctuation

    # Returns "ITEM 1A: RISK FACTORS"
    clean_trailing_punctuation("ITEM 1A: RISK FACTORS.")
    return (clean_trailing_punctuation,)


@app.cell
def _():
    from unstructured.cleaners.core import group_broken_paragraphs

    text_paragraph = """The big brown fox
    was walking down the lane.

    At the end of the lane, the
    fox met a bear."""

    group_broken_paragraphs(text_paragraph)
    return group_broken_paragraphs, text_paragraph


@app.cell
def _(group_broken_paragraphs, re):
    para_split_re = re.compile(r"(\s*\n\s*){3}")

    text_paragraph_separator = """The big brown fox

    was walking down the lane.


    At the end of the lane, the

    fox met a bear."""

    group_broken_paragraphs(
        text_paragraph_separator, paragraph_split=para_split_re
    )
    return para_split_re, text_paragraph_separator


@app.cell
def _():
    from unstructured.cleaners.core import remove_punctuation

    # Returns "A lovely quote"
    remove_punctuation("“A lovely quote!”")
    return (remove_punctuation,)


@app.cell
def _():
    from unstructured.cleaners.translate import translate_text

    # Output is "I'm a Berliner!"
    translate_text("Ich bin ein Berliner!")
    return (translate_text,)


@app.cell
def _(translate_text):
    # Output is "I can also translate Russian!"
    translate_text("Я тоже можно переводать русский язык!", "ru", "en")
    return


if __name__ == "__main__":
    app.run()
