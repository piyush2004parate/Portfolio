import datetime
from flask import Flask, redirect, render_template, request,flash, url_for
from flask_sqlalchemy import SQLAlchemy

local_server= True
app=Flask(__name__)
app.secret_key=b'\xd2k\x96I\xf9)L\xc3W\x17\xd4"' 

app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:@localhost:3307/portfolio'
db = SQLAlchemy(app)

class Test(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(20))
class Project(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    project_name = db.Column(db.String(50))
    category = db.Column(db.String(50))
    client = db.Column(db.String(50))
    project_date = db.Column(db.Date)
    project_url = db.Column(db.String(50))
    description = db.Column(db.String(500))

@app.route('/test')
def test():
    try:
        a=Test.query.all()
        print(a)
        return "Database is Connected"
    except:
        return "Database is not Connected"
@app.route('/starter-page')
def start_page():
    return render_template('starter-page.html')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/project', methods=['POST', 'GET'])
def project():
    if request.method=='POST':
        ID = request.form.get('ID') 
        project_name = request.form.get('project_name')
        category = request.form.get('category')
        client = request.form.get('client')
        project_date = request.form.get('project_date')
        project_url = request.form.get('project_url')
        description = request.form.get('description')
        entry = Project(ID=ID, project_name=project_name, category=category, client=client, project_date=project_date, project_url=project_url, description=description)
        db.session.add(entry)
        db.session.commit()        
        flash('Data Saved, Successfully', 'success')
    return render_template('project.html',)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/service-details')
def service_details():
    return render_template('service-details.html')

@app.route('/portfolio-details')
def portfolio_details():
    return render_template('portfolio-details.html')



if __name__ == '__main__':
    app.run(debug=True, port=8000)