# Weather AI Agent - Render Deployment Guide

## Overview
This guide will help you deploy your Weather AI Agent to Render, a cloud platform that makes it easy to deploy web applications.

## Prerequisites
- A GitHub account
- A Render account (free tier available)
- Your API keys (Weather API and Groq API)

## Step-by-Step Deployment Instructions

### 1. Prepare Your Repository
1. Create a new repository on GitHub
2. Upload the following files to your repository:
   - `app.py` (Flask application)
   - `requirements.txt` (Python dependencies)
   - `Procfile` (Render deployment configuration)

### 2. Set Up Render Service
1. Go to [render.com](https://render.com) and sign in
2. Click "New +" and select "Web Service"
3. Connect your GitHub repository
4. Configure the service:
   - **Name**: `weather-ai-agent` (or your preferred name)
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python app.py`

### 3. Configure Environment Variables
In the Render dashboard, add the following environment variables:

| Variable Name | Value | Description |
|---------------|-------|-------------|
| `WEATHER_API_KEY` | Your WeatherStack API key | API key for weather data |
| `GROQ_API_KEY` | Your Groq API key | API key for the LLM |
| `PORT` | 5000 | Port number (Render will override this) |

**Important Security Note**: 
- The current code contains hardcoded API keys, which is not secure for production
- Always use environment variables for sensitive information
- Consider rotating your API keys after deployment

### 4. Deploy
1. Click "Create Web Service"
2. Render will automatically build and deploy your application
3. The deployment process typically takes 2-5 minutes
4. Once deployed, you'll receive a public URL (e.g., `https://your-app-name.onrender.com`)

## API Usage

### Health Check
```bash
GET https://your-app-name.onrender.com/health
```

### Query the AI Agent
```bash
POST https://your-app-name.onrender.com/query
Content-Type: application/json

{
  "query": "What's the weather like in New York?"
}
```

### Example Response
```json
{
  "query": "What's the weather like in New York?",
  "response": "The weather In New York, at 14:30 (America/New_York), the weather is Partly cloudy with a temperature of 22°C. The humidity is 65% and the wind speed is 15 km/h."
}
```

## Testing Your Deployment

### Using curl
```bash
# Health check
curl https://your-app-name.onrender.com/health

# Weather query
curl -X POST https://your-app-name.onrender.com/query \
  -H "Content-Type: application/json" \
  -d '{"query": "What is the weather in Lagos and Kano?"}'
```

### Using a web browser
Navigate to `https://your-app-name.onrender.com` to see the welcome message.

## Troubleshooting

### Common Issues
1. **Build Failures**: Check that all dependencies are listed in `requirements.txt`
2. **Runtime Errors**: Check the Render logs for detailed error messages
3. **API Key Issues**: Ensure environment variables are set correctly
4. **Timeout Issues**: The free tier has limitations; consider upgrading for production use

### Monitoring
- Use Render's built-in logging to monitor your application
- Set up health checks to ensure your service stays running
- Monitor API usage to avoid hitting rate limits

## Security Recommendations
1. Use environment variables for all sensitive data
2. Implement rate limiting to prevent abuse
3. Add authentication for production use
4. Regularly rotate API keys
5. Monitor logs for suspicious activity

## Scaling Considerations
- Render's free tier has limitations (750 hours/month)
- For production use, consider upgrading to a paid plan
- Implement caching to reduce API calls
- Add error handling and retry logic for better reliability

## Next Steps
- Add authentication and authorization
- Implement request logging and monitoring
- Add more weather-related tools and capabilities
- Create a frontend interface for easier interaction

