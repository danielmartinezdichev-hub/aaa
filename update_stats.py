import json
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

PLACE_ID = "137253701602745"
ROOT = Path(__file__).resolve().parent

def get_json(url):
    req = urllib.request.Request(url, headers={"User-Agent": "PortMediterraneaStats/1.0"})
    with urllib.request.urlopen(req, timeout=25) as response:
        return json.loads(response.read().decode("utf-8"))

now = datetime.now(timezone.utc).isoformat()
try:
    mapping = get_json(f"https://apis.roblox.com/universes/v1/places/{PLACE_ID}/universe")
    universe_id = mapping["universeId"]
    result = get_json(f"https://games.roblox.com/v1/games?universeIds={universe_id}")
    games = result.get("data", [])
    if not games:
        raise RuntimeError("Roblox no devolvió información para esta experiencia")
    game = games[0]
    stats = {
        "placeId": int(PLACE_ID),
        "universeId": universe_id,
        "name": game.get("name", "PortMediterránea"),
        "playing": game.get("playing", 0),
        "maxPlayers": game.get("maxPlayers", 0),
        "visits": game.get("visits", 0),
        "favoritedCount": game.get("favoritedCount", 0),
        "updated": game.get("updated"),
        "capturedAt": now
    }
    (ROOT / "stats.json").write_text(json.dumps(stats, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    history_path = ROOT / "history.json"
    try:
        history = json.loads(history_path.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError):
        history = []
    history.append({"time": now, "playing": stats["playing"]})
    # Mantener aproximadamente los últimos 30 días si se ejecuta cada 5 minutos.
    history = history[-8640:]
    history_path.write_text(json.dumps(history, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"OK: {stats['name']} — {stats['playing']} jugadores")
except Exception as exc:
    print(f"Error consultando Roblox: {exc}")
    raise
