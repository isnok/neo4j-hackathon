abgeordnetenwatch.de Visualizer
===============================

Trying out neo4j at the neo4j hackathon.


Setup / Installation
====================

To start off we took the file `deputies.xml` provided by abgeordnetenwatch.de, and transformed it into a CSV file using:

http://xmlgrid.net/xml2text.html

The result was `profile.csv`.

That file was read into our neo4j database, using the query from `insert.cypher`.

Then we built a scraper (`elections.py`), to scrape the election votes of each deputy.
The results of the scraping is collected in `all_elections.csv'.
This file is included into the dataset via `elections.cypher`.

So, in order to make this database, you will need to run:

```
bin/neoj4-shell -file <path-to>/insert.cypher
bin/neoj4-shell -file <path-to>/elections.cypher
```
