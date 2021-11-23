from flask import Flask, render_template
from dotenv import get_key, set_key


env = '.env'

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    """
    Go to localhost:5000 to see a message
    """
    return ('This is a website.', 200, None)


@app.route('/api/unassigned', methods=['POST'])
def get_unassigned():
    totalWaiting = int(get_key(dotenv_path=env, key_to_get='TOTALWAITING'))
    totalToday = int(get_key(dotenv_path=env, key_to_get='TOTALTODAY'))
    totalWaiting += 1
    totalToday += 1
    set_key(dotenv_path=env, key_to_set='TOTALWAITING', value_to_set=str(totalWaiting))
    set_key(dotenv_path=env, key_to_set='TOTALTODAY', value_to_set=str(totalToday))
    print('TotalWaiting: {0}\nTotalToday: {1}'.format(get_key(dotenv_path=env, key_to_get='TOTALWAITING'), get_key(dotenv_path=env, key_to_get='TOTALTODAY')))
    return ("", 200, None)


@app.route('/api/assigned', methods=['POST'])
def get_assigned():
    totalWaiting = int(get_key(dotenv_path=env, key_to_get='TOTALWAITING'))
    totalWaiting -= 1
    if totalWaiting < 0:
        set_key(dotenv_path=env, key_to_set='TOTALWAITING', value_to_set='0')
    else:
        set_key(dotenv_path=env, key_to_set='TOTALWAITING', value_to_set=str(totalWaiting))
    print('TotalWaiting: {0}'.format(get_key(dotenv_path=env, key_to_get='TOTALWAITING')))
    return ("", 200, None)


@app.route('/wallboard')
def hello():
    return render_template('index.html')
    #return f'{get_key(dotenv_path=env, key_to_get="TOTALWAITING")}'



if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)