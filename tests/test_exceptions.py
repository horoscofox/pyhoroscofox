import pytest

from horoscofox import paolo, branko
from horoscofox.errors import AstrologerException
from requests.exceptions import ConnectionError


def test_exceptions_raises_nosign_and_date():
    with pytest.raises(AstrologerException) as excinfo:
        paolo.get(sign='sign-not-in-list', kind='tomorrow')
    assert "Sign not allowed, did you mean one of ['capricorn', 'acquarius', 'pisces', 'aries', 'taurus', 'gemini', 'cancer', 'leo', 'virgo', 'libra', 'scorpio', 'sagittarius']" in str(
        excinfo.value)
    with pytest.raises(AstrologerException) as excinfo:
        branko.get(sign='sign-not-in-list')
    assert "Sign not allowed, did you mean one of ['capricorn', 'acquarius', 'pisces', 'aries', 'taurus', 'gemini', 'cancer', 'leo', 'virgo', 'libra', 'scorpio', 'sagittarius']" in str(
        excinfo.value)


def test_exceptions_raises_virgo_and_nodate():
    with pytest.raises(AstrologerException) as excinfo:
        paolo.get(sign='virgo', kind='day-after-tomorrow')
    assert "Kind not allowed, did you mean one of ['today', 'tomorrow', 'week']" in str(
        excinfo.value)


def test_exceptions_using_appi(mocker):
    mocked_post = mocker.patch('horoscofox.signs.paolosign.requests.post')
    mocked_post.return_value.status_code = 500
    mocked_get = mocker.patch('horoscofox.signs.brankosign.requests.get')
    mocked_get.return_value.status_code = 500
    with pytest.raises(AstrologerException) as excinfo:
        paolo.get(sign='virgo', kind='today')
    assert 'Error using API!' in str(excinfo.value)
    with pytest.raises(AstrologerException) as excinfo:
        branko.get(sign='virgo', kind='today')
    assert 'Error using API!' in str(excinfo.value)


def test_exceptions_using_connection_error(mocker):
    mocked_post = mocker.patch('horoscofox.signs.paolosign.requests.post')
    mocked_get = mocker.patch('horoscofox.signs.brankosign.requests.get')
    mocked_get.side_effect = mocked_post.side_effect = ConnectionError()
    with pytest.raises(AstrologerException) as excinfo:
        paolo.get(sign='virgo', kind='today')
    assert 'Connection error!' in str(excinfo.value)
    with pytest.raises(AstrologerException) as excinfo:
        branko.get(sign='virgo', kind='today')
    assert 'Connection error!' in str(excinfo.value)


def test_exceptions_branko_not_today(mocker):
    with pytest.raises(AstrologerException) as excinfo:
        branko.get(sign='virgo', kind='day-after-tomorrow')
    assert "Sorry, at the moment Branko can see only today's horoscope" in str(
        excinfo.value)
