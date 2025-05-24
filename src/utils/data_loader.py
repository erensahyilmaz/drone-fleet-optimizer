import os
from datetime import time
from src.models import Drone,DeliveryPoint,NoFlyZone


def parse_time(timestr):
    """'HH:MM' biçimindeki string'i time nesnesine çevirir."""
    hour,minute = map(int,timestr.strip().split(":"))
    return time(hour,minute)

def load_dataset(file_path="data/dataset.txt"):
    drones=[]
    deliveries=[]
    no_fly_zones=[]

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"{file_path} bulunamadı")
    section=None
    with open(file_path,"r") as f:
        for line in f:
            line=line.strip()
            if not line or line.startswith("#"):
                continue
            if line=="[DRONES]":
                section="DRONES"
                continue
            elif line=="[DELIVERIES]":
                section="DELIVERIES"
                continue
            elif line=="[NO_FLY_ZONES]":
                section="NO_FLY_ZONES"
                continue
            if section =="DRONES":
                parts=line.split(",")
                d = Drone(
                    id=int(parts[0]),
                    max_weight=float(parts[1]),
                    battery=int(parts[2]),
                    speed=float(parts[3]),
                    start_pos=(int(parts[4]), int(parts[5]))
                )
                drones.append(d)
            elif section == "DELIVERIES":
                parts = line.split(",")
                dp = DeliveryPoint(
                    id=int(parts[0]),
                    pos=(int(parts[1]), int(parts[2])),
                    weight=float(parts[3]),
                    priority=int(parts[4]),
                    time_window=(parse_time(parts[5]), parse_time(parts[6]))
                )
                deliveries.append(dp)

            elif section == "NO_FLY_ZONES":
                parts = line.split(",")
                coord_pairs = parts[1].split(";")
                coords = [(int(x.split(":")[0]), int(x.split(":")[1])) for x in coord_pairs]
                zone = NoFlyZone(
                    id=int(parts[0]),
                    coordinates=coords,
                    active_time=(parse_time(parts[2]), parse_time(parts[3]))
                )
                no_fly_zones.append(zone)
    return drones, deliveries, no_fly_zones

