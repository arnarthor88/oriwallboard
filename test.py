import os
from dotenv import set_key, get_key


totalWaiting = int(get_key(dotenv_path='.env', key_to_get='TOTALWAITING'))
totalToday = int(get_key(dotenv_path='.env', key_to_get='TOTALTODAY'))
totalWaiting += 1
totalToday += 1
set_key(dotenv_path='.env', key_to_set='TOTALWAITING', value_to_set=str(totalWaiting))
set_key(dotenv_path='.env', key_to_set='TOTALTODAY', value_to_set=str(totalToday))

print(get_key(dotenv_path='.env', key_to_get='TOTALWAITING'))
print(get_key(dotenv_path='.env', key_to_get='TOTALTODAY'))

set_key(dotenv_path='.env', key_to_set='TOTALTODAY', value_to_set='0')
#env_var = os.environ
#os.environ
#os.environ['TOTALWAITING'] = '2'
#print(os.environ['TOTALWAITING'])
#print("User's Environment variable:")
#pprint.pprint(dict(env_var), width = 1)

""" config = dotenv_values('.env')
set_key(dotenv_path='.env', key_to_set='TOTALWAITING', value_to_set=str(totalWaiting))
set_key(dotenv_path='.env', key_to_set='TOTALTODAY', value_to_set=str(totalToday))
get_key(dotenv_path='.env', key_to_set='TOTALWAITING')
get_key(dotenv_path='.env', key_to_set='TOTALTODAY')
print(config)
 """