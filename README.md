## server side
pip install fastapi uvicorn websockets
uvicorn simple_ws_server:app --host 0.0.0.0 --port 8000 

## client side 


python simple_client.py ws://127.0.0.1:8000/ws

