# Cars Dealership - Full-Stack Application Capstone Project

A comprehensive, cloud-native car dealership web portal developed as part of the **IBM Full Stack Software Developer Capstone Project**. This application allows users to browse nationwide car dealership branches, view and filter inventory and reviews, and submit verified customer reviews with integrated AI-based sentiment analysis.

---

## 🚀 Project Overview & Architecture

The solution utilizes a decoupled microservices architecture deployed on **IBM Cloud Code Engine**:

- **Django Application Backend (`server/`)**: Core application framework handling user authentication, session management, car model catalogs (SQLite), and proxying API requests.
- **Dealership & Review Microservice (`Node.js/Express`)**: Express service backed by **MongoDB** for managing dealerships data, reviews database, and geographic filtering.
- **Sentiment Analysis Microservice (`Python/Flask`)**: Natural Language Processing microservice interfacing with IBM Watson NLU / HuggingFace to categorize review text into positive, neutral, or negative sentiments.
- **Frontend SPA (`React`)**: Dynamic client application built with React, Bootstrap, and Axios for a responsive, interactive user experience.
- **DevOps & Cloud Deployment**: Containerized with **Docker**, orchestrated via **Kubernetes**, automated with **GitHub Actions CI/CD**, and hosted on **IBM Cloud Code Engine**.

---

## 🛠️ Tech Stack

- **Backend**: Python 3.10, Django 4.2, Node.js, Express.js, Flask
- **Frontend**: React.js, JavaScript (ES6+), HTML5, CSS3, Bootstrap 5
- **Databases**: SQLite (Django ORM), MongoDB (Mongoose)
- **AI/ML**: Natural Language Sentiment Analysis
- **DevOps & Cloud**: Docker, Kubernetes, GitHub Actions, IBM Cloud Code Engine

---

## 📁 Repository Structure

```text
├── .github/workflows/          # CI/CD GitHub Actions pipelines
├── server/
│   ├── djangoproj/             # Django root configuration and settings
│   ├── djangoapp/              # Application logic, views, models, and API proxy routes
│   │   ├── models.py           # CarMake and CarModel schemas
│   │   ├── views.py            # Authentication, get_dealers, get_reviews, post_review
│   │   ├── urls.py             # URL routing specifications
│   │   └── restapis.py         # HTTP client for Express and Sentiment microservices
│   ├── database/               # Express/MongoDB dealer and review services
│   │   ├── app.js              # Express microservice endpoints
│   │   ├── data/dealers.json   # Seed dealer information
│   │   └── data/reviews.json   # Seed customer reviews
│   └── frontend/
│       ├── src/
│       │   ├── components/     # React modular components (Register, Dealers, Reviews)
│       │   └── App.js          # Client routing
│       └── static/             # Static HTML pages (About.html, Contact.html)
└── README.md
```

---

## 🧑‍💻 Author
- **Ashish Akotkar**
- GitHub: [ashishakotkar24-droid](https://github.com/ashishakotkar24-droid)
