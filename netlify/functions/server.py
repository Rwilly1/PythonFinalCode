from flask import Flask, render_template, send_from_directory, request
import json
import os

app = Flask(__name__)
app.template_folder = os.path.join(os.getcwd(), 'templates')
app.static_folder = os.path.join(os.getcwd(), 'static')

def handler(event, context):
    # Get the path from the event
    path = event.get('path', '/')
    if path == '/':
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'text/html'
            },
            'body': render_template('index.html')
        }
    
    # Handle static files
    if path.startswith('/static/'):
        file_path = path.replace('/static/', '')
        try:
            with open(os.path.join(app.static_folder, file_path), 'rb') as f:
                content = f.read()
                content_type = 'text/css' if path.endswith('.css') else 'application/javascript'
                return {
                    'statusCode': 200,
                    'headers': {
                        'Content-Type': content_type
                    },
                    'body': content.decode('utf-8')
                }
        except:
            return {
                'statusCode': 404,
                'body': 'File not found'
            }
    
    return {
        'statusCode': 404,
        'body': 'Not found'
    }
