# Docker - Steps to Execute (root):

1. docker-compose up --build

# Manual - Steps to Execute (root):

1. venv\Scripts\activate
2. python BlockhouseCore/manage.py runserver
3. Open a New Terminal (root)
4. cd ./blockhouse-dashboard
5. npm run dev

# Post-Execute Testing Steps:

1. Django API go to http://127.0.0.1:8000/api/candlestick-data/
2. React Application http://localhost:3000/
