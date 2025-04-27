
import json
import pytest
import pandas as pd
from pandas import DataFrame

class dataanalytics:
    def __init__(self, data: DataFrame):
        self.data = data
        self.copy_data = data.copy()
        self.data_backup = self.data
        self.temp_data = pd.DataFrame()
        self.cache = {}

    def getStreamerStats(self, streamer: str):
        data = None
        if streamer is not None and streamer != '':
            data = self.data[self.data['Channel'] == streamer]
        else:
            return json.dumps(
                {"average_viewers": 0, "total_watch_time": 0, "stream_time": 0},
                indent=4, ensure_ascii=False
            )

        stats = {
            "average_viewers": int(data['Average viewers'].mean()) if data is not None else 0,
            "total_watch_time": int(data['Watch time(Minutes)'].sum()) if data is not None else 0,
            "stream_time": int(data['Stream time(minutes)'].sum()) if data is not None else 0
        }

        return json.dumps(stats, indent=4, ensure_ascii=False)


@pytest.fixture
def sample_data():
    data = {
        'Channel': ['Streamer1', 'Streamer2', 'Streamer1'],
        'Average viewers': [100, 150, 200],
        'Watch time(Minutes)': [500, 300, 700],
        'Stream time(minutes)': [60, 45, 90]
    }
    return pd.DataFrame(data)

def test_get_streamer_stats_success(sample_data):
    da = dataanalytics(sample_data)
    expected_output = {
        "average_viewers": 150,
        "total_watch_time": 1200,
        "stream_time": 150
    }
    result = json.loads(da.getStreamerStats('Streamer1'))
    assert result == expected_output

def test_get_streamer_stats_invalid_streamer(sample_data):
    da = dataanalytics(sample_data)
    expected_output = {
        "average_viewers": 0,
        "total_watch_time": 0,
        "stream_time": 0
    }
    result = json.loads(da.getStreamerStats(''))
    assert result == expected_output
