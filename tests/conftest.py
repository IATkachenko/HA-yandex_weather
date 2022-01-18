"""Global fixtures"""
from unittest.mock import patch, AsyncMock
import pytest


@pytest.fixture(name="bypass_get_data")
def bypass_get_data_fixture():
    """Skip calls to get data from API."""
    with patch(
        "custom_components.yandex_weather.updater.WeatherUpdater.request",
        AsyncMock(return_value='{"now":1642149940,"now_dt":"2022-01-14T08:45:40.109699Z","info":{"url":"https://yandex.com/weather/213?lat=55.753215\u0026lon=37.622504","lat":55.753215,"lon":37.622504},"fact":{"obs_time":1642147200,"temp":1,"feels_like":-5,"icon":"bkn_d","condition":"cloudy","wind_speed":6.2,"wind_dir":"w","pressure_mm":723,"pressure_pa":963,"humidity":89,"daytime":"d","polar":false,"season":"winter","wind_gust":13.9},"forecast":{"date":"2022-01-14","date_ts":1642107600,"week":2,"sunrise":"08:50","sunset":"16:25","moon_code":14,"moon_text":"moon-code-14","parts":[{"part_name":"day","temp_min":0,"temp_avg":1,"temp_max":1,"wind_speed":6.5,"wind_gust":11.2,"wind_dir":"nw","pressure_mm":723,"pressure_pa":963,"humidity":87,"prec_mm":0.6,"prec_prob":90,"prec_period":360,"icon":"ovc_ra_sn","condition":"wet-snow","feels_like":-6,"daytime":"d","polar":false},{"part_name":"evening","temp_min":-1,"temp_avg":-1,"temp_max":0,"wind_speed":9.1,"wind_gust":14,"wind_dir":"nw","pressure_mm":722,"pressure_pa":962,"humidity":84,"prec_mm":0.6,"prec_prob":40,"prec_period":360,"icon":"ovc_ra_sn","condition":"wet-snow","feels_like":-10,"daytime":"n","polar":false}]}}')
    ):
        yield
