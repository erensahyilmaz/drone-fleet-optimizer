from datetime import time
from typing import Tuple

class Drone:
    def __init__(self,id:int,max_weight:float,battery:int,speed:float,start_pos:Tuple[float,float]):
        self.id=id
        self.max_weight=max_weight
        self.battery=battery
        self.speed=speed
        self.start_pos=start_pos
        #Durum Bilgileri:
        self.current_pos=start_pos
        self.remaining_battery=battery
        self.carrying_weight=0.0
        self.assigned_deliveries=[] #Teslimat ID'leri
    def __repr__(self):
        return f"Drone (id={self.id},battery={self.battery},pos={self.start_pos})"

class DeliveryPoint:
    def __init__(self,id:int,pos:Tuple[float,float],weight:float,priority:int,time_window:Tuple[time,time]):
        self.id=id
        self.pos=pos
        self.weight=weight
        self.priority=priority
        self.time_window=time_window # (start_time, end_time)
    def __repr__(self):
        return f"Delivery(id={self.id}, pos={self.pos}, weight={self.weight}, priority={self.priority})"
        
class NoFlyZone:
    def __init__(self,id:int,coordinates:Tuple[float,float],active_time:Tuple[time,time]):
        self.id=id
        self.coordinates=coordinates  # [(x1, y1), (x2, y2), ...]
        self.active_time=active_time  # (start_time, end_time)
    def __repr__(self):
        return f"NoFlyZone(id={self.id}, active={self.active_time})"
