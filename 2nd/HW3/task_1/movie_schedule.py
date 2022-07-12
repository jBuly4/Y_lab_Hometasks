from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Generator, List, Tuple


@dataclass
class Movie:
    title: str
    dates: List[Tuple[datetime, datetime]]

    def schedule(self) -> Generator[datetime, None, None]:
        for date_range in self.dates:
            current_date = date_range[0]
            while current_date <= date_range[1]:
                yield current_date
                current_date += timedelta(days=1)


if __name__ == '__main__':
    m = Movie(
        'sw', [
                (datetime(2020, 1, 1), datetime(2020, 1, 7)),
                (datetime(2020, 1, 15), datetime(2020, 2, 7))
            ]
        )

    correct_answer = """2020-01-01 00:00:00
2020-01-02 00:00:00
2020-01-03 00:00:00
2020-01-04 00:00:00
2020-01-05 00:00:00
2020-01-06 00:00:00
2020-01-07 00:00:00
2020-01-15 00:00:00
2020-01-16 00:00:00
2020-01-17 00:00:00
2020-01-18 00:00:00
2020-01-19 00:00:00
2020-01-20 00:00:00
2020-01-21 00:00:00
2020-01-22 00:00:00
2020-01-23 00:00:00
2020-01-24 00:00:00
2020-01-25 00:00:00
2020-01-26 00:00:00
2020-01-27 00:00:00
2020-01-28 00:00:00
2020-01-29 00:00:00
2020-01-30 00:00:00
2020-01-31 00:00:00
2020-02-01 00:00:00
2020-02-02 00:00:00
2020-02-03 00:00:00
2020-02-04 00:00:00
2020-02-05 00:00:00
2020-02-06 00:00:00
2020-02-07 00:00:00
"""
    answer = ""
    for date in m.schedule():
        answer += date.strftime("%Y-%m-%d %H:%M:%S") + '\n'
    assert answer == correct_answer



