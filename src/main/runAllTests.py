import os
import re
from os import path
import subprocess

parentFolderPaths = [
    'src/test/testing'
]


class Test:
    def __init__(self, path, name):
        self.path = path
        self.name = name


def getAllKarmaTests(searchPath):
    tests = []
    buildFilePath = path.join(searchPath, 'BUILD')
    if path.isfile(buildFilePath):
        tests += getKarmaTests(buildFilePath)
        # tests.append(Test(searchPath, 'example'))

    folderContents = os.listdir(searchPath)
    for item in folderContents:
        itemPath = path.join(searchPath, item)
        if path.isdir(itemPath):
            tests += getAllKarmaTests(itemPath)

    return tests


def getKarmaTests(buildFilePath):
    folder = path.dirname(buildFilePath)

    tests = []
    with open(buildFilePath, 'r') as buildFile:
        buildFileText = buildFile.read()
        testNames = re.findall(
            r'karma_web_test_suite\([^\)]*name\s*=\s*[\'"]([\w_-]*)[\'"]', buildFileText)
        tests += [Test(folder, name) for name in testNames]

    return tests


def runTest(path, name):
    pass


def blazeTest(tests):
    cmd = ['blaze', 'test'] + ['%s:%s' %
                               (test.path, test.name) for test in tests]

    subprocess.run(' '.join(cmd), shell=True, check=True)


if __name__ == '__main__':
    allTests = []

    for parentFolderPath in parentFolderPaths:
        allTests += getAllKarmaTests(parentFolderPath)

    blazeTest(allTests)
