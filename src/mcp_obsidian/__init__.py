from . import server

def main():
    app = server.create(json_response=True)
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=9999)

# Optionally expose other important items at package level
__all__ = ['main', 'server']