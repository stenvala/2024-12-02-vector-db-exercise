import wikipedia
from pathlib import Path

dir = Path(__file__).parent.absolute() / "finnish_cities"
dir.mkdir(parents=True, exist_ok=True)

cities = [
    "Helsinki",
    "Espoo",
    "Vantaa",
    "Porvoo",
    "Hyvinkää",
    "Turku",
    "Salo",
    "Kaarina",
    "Raisio",
    "Pori",
    "Rauma",
    "Huittinen",
    "Tampere",
    "Nokia",
    "Ylöjärvi",
    "Hämeenlinna",
    "Riihimäki",
    "Forssa",
    "Lahti",
    "Heinola",
    "Orimattila",
    "Kotka",
    "Kouvola",
    "Hamina",
    "Lappeenranta",
    "Imatra",
    "Mikkeli",
    "Savonlinna",
    "Pieksämäki",
    "Kuopio",
]


for index, i in enumerate(cities):
    target = dir / f"{i}.txt"
    print(f"Processing {i}: {index+1}/{len(cities)}")
    if target.exists():
        print("File already fetched")
        continue
    try:
        content = wikipedia.summary(f"{i}, Finland")
    except:
        print(f"Failed to get content for {i}")
        continue
    with open(target, "w") as f:
        f.write(content)
