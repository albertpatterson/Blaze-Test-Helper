from ..main.runAllTests import getKarmaTests
from ..main.runAllTests import getAllKarmaTests
from ..main.runAllTests import google3Location
from os import path

testingPath = path.join(google3Location, 'src/test/testing')


def test_getKarmaTests():
    tests = getKarmaTests(path.join(testingPath, 'BUILD'))
    assert len(tests) == 1

    tests = getKarmaTests(path.join(testingPath, 'sub1/BUILD'))
    assert len(tests) == 2


def test_getAllKarmaTests():
    tests = getAllKarmaTests(testingPath)
    assert len(tests) == 3
    sorted(tests, key=lambda t: "%s:%s" % (t.path, t.name))
    assert tests[0].name == 'name_Of-Test'
    assert tests[0].path == testingPath

    assert tests[1].name == 'test11'
    assert tests[1].path == path.join(testingPath, 'sub1')

    assert tests[2].name == 'test22'
    assert tests[2].path == path.join(testingPath, 'sub1')
