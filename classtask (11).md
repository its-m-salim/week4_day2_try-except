# Week 4, Day 1 — Classwork: Exceptions and Debugging

## 1. Safe Division

**English**
Read two values as strings, convert them to numbers, and divide the first by the second. Catch `ValueError` and `ZeroDivisionError` separately. Use `else` to print a successful result and `finally` to always print `Calculation finished`. Do not use a broad `except` for these expected errors.

**Тоҷикӣ**
Ду қиматро ҳамчун string хонда, ба рақам табдил диҳед ва якумро ба дуюм тақсим кунед. `ValueError` ва `ZeroDivisionError`-ро алоҳида коркард кунед. Дар `else` натиҷаи муваффақ ва дар `finally` ҳамеша `Calculation finished`-ро чоп кунед. Барои ин хатоҳои пешбинишуда `except`-и умумиро истифода набаред.

**Русский**
Считайте два значения как строки, преобразуйте их в числа и разделите первое на второе. Обработайте `ValueError` и `ZeroDivisionError` отдельно. В `else` выведите успешный результат, а в `finally` всегда выводите `Calculation finished`. Не используйте общий `except` для этих ожидаемых ошибок.

**Input**

    20
    4

**Output**

    Result: 5.0
    Calculation finished

------------------------------------------------------------------------

## 2. Safe List Position

**English**
Given a fixed list of city names, read an index and print the selected city. Handle a non-integer index with `ValueError` and an unavailable position with `IndexError`. Negative indexes are not allowed and must be rejected explicitly with `raise IndexError`. Print a different clear message for each problem.

**Тоҷикӣ**
Бо рӯйхати тайёри номи шаҳрҳо index-ро хонда, шаҳри интихобшударо чоп кунед. Index-и integer набударо бо `ValueError` ва position-и мавҷуд набударо бо `IndexError` коркард кунед. Index-и манфӣ иҷозат нест ва бояд бевосита бо `raise IndexError` рад карда шавад. Барои ҳар мушкил message-и равшан чоп кунед.

**Русский**
Используя готовый список городов, считайте индекс и выведите выбранный город. Нецелый индекс обработайте через `ValueError`, а отсутствующую позицию — через `IndexError`. Отрицательные индексы запрещены и должны явно отклоняться через `raise IndexError`. Для каждой проблемы выведите отдельное понятное сообщение.

**Input**

    Cities: ['Dushanbe', 'Khujand', 'Bokhtar']
    5

**Output**

    Position does not exist

------------------------------------------------------------------------

## 3. Product Price Lookup

**English**
Use a dictionary of product names and prices. Read a product name and quantity, then print the total price. Handle an unknown product with `KeyError`, an invalid quantity with `ValueError`, and reject a non-positive quantity by raising `ValueError` yourself. Use `else` for the successful calculation.

**Тоҷикӣ**
Dictionary-и ном ва нархи маҳсулотро истифода баред. Номи маҳсулот ва quantity-ро хонда, total price-ро чоп кунед. Маҳсулоти номаълумро бо `KeyError`, quantity-и нодурустро бо `ValueError` коркард кунед ва quantity-и ғайримусбатро худатон бо `raise ValueError` рад намоед. Барои ҳисоби муваффақ `else`-ро истифода баред.

**Русский**
Используйте словарь названий и цен товаров. Считайте название товара и количество, затем выведите общую стоимость. Неизвестный товар обработайте через `KeyError`, неверное количество — через `ValueError`, а неположительное количество отклоните самостоятельно с помощью `raise ValueError`. Успешный расчёт выполняйте в `else`.

**Input**

    Prices: {'mouse': 100, 'keyboard': 250, 'monitor': 1200}
    keyboard
    3

**Output**

    Total: 750

------------------------------------------------------------------------

## 4. Catch the Right Exception

**English**
Create `calculate_average(values)` that converts a list of strings to integers and returns their average. Write handlers in the correct order for `ValueError`, `ZeroDivisionError`, and an unexpected `Exception`. Print the exception class name and message. Test valid input, an invalid value, and an empty list, and explain why the broad handler must be last.

**Тоҷикӣ**
`calculate_average(values)` созед, ки рӯйхати string-ҳоро ба integer табдил дода, average-ро бармегардонад. Handler-ҳоро барои `ValueError`, `ZeroDivisionError` ва `Exception`-и ғайричашмдошт бо тартиби дуруст нависед. Номи class-и exception ва message-и онро чоп кунед. Input-и дуруст, қимати нодуруст ва рӯйхати холиро санҷида, фаҳмонед, ки чаро handler-и умумӣ бояд охир бошад.

**Русский**
Создайте `calculate_average(values)`, преобразующую список строк в целые числа и возвращающую среднее. Расположите обработчики `ValueError`, `ZeroDivisionError` и неожиданного `Exception` в правильном порядке. Выводите имя класса исключения и его сообщение. Проверьте корректный ввод, неверное значение и пустой список и объясните, почему общий обработчик должен находиться последним.

**Input**

    10 20 30
    10 abc 30
    (empty list)

**Output**

    Average: 20.0
    ValueError: invalid literal for int() with base 10: 'abc'
    ZeroDivisionError: division by zero

------------------------------------------------------------------------

## 5. Validation with `raise`

**English**
Write `register_participant(name, age)` with explicit validation. Raise `TypeError` when `name` is not a string or `age` is not an integer. Raise `ValueError` when the stripped name is empty or age is outside 18–100. Return a participant dictionary only for valid data. Call the function in `try/except` and print specific error messages.

**Тоҷикӣ**
`register_participant(name, age)`-ро бо validation-и равшан нависед. Агар `name` string ё `age` integer набошад, `TypeError` raise кунед. Агар номи тозашуда холӣ ё age берун аз 18–100 бошад, `ValueError` raise кунед. Танҳо барои маълумоти дуруст dictionary-и participant баргардонед. Function-ро дар `try/except` даъват карда, message-и мушаххас чоп кунед.

**Русский**
Напишите `register_participant(name, age)` с явной проверкой. Выбрасывайте `TypeError`, если `name` не является строкой или `age` — целым числом. Выбрасывайте `ValueError`, если очищенное имя пустое или возраст находится вне диапазона 18–100. Возвращайте словарь участника только для допустимых данных. Вызывайте функцию в `try/except` и выводите конкретные сообщения.

**Input**

    Ali 22
    Sara seventeen
    Bob 15

**Output**

    Registered: {'name': 'Ali', 'age': 22}
    TypeError: age must be an integer
    ValueError: age must be from 18 to 100

------------------------------------------------------------------------

## 6. Custom Bank Exception

**English**
Create a custom `InsufficientFundsError(Exception)`. Create `BankAccount` with `owner`, private balance, `deposit()`, and `withdraw()`. Raise `ValueError` for a non-positive amount and `InsufficientFundsError` when the balance is too small. Catch the two errors separately outside the class and prove that failed operations do not change the balance.

**Тоҷикӣ**
Exception-и custom-и `InsufficientFundsError(Exception)` созед. `BankAccount` бояд `owner`, balance-и private, `deposit()` ва `withdraw()` дошта бошад. Барои amount-и ғайримусбат `ValueError` ва барои нокифоя будани balance `InsufficientFundsError` raise кунед. Ҳар ду хатогиро берун аз class алоҳида коркард карда, нишон диҳед, ки амалиёти ноком balance-ро тағйир намедиҳад.

**Русский**
Создайте пользовательское исключение `InsufficientFundsError(Exception)`. Класс `BankAccount` должен иметь `owner`, приватный баланс, `deposit()` и `withdraw()`. Для неположительной суммы выбрасывайте `ValueError`, для нехватки средств — `InsufficientFundsError`. Обработайте ошибки отдельно вне класса и докажите, что неудачные операции не меняют баланс.

**Input**

    Ali 500
    withdraw 700
    deposit -10
    withdraw 200

**Output**

    InsufficientFundsError: requested 700, available 500
    ValueError: amount must be positive
    Withdrawal completed
    Balance: 300

------------------------------------------------------------------------

## 7. `else` and `finally` in a Payment

**English**
Create `process_payment(balance, amount)` that raises `ValueError` for a non-positive amount and `InsufficientFundsError` for insufficient money. In the caller, use `try` for the operation, separate `except` blocks, `else` to print the new balance only after success, and `finally` to print `Payment attempt finished` every time.

**Тоҷикӣ**
`process_payment(balance, amount)` созед, ки барои amount-и ғайримусбат `ValueError` ва барои пули нокифоя `InsufficientFundsError` raise мекунад. Дар қисми даъват `try`, `except`-ҳои алоҳида, `else` барои чопи balance-и нав танҳо баъди муваффақият ва `finally` барои чопи доимии `Payment attempt finished` истифода баред.

**Русский**
Создайте `process_payment(balance, amount)`, выбрасывающую `ValueError` для неположительной суммы и `InsufficientFundsError` при нехватке денег. При вызове используйте `try`, отдельные блоки `except`, `else` для вывода нового баланса только после успеха и `finally`, всегда выводящий `Payment attempt finished`.

**Input**

    Balance: 1000
    Payment: 250

**Output**

    New balance: 750
    Payment attempt finished

------------------------------------------------------------------------

## 8. Read a Traceback Bottom to Top

**English**
Run the code below without changing it. Starting from the last traceback line, write down: exception type, message, failing line, and the chain of function calls. Then fix only the real cause so the program prints the expected result. Do not guess from the first traceback line.

**Тоҷикӣ**
Code-и зерро бе тағйир иҷро кунед. Аз сатри охирини traceback сар карда, exception type, message, сатри хато ва занҷири function call-ҳоро нависед. Баъд танҳо сабаби аслиро ислоҳ кунед, то output-и интизоршуда барояд. Аз сатри якуми traceback тахмин накунед.

**Русский**
Запустите код ниже без изменений. Начиная с последней строки traceback, запишите тип исключения, сообщение, строку ошибки и цепочку вызовов функций. Затем исправьте только настоящую причину, чтобы получить ожидаемый результат. Не пытайтесь угадать ошибку по первой строке traceback.

```python
def price_per_item(total, quantity):
    return total / quantity


def build_report(order):
    return price_per_item(order["total"], order["quantity"])


def main():
    order = {"total": 600, "quantity": 0}
    print(build_report(order))


main()
```

**Input**

    total=600, quantity must be 3

**Output**

    200.0

------------------------------------------------------------------------

## 9. VS Code Debugger: Cart Total

**English**
Debug the program below using VS Code breakpoints, Step Over, Step Into, and the Variables/Watch panels. Do not add diagnostic `print()` calls. Watch `index`, `price`, `quantity`, and `total`, find why only the last item affects the result, fix the smallest possible line, and remove breakpoints after verification.

**Тоҷикӣ**
Барномаи зерро бо VS Code breakpoints, Step Over, Step Into ва Variables/Watch panel debug кунед. Diagnostic `print()` илова накунед. `index`, `price`, `quantity`, `total`-ро watch карда, сабаби таъсир кардани танҳо item-и охиринро ёбед, хурдтарин ислоҳро иҷро кунед ва баъди санҷиш breakpoint-ҳоро нест кунед.

**Русский**
Отладьте программу ниже с помощью точек останова VS Code, Step Over, Step Into и панелей Variables/Watch. Не добавляйте диагностические `print()`. Наблюдайте `index`, `price`, `quantity`, `total`, найдите причину влияния только последнего товара, исправьте минимально возможную строку и удалите точки останова после проверки.

```python
def line_total(price, quantity):
    return price * quantity


def cart_total(items):
    total = 0
    for index, item in enumerate(items):
        price = item["price"]
        quantity = item["quantity"]
        total = line_total(price, quantity)
    return total


cart = [
    {"name": "Mouse", "price": 100, "quantity": 2},
    {"name": "Keyboard", "price": 250, "quantity": 1},
    {"name": "Cable", "price": 30, "quantity": 3},
]
print(cart_total(cart))
```

**Input**

    (no input — use the provided cart)

**Output**

    540

------------------------------------------------------------------------

## 10. `breakpoint()`, `pdb`, and Documentation

**English**
The date parser uses the wrong format. First run it and read the `ValueError` traceback bottom to top. Place `breakpoint()` before the parser call and use at least `p text`, `s`, `n`, and `c` in `pdb`. Look up `datetime.strptime` in the official Python documentation first; use Stack Overflow only if the documentation is insufficient. Fix the format and add specific `ValueError` handling for invalid dates. Remove `breakpoint()` when finished.

**Тоҷикӣ**
Date parser format-и нодуруст дорад. Аввал онро иҷро карда, traceback-и `ValueError`-ро аз поён ба боло хонед. Пеш аз parser call `breakpoint()` гузошта, дар `pdb` камаш `p text`, `s`, `n`, `c`-ро истифода баред. Аввал `datetime.strptime`-ро дар documentation-и расмии Python ҷустуҷӯ кунед; танҳо агар он кофӣ набошад Stack Overflow-ро истифода баред. Format-ро ислоҳ карда, барои санаи нодуруст `ValueError`-и мушаххасро коркард кунед. Дар охир `breakpoint()`-ро нест кунед.

**Русский**
Парсер даты использует неверный формат. Сначала запустите его и прочитайте traceback `ValueError` снизу вверх. Поставьте `breakpoint()` перед вызовом парсера и используйте в `pdb` как минимум `p text`, `s`, `n`, `c`. Сначала найдите `datetime.strptime` в официальной документации Python; обращайтесь к Stack Overflow, только если документации недостаточно. Исправьте формат и добавьте конкретную обработку `ValueError` для неверной даты. После завершения удалите `breakpoint()`.

```python
from datetime import datetime


def parse_date(text):
    return datetime.strptime(text, "%d/%m/%Y")


text = input()
print(parse_date(text).strftime("%Y-%m-%d"))
```

**Input**

    07.09.2026

**Output**

    2026-09-07
