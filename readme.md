Обновление базы данных
```bash
flask db migrate -m ""
flask db upgrade
```

Добавить папку с переводом на <код>
```bash
flask translate init <language-code>
```

Обновить, если есть изменения в коде строк, которые должны иметь перевод
```bash
flask translate update
```

После измений в файлах .po с переводами
```bash
flask translate compile
```