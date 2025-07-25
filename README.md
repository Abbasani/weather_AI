# Weather AI Agent

A LangChain-powered AI agent that provides weather information using natural language queries.

## Features
- Natural language weather queries
- Powered by Groq's LLaMA model
- RESTful API interface
- Easy deployment to Render

## Quick Start

### Local Development
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Set environment variables:
   ```bash
   export WEATHER_API_KEY="your_weatherstack_api_key"
   export GROQ_API_KEY="your_groq_api_key"
   ```

3. Run the application:
   ```bash
   python app.py
   ```

### API Endpoints

- `GET /` - Welcome message
- `GET /health` - Health check
- `POST /query` - Query the AI agent

### Example Usage
```bash
curl -X POST http://localhost:5000/query \
  -H "Content-Type: application/json" \
  -d '{"query": "What is the weather like in New York?"}'
```

## Deployment
See `render_deployment_guide.md` for detailed deployment instructions.

## License
MIT License

