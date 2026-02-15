def get_pins(client):
    response = client.get("/api/users/me/pins")
    response.raise_for_status()
    return response.json()

def remove_pin(client):
    response = client.delete("/api/users/me/pin")
    response.raise_for_status()
    return response.json()

def set_pin(client, slug: str):
    payload = {{'slug': slug}}
    response = client.put("/api/users/me/pin", json=payload)
    response.raise_for_status()
    return response.json()
