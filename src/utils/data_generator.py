import random
from datetime import time
import os

def generate_random_time_window(start_hour_range=(9,12),duration_range=(30,90)):
    start_hour=random.randint(*start_hour_range)
    start_minute=random.randint(0,59)
    start=time(start_hour,start_minute)
    duration_minutes=random.randint(*duration_range)
    end_hour=(start_hour+(start_minute+duration_minutes)//60) %24
    end_minute=(start_minute+duration_minutes)%60
    end=time(end_hour,end_minute)
    return (start,end)
def generate_drones(n):
    drones=[]
    for i in range(n):
        drone={
            "id":i,
            "max_weight":round(random.uniform(2.0,5.0),2),
            "battery":random.randint(5000,10000),
            "speed": round(random.uniform(5.0, 15.0), 2),
            "start_pos": (random.randint(0, 100), random.randint(0, 100))
        }
        drones.append(drone)
    return drones
def generate_deliveries(n):
    deliveries=[]
    for i in range(n):
        delivery={
            "id":i,
            "pos":(random.randint(0,200),random.randint(0,200)),
            "weight": round(random.uniform(0.5,3.0),2),
            "priority":random.randint(1,5),
            "time_window":generate_random_time_window()
        }
        deliveries.append(delivery)
    return deliveries
def generate_no_fly_zones(n):
    zones=[]
    for i in range(n):
        x, y = random.randint(50, 150), random.randint(50, 150)
        zone={
            "id":i,
            "coordinates" : [(x, y), (x+10, y), (x+10, y+10), (x, y+10)],
            "active_time":generate_random_time_window()
        }
        zones.append(zone)
    return zones
def save_dataset_to_txt(drones, deliveries, zones, file_path="data/dataset.txt"):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    with open(file_path, "w") as f:
        f.write("[DRONES]\n")
        for d in drones:
            f.write(f"{d['id']},{d['max_weight']},{d['battery']},{d['speed']},{d['start_pos'][0]},{d['start_pos'][1]}\n")

        f.write("\n[DELIVERIES]\n")
        for dp in deliveries:
            f.write(f"{dp['id']},{dp['pos'][0]},{dp['pos'][1]},{dp['weight']},{dp['priority']},{dp['time_window'][0].strftime('%H:%M')},{dp['time_window'][1].strftime('%H:%M')}\n")
        f.write("\n[NO_FLY_ZONES]\n")
        for z in zones:
            coords_str = ";".join(f"{x}:{y}" for x, y in z['coordinates'])
            f.write(f"{z['id']},{coords_str},{z['active_time'][0].strftime('%H:%M')},{z['active_time'][1].strftime('%H:%M')}\n")


if __name__ == "__main__":
    drones = generate_drones(5)
    deliveries = generate_deliveries(20)
    zones = generate_no_fly_zones(2)

    save_dataset_to_txt(drones, deliveries, zones)
    print("✅ Veri başarıyla 'data/dataset.txt' dosyasına kaydedildi.")