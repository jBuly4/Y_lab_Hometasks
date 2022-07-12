# Y-lab_homework 3 task 1

## Задача на циклический итератор.
Надо написать класс CyclicIterator.
Итератор должен итерироваться по итерируемому объекту (list, tuple, set, range, Range2, и т. д.), и когда достигнет 
последнего элемента, начинать сначала.

```python
cyclic_iterator = CyclicIterator(range(3))
for i in cyclic_iterator:
    print(i)
```
Основа:
```python
class CyclicIterator:
    def __iter__(self):
        pass

    def __next__(self):
        pass

```

Для проверки ожидаемый вывод:
```python
0
1
2
0
1
2
0
1
2
....
```

## Solution approach for task 1
Main idea for solution:  
We can use itertools, and it's implementation of cyclic [iterator](https://docs.python.org/3/library/itertools.html#itertools.cycle)
When we instantiate instance of our class we need to add input iterable to itertools.cycle()

## Задача на разжатие массива

У каждого фильма есть расписание, по каким дням он идёт в кинотеатрах. Для эффективности дни проката хранятся 
периодами дат. Например, прокат фильма проходит с 1 по 7 января, а потом показ возобновляется с 15 января по 7 февраля: 
```python
[
  (datetime(2020, 1, 1), datetime(2020, 1, 7)),
  (datetime(2020, 1, 15), datetime(2020, 2, 7))
]
```
**Вам дан class Movie. Реализуйте у него метод schedule. Он будет генерировать дни, в которые показывают фильм.**

**Основа:**
```python
from dataclasses import dataclass
from datetime import datetime
from typing import Generator, List, Tuple


@dataclass
class Movie:
    title: str
    dates: List[Tuple[datetime, datetime]]

    def schedule(self) -> Generator[datetime, None, None]:
        return []


m = Movie('sw', [
  (datetime(2020, 1, 1), datetime(2020, 1, 7)),
  (datetime(2020, 1, 15), datetime(2020, 2, 7))
])

for d in m.schedule():
    print(d)
```

**Для проверки. Ожидаемый вывод программы:**
```python
2020-01-01 00:00:00
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
```