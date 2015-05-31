abgeordnetenwatch.de Visualizer
===============================

Trying out neo4j.


Setup / Installation
====================

To start off we took the file `deputies.xml` provided by abgeordnetenwatch.de, and transformed it into a CSV file using:

http://xmlgrid.net/xml2text.html

The result was `profile.csv`.

That file was read into our neo4j database, using the query from `insert.cypher`.
