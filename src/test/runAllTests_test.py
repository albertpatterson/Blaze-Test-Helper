from ..main.runAllTests import getKarmaTests
from ..main.runAllTests import getAllKarmaTests

from os import path


def test_getKarmaTests():
    tests = getKarmaTests('src/test/testing/BUILD')
    assert len(tests) == 1

    tests = getKarmaTests('src/test/testing/sub1/BUILD')
    assert len(tests) == 2


def test_getAllKarmaTests():
    tests = getAllKarmaTests('src/test/testing')
    assert len(tests) == 3
    sorted(tests, key=lambda t: "%s:%s" % (t.path, t.name))
    assert tests[0].name == 'name_Of-Test'
    assert tests[0].path == 'src/test/testing'

    assert tests[1].name == 'test11'
    assert tests[1].path == 'src/test/testing/sub1'

    assert tests[2].name == 'test22'
    assert tests[2].path == 'src/test/testing/sub1'
