from app import app
from flask import render_template
from datetime import datetime, timedelta

@app.route('/')
@app.route('/index')
def index():
	d = datetime.utcnow()
	epoch = datetime(1970,1,1)
	t = (d - epoch).total_seconds()
	return render_template('index.html', timestamp = t)
