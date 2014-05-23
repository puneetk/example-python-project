from bugs import greet


def test_greet():
    result = 'What\'s up, Granny?'
    assert greet.greet('Granny') == result, 'bad greeting'
