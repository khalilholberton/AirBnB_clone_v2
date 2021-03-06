#!/usr/bin/python3
'''script start flask application to listen
 on 0.0.0.0 port 5000 with variables'''

from flask import render_template
from flask import Flask
from models import State
from models import storage
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list')
def city_by_state():
    '''city by state'''
    st = []
    for key in storage.all(State):
        st.append(storage.all(State)[key])
    return render_template('7-states_list.html', st=st)


@app.teardown_appcontext
def tear_db(self):
    """
    tear_db
    """
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
