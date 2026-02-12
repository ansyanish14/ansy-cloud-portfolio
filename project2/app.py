from flask import Flask
import boto3

app = Flask(__name__)

# S3 bucket and image details
BUCKET_NAME = 'staticwebsitesfors3'
IMAGE_NAME = 'sample.jpg'

@app.route('/')
def home():
    # Construct the public S3 URL
    image_url = f'https://{BUCKET_NAME}.s3.amazonaws.com/{IMAGE_NAME}'

    # Simple HTML to display the image
    return f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>My Cloud Portfolio</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                text-align: center;
                background-color: #f5f5f5;
                padding: 50px;
            }}
            h1 {{
                color: #2c3e50;
            }}
            img {{
                margin-top: 20px;
                border: 2px solid #2c3e50;
                border-radius: 8px;
            }}
        </style>
    </head>
    <body>
        <h1>Hello Cloud!</h1>
        <p>My first EC2 + S3 app</p>
        <img src="{image_url}" alt="S3 Image" width="400">
    </body>
    </html>
    '''

if __name__ == "__main__":
    # Run the app on all interfaces at port 80
    app.run(host='0.0.0.0', port=80)
