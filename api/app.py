from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import os

# Initialize FastAPI app
app = FastAPI(
    title="Career Guidance API",
    description="NLP-based API to predict career paths based on user preferences",
    version="2.0.0"
)

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load model - try multiple paths for local vs deployed environments
MODEL_PATHS = [
    "model/career_model.pkl",
    "./model/career_model.pkl",
    "/app/model/career_model.pkl"
]

model_pipeline = None
for path in MODEL_PATHS:
    try:
        if os.path.exists(path):
            model_pipeline = joblib.load(path)
            print(f"✅ Model loaded from {path}")
            break
    except Exception as e:
        print(f"Failed to load from {path}: {e}")

if model_pipeline is None:
    print("⚠️ Warning: Model not loaded. Run training first.")


class UserProfile(BaseModel):
    """Request model with all 4 mandatory parameters"""
    salary_range: str
    time_horizon: str
    risk_appetite: str
    industry: str


@app.get("/")
def health_check():
    """Health check endpoint"""
    return {
        "status": "ok",
        "message": "Career Guidance API v2.0 is running",
        "model_loaded": model_pipeline is not None
    }


@app.post("/predict")
def predict_career(profile: UserProfile):
    """
    Predict top career recommendations based on user profile.
    
    Uses TF-IDF + RandomForest NLP pipeline to analyze combined features
    and return ranked career recommendations with confidence scores.
    """
    if model_pipeline is None:
        raise HTTPException(status_code=500, detail="Model is not loaded. Please train the model first.")
    
    # NLP Preprocessing: Combine features exactly as in training
    combined_features = f"{profile.salary_range} {profile.time_horizon} {profile.risk_appetite} {profile.industry}"
    
    try:
        # Get class probabilities from the trained model
        probabilities = model_pipeline.predict_proba([combined_features])[0]
        classes = model_pipeline.classes_
        
        # Pair classes with their probabilities and sort descending
        career_probs = list(zip(classes, probabilities))
        career_probs.sort(key=lambda x: x[1], reverse=True)
        
        # Get top 5 recommendations with non-zero confidence
        top_careers = []
        for career, prob in career_probs[:5]:
            confidence = round(prob * 100, 1)
            if confidence > 0:  # Only include meaningful recommendations
                top_careers.append({
                    "career": career,
                    "confidence": confidence
                })
        
        return {
            "recommendations": top_careers,
            "input": {
                "salary_range": profile.salary_range,
                "time_horizon": profile.time_horizon,
                "risk_appetite": profile.risk_appetite,
                "industry": profile.industry
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")


# For debugging/running with python app.py directly
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
