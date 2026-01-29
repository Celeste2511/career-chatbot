import requests
import sys

API_URL = "http://localhost:8000/predict"

def get_user_input():
    print("\n--- Career Guidance Chatbot ---")
    print("Please answer the following questions to get a career recommendation.")
    
    # In a real app, I'd validate these against allowed values, 
    # but for now I'll trust the user or the model's tolerance.
    print("\nSelect Salary Range: [18+ LPA, 12–18 LPA, 6–12 LPA, 3–6 LPA]")
    salary = input("Your Salary Range: ").strip()
    
    print("\nSelect Time Horizon: [Short-term, Medium-term, Long-term]")
    time_horizon = input("Your Time Horizon: ").strip()
    
    print("\nSelect Risk Appetite: [Stable, Moderate, High-growth]")
    risk = input("Your Risk Appetite: ").strip()
    
    return salary, time_horizon, risk

def get_prediction(salary, time_horizon, risk):
    payload = {
        "salary_range": salary,
        "time_horizon": time_horizon,
        "risk_appetite": risk
    }
    
    try:
        response = requests.post(API_URL, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.ConnectionError:
        return {"error": "Could not connect to the API. Is the server running?"}
    except Exception as e:
        return {"error": f"An error occurred: {e}"}

def run_chatbot():
    # Allow running with arguments for automated testing
    if len(sys.argv) == 4:
        salary, time, risk = sys.argv[1], sys.argv[2], sys.argv[3]
        print(f"DEBUG: Using arguments: {salary}, {time}, {risk}")
    else:
        salary, time, risk = get_user_input()
        
    print("\nThinking...")
    result = get_prediction(salary, time, risk)
    
    if "predicted_career" in result:
        print(f"\n>>> Recommended Career Path: {result['predicted_career']}")
    else:
        print(f"\n>>> Error: {result.get('error', 'Unknown error')}")

if __name__ == "__main__":
    run_chatbot()
