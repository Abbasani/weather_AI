from flask import Flask, request, jsonify, send_from_directory, send_file
from flask_cors import CORS
from langchain.tools import tool
from langchain.agents import initialize_agent, AgentType
from langchain_groq import ChatGroq
import os
import requests

app = Flask(__name__, static_folder='static', static_url_path='')
CORS(app)  # Enable CORS for all routes

# Environment variables for API keys
WEATHER_API = os.environ.get("WEATHER_API_KEY", "87d43b9ae73a1b83708dbd90e39d270b")
GROQ_API_KEY = os.environ.get("GROQ_API_KEY", "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")

os.environ["GROQ_API_KEY"] = GROQ_API_KEY

@tool
def get_weather(city: str):
    """
    Fetches the current weather for a specified city.
    """
    url = f"https://api.weatherstack.com/current?access_key={WEATHER_API}"
    city_param = {"query": city}

    response = requests.get(url, params=city_param)
    data = response.json()
    
    # Check if the API call was successful and data is available
    if "location" in data and "current" in data:
        zone = data["location"]["timezone_id"]
        time = data['current']['observation_time']
        condition = data["current"]["weather_descriptions"][0]
        temp = data["current"]["temperature"]
        humidity = data["current"]["humidity"]
        wind_speed = data["current"]["wind_speed"]

        return f"The weather In {city_param['query']}, at {time} ({zone}), the weather is {condition} with a temperature of {temp}°C. The humidity is {humidity}% and the wind speed is {wind_speed} km/h."
    else:
        return f"Could not retrieve weather information for {city}."

# Initialize the LLM and agent
llm = ChatGroq(
    model="meta-llama/llama-4-scout-17b-16e-instruct",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

tools = [get_weather]

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    handle_parsing_errors=True
)

@app.route('/')
def serve_frontend():
    return send_file('static/index.html')

@app.route('/<path:path>')
def serve_static_files(path):
    try:
        return send_from_directory('static', path)
    except:
        return send_file('static/index.html')

@app.route('/api/query', methods=['POST'])
def query_agent():
    try:
        data = request.get_json()
        if not data or 'query' not in data:
            return jsonify({"error": "Please provide a 'query' parameter in the request body"}), 400
        
        query = data['query']
        response = agent.invoke(query)
        
        return jsonify({
            "query": query,
            "response": response.get('output', str(response))
        })
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)

