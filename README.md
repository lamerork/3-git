# Bitlink

Прграмма проверят ссылку на bit.ly
Если ссылка присутсвут на bit.ly, то возвращаем количество переход по ссылке
Если ссылка новая, то создаем коротку ссылки и возвращаем ее

### Как установить

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

### Как использовать

Пример если отправить не битлинк

```
python main.py https://google.com
```

Программа создат ссылку на битлинк

```
Битлинк: https://bit.ly/3N3hWZw
```

Если отправить битлинк

```
python main.py https://bit.ly/3N3hWZw
```

Программа вернет количество кликов по битлинку

```
Клики: 3
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).