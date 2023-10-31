import pytest

import primes


def test_sieve_1(monkeypatch, capsys, detector):
    inputs = iter([1, 10])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    sieve = primes.main()

    if detector == 4:
        expected = [0, 1, 2, 3, 0, 5, 0, 7, 0, 0, 0]
    else:
        expected = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert sieve == expected

def test_sieve_2(monkeypatch, capsys, detector):
    inputs = iter([5, 20])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    sieve = primes.main()
    if detector == 4:
        expected = [0, 1, 2, 3, 0, 5, 0, 7, 0, 0, 0, 11, 0, 13, 0, 0, 0, 17, 0, 19, 0]
    else:
        expected = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    assert sieve == expected


def test_primes_1(monkeypatch, capsys, detector):
    if detector == 1:
        print ('This test will fail with step 1')
        exit('expected to fail at this time')
    else:
        inputs = iter([1, 23])
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        primes.main()
        captured = capsys.readouterr()
        if detector <= 3:
            assert captured.out == '2\n3\n4\n5\n6\n7\n8\n9\n10\n11\n12\n13\n14\n15\n16\n17\n18\n19\n20\n21\n22\n23\n'
        else:
            assert captured.out == '2\n3\n5\n7\n11\n13\n17\n19\n23\n'


def test_primes_2(monkeypatch, capsys, detector):
    if detector <= 2:
        print ('This test will fail with step 1 and 2')
        exit('expected to fail at this time')
    else:
        inputs = iter([4, 19])
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        primes.main()
        captured = capsys.readouterr()
        if detector <= 3:
            assert captured.out == '4\n5\n6\n7\n8\n9\n10\n11\n12\n13\n14\n15\n16\n17\n18\n19\n'
        else:
            assert captured.out == '5\n7\n11\n13\n17\n19\n'

def test_primes_3(monkeypatch, capsys, detector):
    if detector <= 3:
        print ('This test will fail with step 1, 2 and 3')
        exit('expected to fail at this time')
    else:
        inputs = iter([5, 18])
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        sieve = primes.main()
        assert sieve == [0, 1, 2, 3, 0, 5, 0, 7, 0, 0, 0, 11, 0, 13, 0, 0, 0, 17, 0]
        captured = capsys.readouterr()
        assert captured.out == ('5\n7\n11\n13\n17\n')

def test_primes_4(monkeypatch, capsys, detector):
    if detector <= 3:
        print ('This test will fail with step 1, 2 and 3')
        exit('expected to fail at this time')
    else:
        inputs = iter([5, 19])
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        sieve = primes.main()
        assert sieve == [0, 1, 2, 3, 0, 5, 0, 7, 0, 0, 0, 11, 0, 13, 0, 0, 0, 17, 0, 19]
        captured = capsys.readouterr()
        assert captured.out == ('5\n7\n11\n13\n17\n19\n')

@pytest.fixture
def detector(monkeypatch, capsys):
    inputs = iter([3, 5])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    sieve = primes.main()
    output = capsys.readouterr().out

    if sieve is None:
        print('Der Befehl "return sieve" fehlt am Ende Ihres Programms')
        print('Tests können nicht durchgeführt werden')
        step = 0
    elif output == '':
        step = 1
    elif sieve[3] == 3 and sieve[4] == 0:
        step = 4
    elif output[0:1] == '2':
        step = 2
    else:
        step = 3
    return step
