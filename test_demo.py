def test_slash_join():
    assert slash_join_strings('abc', 'def') == 'abc/def'

def slash_join_strings(s1, s2):
    """
    Joins two strings on a slash

    >>> slash_join_strings('hello', 'world')
    'hello/world'

    """

    return "/".join((s1, s2))

