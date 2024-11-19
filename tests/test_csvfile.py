import os
import pytest
from acc.csvfile import CSVFile


@pytest.fixture
def csvfile(tmp_path):
    path = os.path.join(tmp_path, 'csvfile')
    csvfile = CSVFile(path)
    yield csvfile
    try:
        os.unlink(path)
    except FileNotFoundError:
        pass


def test_path():
    assert CSVFile('foo').path == 'foo'


def test_write(csvfile):
    csvfile.write([{'a': 1, 'b': 2}])
    assert open(csvfile.path).read() == 'a,b\n1,2\n'


def test_read(csvfile):
    open(csvfile.path, mode='w').write('a,b\n1,2\n')
    assert csvfile.read() == [{'a': '1', 'b': '2'}]
