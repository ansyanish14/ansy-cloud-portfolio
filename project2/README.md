
# Project 2: EC2 + S3 Flask App

## Description
This project demonstrates a simple web application hosted on an AWS EC2 instance that fetches and displays an image stored in an S3 bucket. It showcases foundational cloud skills, including:

- Launching and configuring an EC2 instance
- Installing and running a Python Flask web application
- Integrating AWS S3 to store and serve static content
- Accessing the web app via a public IP

This project highlights practical hands-on experience in cloud infrastructure and web deployment using AWS services.

---

## Implementation Steps
1. Create S3 Bucket

Go to the AWS S3 console and create a new bucket (e.g., staticwebsitesfors3).

Upload your image file (myphoto.jpg) to the bucket.

Make the object publicly accessible by either enabling bucket policy for public read or configuring pre-signed URLs.

(Optional) Take a screenshot of your S3 bucket and uploaded file.

2. Launch EC2 Instance

Navigate to AWS EC2 console → Launch an instance.

Choose Amazon Linux 2023 AMI.

Select instance type (e.g., t2.micro for free tier).

Configure security group:

Allow SSH (port 22) from your IP.

Allow HTTP (port 80) from anywhere (0.0.0.0/0) for public access.

Launch instance and download the key pair (mywebserverkey.pem).

3. Connect to EC2 via SSH
4. chmod 400 mywebserverkey.pem
ssh -i "mywebserverkey.pem" ec2-user@<EC2-Public-IP>
4. Install Python and Required Packages
    sudo yum update -y
    sudo yum install python3 -y
    sudo yum install python3-pip -y
    sudo pip3 install flask boto3
5. Upload Your Flask Application

 Create app.py on EC2 using nano app.py or transfer via scp.
6. Run Flask Application
sudo python3 app.py
Access your app at: http://<EC2-Public-IP> in a browser.

You should see your image loaded from S3.
7. Test and Verify

  Verify Flask server is running and accessible.
  
  Ensure the image from S3 loads correctly.
  
  Take screenshots of:
  
  Running Flask server
  
  Image loaded from S3
  
  EC2 instance details in AWS console
  


