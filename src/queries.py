###
### DB.DBA.RDF_GRAPH_USER_PERMS_SET ('http://graph-uri', 'nobody', 3);
### Command to run on iSQL
###
from settings import GRAPH

GET_QUERY = "select distinct ?class from <%s> {?class a owl:Class} LIMIT 100" % GRAPH

POST_QUERY = "insert data into <%s>" % GRAPH
POST_QUERY += "{<http://uri-%s> a owl:Class}"

DELETE_QUERY = "delete from <%s> {?class a owl:Class} where {?class a owl:Class}" % GRAPH
