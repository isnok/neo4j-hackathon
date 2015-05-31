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

Playing around with the data
============================

Here are some queries:

Find all deputies, that voted "No" on the Bundesdatenschutzgesetz.

```
MATCH ()-[r:VOTED {vote: "NEIN"}]->(Election {name: "Bundesdatenschutzgesetz"}) RETURN r;
```

To also see which parties these deputies belong to, we can extend the query as follows:

```
(p:Party)<--()-[r:VOTED {vote: "NEIN"}]->(Election {name: "Bundesdatenschutzgesetz"}) RETURN r, p;
```

If we want the database to count these groups we can use the following.
The results look best in the rows view.

```
MATCH (p:Party)<--()-[r:VOTED {vote: "NEIN"}]->(e:Election {name: "Bundesdatenschutzgesetz"}) RETURN p, e, count(r);
```

To see how many deputies of each party voted "Yes" on any election, we can use this query:

```
MATCH (p:Party)<--()-[r:VOTED {vote: "JA"}]->(e:Election) RETURN p, e, count(r);
```
