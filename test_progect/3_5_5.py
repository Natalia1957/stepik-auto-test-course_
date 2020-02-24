import pytest


# Изучите самостоятельно документацию про маркировку xfail. Найдите там параметр, который в случае неожиданного
# прохождение теста, помеченного как xfail, в отчете пометит этот тест как упавший.
# Пометьте таким образом первый тест из этого тестового набора:
@pytest.mark.xfail(strict=True)
def test_succeed():
    assert True


@pytest.mark.xfail
def test_not_succeed():
    assert False


@pytest.mark.skip
def test_skipped():
    assert False