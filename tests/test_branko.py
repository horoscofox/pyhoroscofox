import horoscofox

from datetime import datetime
from horoscofox import branko


def test_client_today(mocker):
    mock_response = {
        "success": 1,
        "oroscopo": [
            {"segno": "SCORPIONE",
             "oroscopo": "Amore, amicizia, fortuna. schiarite e influssi positivi arrivano all'improvviso.",
             "createdAt": "2018-04-07 07:15:14",
             }
        ]
    }

    mocked_post = mocker.patch('horoscofox.signs.brankosign.requests.get')
    mocked_post.return_value.status_code = 200
    mocked_post.return_value.json.return_value = mock_response

    resp = branko.scorpio.today()
    assert resp.text == "Amore, amicizia, fortuna. schiarite e influssi positivi arrivano all'improvviso."
    assert resp.date_start == datetime(2018, 4, 7, 15, 14).date()

    resp = branko.get(sign='scorpio', kind='today')
    assert resp.text == "Amore, amicizia, fortuna. schiarite e influssi positivi arrivano all'improvviso."
    assert resp.date_start == datetime(2018, 4, 7, 15, 14).date()


def test_client_json_response(mocker):
    mock_response = {
        "success": 1,
        "oroscopo": [
            {"segno": "VERGINE",
             "oroscopo": "Per ogni fine c’è un nuovo inizio",
             "createdAt": "2018-04-07 07:15:14",
             }
        ]
    }

    mocked_post = mocker.patch('horoscofox.signs.brankosign.requests.get')
    mocked_post.return_value.status_code = 200
    mocked_post.return_value.json.return_value = mock_response

    resp = branko.get(sign='virgo').json()
    assert resp['text'] == "Per ogni fine c’è un nuovo inizio"
    assert resp['date_start'] == '2018-04-07'
