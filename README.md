# ChatGPT Clone — Full Stack Project

GitHub Repository: https://github.com/Valeron2023/AI-Chat

## Stack
- **Backend:** Python FastAPI
- **Frontend:** React (Vite SPA)
- **Database:** MySQL
- **AI:** OpenAI API (GPT-4o-mini)

## Project Structure
```
Last_Project/
├── Database/
│   └── chatgpt_db.sql
├── Backend/
│   ├── .env                  ← NOT committed to GitHub
│   ├── .gitignore
│   ├── requirements.txt
│   └── src/
│       ├── app.py            ← entry point
│       ├── controllers/
│       │   └── chat_controller.py
│       ├── services/
│       │   └── chat_service.py
│       ├── models/
│       │   └── chat_model.py
│       ├── middleware/
│       │   └── exception_handler.py
│       └── utils/
│           ├── app_config.py
│           └── dal.py
└── Frontend/
    └── src/
        ├── App.jsx
        ├── components/
        │   ├── Navbar.jsx
        │   └── Message.jsx
        └── pages/
            ├── Home.jsx
            └── About.jsx
```

## How to Run

### Database
Import schema into MySQL:
```bash
mysql -u root -p < Database/chatgpt_db.sql
```

### Backend
```bash
cd Backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
# Edit .env — add your OpenAI API key and MySQL password
cd src
python app.py
```
Server runs on http://localhost:4000

### Frontend
```bash
cd Frontend
npm install
npm run dev
```
App runs on http://localhost:5173
