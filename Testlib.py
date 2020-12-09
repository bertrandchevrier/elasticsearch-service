from elasticsearch_service.elasticsearch_service import ElasticsearchService
import os
import urllib3
import requests
#
# elk_service=ElasticsearchService('localhost',9200,scheme = 'https',http_auth_username= 'admin', http_auth_password= 'admin')
#
# list_of_values=[{'_id':'myid1','field1':'value1','field2':'value2','date':'2016-07-15T15:29:50+02:00'},{'_id':'myid2','field1':'value33','field2':'value4','date':'2016-07-15T15:29:50+02:00'}]
# elk_service.import_documents('myelk-index',list_of_values)

urllib3.disable_warnings()

os.environ['http_proxy']='http://proxypac.si.francetelecom.fr:8080'
os.environ['https_proxy']='http://proxypac.si.francetelecom.fr:8080'

elk_service=ElasticsearchService('https://es-home.si.francetelecom.fr',443,scheme = 'https',http_auth_username = 'beic7342',http_auth_password='AccesKES93')

list_of_values=[{'_id':'myid1','field1':'value1','field2':'value2','date':'2020-07-15T15:29:50+02:00'},{'_id':'myid2','field1':'value33','field2':'value4','date':'2020-07-15T15:29:50+02:00'}]
elk_service.import_documents('myelk-index',list_of_values)

hits=elk_service.get_documents('myelk-index')
hits=elk_service.get_documents('smartlife-lo-commandstatus')
#hits=elk_service.get_documents('smartlife-lo-commandStatus',timefield='created',startdate='2020-07-01',enddate='2020-07-15')

print(hits)

for hit in hits:
    print(hit)

