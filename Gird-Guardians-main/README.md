# Grid Guardians

A software-based intelligent power grid monitoring system with ML inference, visualization dashboard, and simulated transformer data.

## Project Structure

```
backend/
  flask-api/         # Python Flask API for ML inference
    model/           # Model training and preprocessing scripts
  node-api/          # Node.js (TypeScript) Express API
frontend/            # React dashboard
  src/components/    # Visualization components
  public/            # Static files
  ...
database/            # MongoDB initialization scripts
```

## Setup Instructions

### Backend (Flask API)
1. `cd backend/flask-api`
2. `pip install -r requirements.txt`
3. Train your model: `python model/train.py`
4. Run the Flask server: `python app.py`

### Backend (Node API)
1. `cd backend/node-api`
2. `npm install`
3. `npm start`

### Frontend (React)
1. `cd frontend`
2. `npm install`
3. `npm start`

### Database (MongoDB)
- Use `mongo < database/mongo-init.js` to initialize collections.

---

- ML: Random Forest, Python, Flask
- API Gateway: Node.js (TypeScript), Express
- Frontend: React
- Database: MongoDB
