from settings import SPARQL_ENDPOINT_AUTH, SPARQL_ENDPOINT_USER, \
    SPARQL_ENDPOINT_PASSWORD, SPARQL_ENDPOINT_AUTH_MODE,\
    SPARQL_ENDPOINT_REALM
from SPARQLWrapper import SPARQLWrapper, JSON

sparql_db = SPARQLWrapper(SPARQL_ENDPOINT_AUTH)
sparql_db.setCredentials(SPARQL_ENDPOINT_USER,
                         SPARQL_ENDPOINT_PASSWORD,
                         SPARQL_ENDPOINT_AUTH_MODE,
                         SPARQL_ENDPOINT_REALM)


def query_sparql(query):
    sparql_db.setQuery(query)
    sparql_db.setReturnFormat(JSON)
    results = sparql_db.query().convert()
    return results
