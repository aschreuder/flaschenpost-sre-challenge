## FastAPI Application
The Python script runs a FastAPI server with 2 GET endpoints - `/movies` (which accepts a substring search parameter) and `/` (health check endpoint for testing API connectivity).

### How it works
When the `/movies` endpoint is called with a substring, it queries `https://jsonmock.hackerrank.com/api/movies/search/?Title=substr` and returns sorted movie titles as an array. The script uses `asyncio` for concurrent page fetching to optimize performance.

### Error handling
- Timeout values prevent hanging requests
- `raise HTTPException` catches HTTP errors
- Returns `None` on certain failures to prevent script breakage
- Validates that `substr` is not empty

### Running locally
- `cd FlaskApp`
- `pip install -r requirements.txt`
- `uvicorn app:app --reload` or `python app.py`
- Test the API: `curl "http://localhost:8000/movies?substr=spider"`