from dbutils.utils import statistic_for_ip
from dbutils.utils import get_all_db_entries

print 'Theres are ' + statistic_for_ip('192.168.43.190') + 'entries in database'

print 'All entries in database are as follow:'
get_all_db_entries()