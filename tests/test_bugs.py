import bugs


def check_attr(attr):
    assert hasattr(bugs, attr), 'missing {} from bugs'.format(attr)


def test_attrs():
    for attr in [
        '__version__',
    ]:
        yield check_attr, attr
