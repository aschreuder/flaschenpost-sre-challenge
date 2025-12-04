from fastapi import FastAPI, HTTPException
import httpx
import asyncio

app = FastAPI()

API_URL = "https://jsonmock.hackerrank.com/api/movies/search/"

async def get_page(client, substr, page):
    """This block initially handles single page fetches, for cleaner code seperation"""
    try:
        resp = await client.get(f"{API_URL}?Title={substr}&page={page}", timeout=10)
        resp.raise_for_status()
        return resp.json()
    except httpx.HTTPError:
        return None

@app.get("/")
async def health_check():
    """Simple health check endpoint."""
    return {"status": "ok"}


@app.get("/movies")
async def get_movies(substr: str):
    """
    Search movies by title substring and return sorted titles.
    This handles pagination concurrently which greatly improves performance
    """
    if not substr:
        raise HTTPException(400, "Search substring is required")
    
    async with httpx.AsyncClient() as client:
        # Fetch first page to determine total pages
        first_page = await get_page(client, substr, 1)
        if not first_page:
            raise HTTPException(502, "Failed to reach external API")
        
        # Collect titles from first page
        titles = [mov["Title"] for mov in first_page["data"]]
        total_pages = first_page["total_pages"]
        
        # Fetch remaining pages concurrently if there are more
        if total_pages > 1:
            tasks = [get_page(client, substr, p) for p in range(2, total_pages + 1)]
            results = await asyncio.gather(*tasks)
            
            # Add titles from successful page fetches
            for page_data in results:
                if page_data:
                    titles.extend([mov["Title"] for mov in page_data["data"]])
        
        # Return alphabetically sorted titles
        return sorted(titles)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8000)
