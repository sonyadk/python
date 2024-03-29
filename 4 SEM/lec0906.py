'''
https://replit.com/@sonyadk/Lectia0906#main.py

PEP 589 -- TypedDict: Type Hints for Dictionaries with a Fixed Set of Keys

В версии python 3.8 разработчики представили подсказки типов, – PEP 589, который вводит TypedDict. Его можно использовать для указания типов для ключей и значений в словаре с использованием нотации, аналогичной типизированному NamedTuple.

Традиционно, словари были аннотированы с помощью Dict. Проблема заключается в том, что это разрешает только один тип для ключей и один тип для значений, что часто приводит к аннотациям, таким как Dict[str, Any]. В качестве примера рассмотрим словарь, который регистрирует информацию о версиях Python:
'''

py38 = {"version": "3.8", "release_year": 2019}
print(py38)
'''
Значение, соответствующее version, является строкой, а release_year является целым числом, что не может быть точно представлено с помощью Dict. С новым TypedDict вы можете сделать следующее:
'''
from typing import TypedDict


class PythonVersion(TypedDict):
    version: str
    release_year: int


py38_1 = PythonVersion(version="3.8", release_year=2019)
print(py38_1)
'''
Затем средство проверки типов сможет сделать вывод, что py38 [“version”] имеет тип str, а py38 [“release_year”] является int. Во время выполнения TypedDict является обычным dict, а подсказки типов игнорируются как обычно. Вы также можете использовать TypedDict исключительно в качестве аннотации:
'''
py38_2: PythonVersion = {"version": "3.8", "release_year": 2019}
print(py38_2)
'''
Использование TypedDict имеет ряд ограничений. 
В частности:
- не поддерживаются проверки в рантайме через isinstance
- ключи должны быть литералами или final значениями
Кроме того, с таким словарем запрещены такие "небезопасные" операции как .clear или del. 
Работа по ключу, который не является литералом, также может быть запрещена, так как в этом случае невозможно определить ожидаемый тип значения.

TypedDict используется, когда нужно работать именно со словарями, например для  json-запросов.
'''
