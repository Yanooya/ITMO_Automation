def test_home_work():
    assert ('home', "work") == ('home', 'work')
def test_qa():
    assert 'QA' == 'QA'
def test_numbers():
    assert not (1, 1, 2, 3, 5) == (2, 3, 5)
