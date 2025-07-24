from flask import Flask, request
import boto3
from datetime import datetime
from werkzeug.utils import secure_filename

app = Flask(__name__)

# AWS Clients
s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb', region_name='ap-south-1')
table = dynamodb.Table('ResumeSubmissions')    #change your dynamodb name here 

BUCKET_NAME = 'resumebucket1122'               #change your s3 bucket name here 

@app.route('/')
def form():
    return open('upload.html').read()

@app.route('/upload', methods=['POST'])
def upload_resume():
    name = request.form['name']
    email = request.form['email']
    file = request.files['resume']
    
    if file and file.filename.endswith('.pdf'):
        filename = secure_filename(file.filename)
        s3_key = f"resumes/{email}-{datetime.utcnow().timestamp()}.pdf"
        s3.upload_fileobj(file, BUCKET_NAME, s3_key)
        
        file_url = f"https://{BUCKET_NAME}.s3.amazonaws.com/{s3_key}"
        
        table.put_item(Item={
            'email': email,
            'name': name,
            'resume_url': file_url,
            'uploaded_at': datetime.utcnow().isoformat()
        })
        
        return f"<h2>✅ Resume uploaded!</h2><a href='/'>Upload Another</a>"
    
    return "<h2>❌ Invalid file type</h2><a href='/'>Try Again</a>"

@app.route('/submissions')
def list_submissions():
    items = table.scan().get('Items', [])
    html = "<h2>Submitted Resumes:</h2><ul>"
    for item in items:
        html += f"<li>{item['name']} - <a href='{item['resume_url']}'>View Resume</a></li>"
    return html + "</ul>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
