// vote it
LOAD CSV WITH HEADERS FROM
// "file:///Users/ddymke/Desktop/all.csv" AS csvLine
"file:///home/k/hackstuff/neo4j-hackaton/neo4jhacker/all_elections.csv" AS csvLine
MATCH (p:Person {uuid: csvLine.uuid})
MERGE (elec:Election {name: csvLine.title, date: csvLine.date})
MERGE (p)-[:VOTED {vote:csvLine.vote}]->(elec)
RETURN p;
