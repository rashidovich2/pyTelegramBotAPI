"""
Markdown & HTML formatting functions.

.. versionadded:: 4.5.1
"""

import html

import re

from typing import Optional


def format_text(*args, separator="\n"):
    """
    Formats a list of strings into a single string.

    .. code:: python3

        format_text( # just an example
            mbold('Hello'),
            mitalic('World')
        )

    :param args: Strings to format.
    :type args: :obj:`str`

    :param separator: The separator to use between each string.
    :type separator: :obj:`str`

    :return: The formatted string.
    :rtype: :obj:`str`
    """
    return separator.join(args)



def escape_html(content: str) -> str:
    """
    Escapes HTML characters in a string of HTML.

    :param content: The string of HTML to escape.
    :type content: :obj:`str`

    :return: The escaped string.
    :rtype: :obj:`str`
    """
    return html.escape(content)


def escape_markdown(content: str) -> str:
    """
    Escapes Markdown characters in a string of Markdown.

    Credits to: simonsmh

    :param content: The string of Markdown to escape.
    :type content: :obj:`str`

    :return: The escaped string.
    :rtype: :obj:`str`
    """
    
    parse = re.sub(r"([_*\[\]()~`>\#\+\-=|\.!\{\}])", r"\\\1", content)
    return re.sub(r"\\\\([_*\[\]()~`>\#\+\-=|\.!\{\}])", r"\1", parse) 


def mbold(content: str, escape: Optional[bool]=True) -> str:
    """
    Returns a Markdown-formatted bold string.

    :param content: The string to bold.
    :type content: :obj:`str`

    :param escape: True if you need to escape special characters. Defaults to True.
    :type escape: :obj:`bool`

    :return: The formatted string.
    :rtype: :obj:`str`
    """
    return f'*{escape_markdown(content) if escape else content}*'


def hbold(content: str, escape: Optional[bool]=True) -> str:
    """
    Returns an HTML-formatted bold string.

    :param content: The string to bold.
    :type content: :obj:`str`

    :param escape: True if you need to escape special characters. Defaults to True.
    :type escape: :obj:`bool`

    :return: The formatted string.
    :rtype: :obj:`str`
    """
    return f'<b>{escape_html(content) if escape else content}</b>'


def mitalic(content: str, escape: Optional[bool]=True) -> str:
    """
    Returns a Markdown-formatted italic string.

    :param content: The string to italicize.
    :type content: :obj:`str`

    :param escape: True if you need to escape special characters. Defaults to True.
    :type escape: :obj:`bool`

    :return: The formatted string.
    :rtype: :obj:`str`
    """
    return f'_{escape_markdown(content) if escape else content}_\r'


def hitalic(content: str, escape: Optional[bool]=True) -> str:
    """
    Returns an HTML-formatted italic string.

    :param content: The string to italicize.
    :type content: :obj:`str`

    :param escape: True if you need to escape special characters. Defaults to True.
    :type escape: :obj:`bool`

    :return: The formatted string.
    :rtype: :obj:`str`
    """
    return f'<i>{escape_html(content) if escape else content}</i>'


def munderline(content: str, escape: Optional[bool]=True) -> str:
    """
    Returns a Markdown-formatted underline string.

    :param content: The string to underline.
    :type content: :obj:`str`

    :param escape: True if you need to escape special characters. Defaults to True.
    :type escape: :obj:`bool`

    :return: The formatted string.
    :rtype: :obj:`str`
    """
    return f'__{escape_markdown(content) if escape else content}__'


def hunderline(content: str, escape: Optional[bool]=True) -> str:
    """
    Returns an HTML-formatted underline string.

    :param content: The string to underline.
    :type content: :obj:`str`

    :param escape: True if you need to escape special characters. Defaults to True.
    :type escape: :obj:`bool`

    :return: The formatted string.
    :rtype: :obj:`str`

    """
    return f'<u>{escape_html(content) if escape else content}</u>'


def mstrikethrough(content: str, escape: Optional[bool]=True) -> str:
    """
    Returns a Markdown-formatted strikethrough string.

    :param content: The string to strikethrough.
    :type content: :obj:`str`

    :param escape: True if you need to escape special characters. Defaults to True.
    :type escape: :obj:`bool`

    :return: The formatted string.
    :rtype: :obj:`str`
    """
    return f'~{escape_markdown(content) if escape else content}~'


def hstrikethrough(content: str, escape: Optional[bool]=True) -> str:
    """
    Returns an HTML-formatted strikethrough string.

    :param content: The string to strikethrough.
    :type content: :obj:`str`

    :param escape: True if you need to escape special characters. Defaults to True.
    :type escape: :obj:`bool`

    :return: The formatted string.
    :rtype: :obj:`str`
    """
    return f'<s>{escape_html(content) if escape else content}</s>'


def mspoiler(content: str, escape: Optional[bool]=True) -> str:
    """
    Returns a Markdown-formatted spoiler string.

    :param content: The string to spoiler.
    :type content: :obj:`str`

    :param escape: True if you need to escape special characters. Defaults to True.
    :type escape: :obj:`bool`

    :return: The formatted string.
    :rtype: :obj:`str`
    """
    return f'||{escape_markdown(content) if escape else content}||'


def hspoiler(content: str, escape: Optional[bool]=True) -> str:
    """
    Returns an HTML-formatted spoiler string.

    :param content: The string to spoiler.
    :type content: :obj:`str`

    :param escape: True if you need to escape special characters. Defaults to True.
    :type escape: :obj:`bool`

    :return: The formatted string.
    :rtype: :obj:`str`
    """
    return f'<tg-spoiler>{escape_html(content) if escape else content}</tg-spoiler>'


def mlink(content: str, url: str, escape: Optional[bool]=True) -> str:
    """
    Returns a Markdown-formatted link string.

    :param content: The string to link.
    :type content: :obj:`str`

    :param url: The URL to link to.
    :type url: str

    :param escape: True if you need to escape special characters. Defaults to True.
    :type escape: :obj:`bool`

    :return: The formatted string.
    :rtype: :obj:`str`
    """
    return f'[{escape_markdown(content)}]({escape_markdown(url) if escape else content})'


def hlink(content: str, url: str, escape: Optional[bool]=True) -> str:
    """
    Returns an HTML-formatted link string.

    :param content: The string to link.
    :type content: :obj:`str`

    :param url: The URL to link to.
    :type url: :obj:`str`

    :param escape: True if you need to escape special characters. Defaults to True.
    :type escape: :obj:`bool`

    :return: The formatted string.
    :rtype: :obj:`str`
    """
    return f'<a href="{escape_html(url)}">{escape_html(content) if escape else content}</a>'


def mcode(content: str, language: str="", escape: Optional[bool]=True) -> str:
    """
    Returns a Markdown-formatted code string.

    :param content: The string to code.
    :type content: :obj:`str`

    :param escape: True if you need to escape special characters. Defaults to True.
    :type escape: :obj:`bool`

    :return: The formatted string.
    :rtype: :obj:`str`
    """
    return f'```{language}\n{escape_markdown(content) if escape else content}```'


def hcode(content: str, escape: Optional[bool]=True) -> str:
    """
    Returns an HTML-formatted code string.

    :param content: The string to code.
    :type content: :obj:`str`

    :param escape: True if you need to escape special characters. Defaults to True.
    :type escape: :obj:`bool`

    :return: The formatted string.
    :rtype: :obj:`str`
    """
    return f'<code>{escape_html(content) if escape else content}</code>'


def hpre(content: str, escape: Optional[bool]=True, language: str="") -> str:
    """
    Returns an HTML-formatted preformatted string.

    :param content: The string to preformatted.
    :type content: :obj:`str`

    :param escape: True if you need to escape special characters. Defaults to True.
    :type escape: :obj:`bool`

    :return: The formatted string.
    :rtype: :obj:`str`
    """
    return f'<pre><code class="{language}">{escape_html(content) if escape else content}</code></pre>'


def hide_link(url: str) -> str:
    """
    Hide url of an image.

    :param url: The url of the image.
    :type url: :obj:`str`
    
    :return: The hidden url.
    :rtype: :obj:`str`
    """
    return f'<a href="{url}">&#8288;</a>'
