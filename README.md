# 📝 Resume Upload Web App (AWS + Flask)

This project is a **cloud-based resume uploader** where users can upload PDF resumes via a simple web form. The resumes are stored in **Amazon S3**, and related metadata (name, email, S3 URL, timestamp) is stored in **AWS DynamoDB**. It is built using **Flask** and hosted on an **EC2 (Ubuntu)** instance.

---

## 🚀 Live Demo

> Not deployed publicly. Hosted on EC2 internal IP only.

---

## 👨‍🏫 Built Under Mentorship

This project was developed under the guidance of **Ashutosh Sir** as part of my AWS hands-on learning journey.

---

## 📌 Features

- ✅ Upload PDF resume through web form
- 📁 Resume file is stored in **Amazon S3**
- 🧾 Metadata (name, email, resume URL, timestamp) stored in **DynamoDB**
- 🔐 Admin panel (`/submissions`) shows all submitted resumes
- 💡 Clean, modern UI using HTML & CSS

---

## 🧱 Architecture

  [ User Browser ]
        |
        v
  [ Flask Web App (EC2) ]
        |
        v
[ S3: File Upload ] & [ DynamoDB: Store Metadata ]


---

## 🛠 Tech Stack

| Layer        | Technology         |
|--------------|--------------------|
| Frontend     | HTML, CSS          |
| Backend      | Python Flask       |
| Storage      | Amazon S3          |
| Database     | Amazon DynamoDB    |
| Deployment   | AWS EC2 (Ubuntu)   |
| AWS SDK      | Boto3              |

---

## 🔧 Setup Instructions

### 1. Launch EC2 Instance
- Ubuntu 22.04 LTS
- Allow ports: 22 (SSH), 5000 (Flask), 80 (optional for nginx)

### 2. Install Dependencies

sudo apt update
sudo apt install python3-pip -y
pip3 install flask boto3 werkzeug

### 3.Create S3 Bucket
Go to AWS S3 → Create a bucket (e.g., resumebucket1122)

Unblock public access (optional)

### 4. Create DynamoDB Table
Table name: ResumeSubmissions

Primary key: email (String)

### 5. Project Structure
resume-uploader/
├── app.py
└── upload.html
7. Run Flask App
bash
Copy
Edit
python3 app.py
Access: http://<EC2-public-IP>:5000/

