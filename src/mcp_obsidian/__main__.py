from . import server
import os

if __name__ == "__main__":
    app = server.create(json_response=True)
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=int(os.getenv("PORT", "9999")))