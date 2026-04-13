import socket
import uvicorn
import sys
import os

# Add backend to path
backend_dir = os.path.join(os.path.dirname(__file__), 'backend')
if backend_dir not in sys.path:
    sys.path.insert(0, backend_dir)

def find_open_port(start_port=8000, max_tries=10):
    for port in range(start_port, start_port + max_tries):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            try:
                sock.bind(("127.0.0.1", port))
                return port
            except OSError:
                continue
    return start_port

if __name__ == "__main__":
    try:
        port = find_open_port(8000)
        if port != 8000:
            print(f"Port 8000 is busy. Starting server on localhost:{port} instead.")
        else:
            print("Starting server on http://127.0.0.1:8000")
        uvicorn.run("backend.main:app", host="127.0.0.1", port=port, reload=True)
    except Exception as e:
        print(f"Error starting server: {e}")
        import traceback
        traceback.print_exc()
