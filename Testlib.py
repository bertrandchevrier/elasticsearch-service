from elasticsearch_service.elasticsearch_service import ElasticsearchService

elk_service=ElasticsearchService('localhost',9200,scheme = 'https',http_auth_username= 'admin', http_auth_password= 'admin')

list_of_values=[{'_id':'myid1','field1':'value1','field2':'value2','date':'2016-07-15T15:29:50+02:00'},{'_id':'myid2','field1':'value33','field2':'value4','date':'2016-07-15T15:29:50+02:00'}]
elk_service.import_documents('myelk-index',list_of_values)