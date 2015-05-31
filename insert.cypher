// insert all with education and uuid
LOAD CSV WITH HEADERS FROM
// "file:///Users/ddymke/Documents/workspace/neo4jhacker/resources/profile.csv"
"file:///home/k/hackstuff/neo4j-hackaton/neo4jhacker/resources/profile.csv"
AS csvLine
MERGE (p:Person {uuid: csvLine.uuid, firstName: csvLine.first_name, lastName: csvLine.last_name, profile: csvLine.url_profile, education: csvLine.education  })
MERGE (gender:Gender {name: csvLine.gender})
MERGE (party:Party {name: csvLine.party})
foreach (x in split(csvLine.education,",") | MERGE(ed:Education {name: x})
MERGE (p)-[:IS_EDUCATED]->(ed))
MERGE (p)-[:IN_PARTY]->(party)
MERGE (p)<-[:HAS_GENDER]-(gender)
RETURN p
;
