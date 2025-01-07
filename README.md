# Callink_Spider
To extract all website keys:

```bash
scrapy crawl callinks -O callinks.json
```

To extract organization names and emails:

```bash
scrapy crawl organizations -O organizations.json
```

To convert `organizations.json` to csv:

```bash
python to_csv.py
```
