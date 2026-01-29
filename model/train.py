import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import os

def train_model():
    """
    Train an NLP-based career recommendation model.
    Uses TF-IDF vectorization + RandomForest classifier.
    Features: salary_range, time_horizon, risk_appetite, industry (combined as text)
    """
    
    # Load dataset
    data_path = "data/raw_data.csv"
    if not os.path.exists(data_path):
        print(f"❌ Dataset not found at {data_path}")
        print("Run 'python data/generate_data.py' first.")
        return
    
    df = pd.read_csv(data_path)
    print(f"📊 Loaded {len(df)} samples with {df['career'].nunique()} unique careers")
    
    # NLP Preprocessing: Combine all text features into a single string
    # This allows TF-IDF to learn patterns from the combined feature space
    df['combined_features'] = (
        df['salary_range'] + " " + 
        df['time_horizon'] + " " + 
        df['risk_appetite'] + " " +
        df['industry']
    )
    
    X = df['combined_features']
    y = df['career']
    
    # Train-test split with stratification
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    print(f"🔀 Train set: {len(X_train)} | Test set: {len(X_test)}")
    
    # Create NLP Pipeline: TF-IDF Vectorizer -> RandomForest Classifier
    # TF-IDF converts text features into numerical vectors
    # RandomForest learns complex patterns from the vectorized features
    pipeline = Pipeline([
        ('tfidf', TfidfVectorizer(
            ngram_range=(1, 2),  # Use unigrams and bigrams
            max_features=500,    # Limit vocabulary size
            lowercase=True
        )),
        ('clf', RandomForestClassifier(
            n_estimators=200,    # More trees for better accuracy
            max_depth=20,        # Prevent overfitting
            random_state=42,
            n_jobs=-1            # Use all CPU cores
        ))
    ])
    
    # Train the model
    print("\n🚀 Training NLP model...")
    pipeline.fit(X_train, y_train)
    
    # Evaluate on test set
    print("\n📈 Evaluating model...")
    y_pred = pipeline.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"✅ Accuracy: {accuracy * 100:.2f}%")
    
    # Detailed classification report
    print("\n📋 Classification Report (sample):")
    report = classification_report(y_test, y_pred, output_dict=True)
    
    # Show top 10 careers by F1-score
    career_scores = [(k, v['f1-score']) for k, v in report.items() 
                     if isinstance(v, dict) and 'f1-score' in v]
    career_scores.sort(key=lambda x: x[1], reverse=True)
    
    print("\nTop 10 careers by F1-score:")
    for career, f1 in career_scores[:10]:
        print(f"  {career}: {f1:.2f}")
    
    # Save the trained model
    model_path = "model/career_model.pkl"
    os.makedirs("model", exist_ok=True)
    joblib.dump(pipeline, model_path)
    print(f"\n💾 Model saved to {model_path}")
    
    # Test prediction
    print("\n🧪 Test Predictions:")
    test_inputs = [
        "18+ LPA Long-term High-growth Technology",
        "12–18 LPA Medium-term Moderate Finance",
        "6–12 LPA Short-term Stable Healthcare",
        "18+ LPA Long-term Stable Public Sector"
    ]
    
    for input_text in test_inputs:
        probs = pipeline.predict_proba([input_text])[0]
        top_indices = probs.argsort()[-3:][::-1]
        top_careers = [(pipeline.classes_[i], probs[i] * 100) for i in top_indices]
        print(f"\n  Input: '{input_text}'")
        print(f"  Top 3: {', '.join([f'{c} ({p:.1f}%)' for c, p in top_careers])}")

if __name__ == "__main__":
    train_model()
