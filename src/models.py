from datetime import time
from typing import Tuple

class Drone:
    def __init__(self,id:int,max_weight:float,battery:int,speed:float,start_pos:Tuple[float,float]):
        self.id=id
        self.max_weight=max_weight
        self.battery = battery      
        self.speed=speed
        self.start_pos=start_pos
        #Durum Bilgileri:
        self.current_pos=start_pos
        self.remaining_battery=battery
        self.carrying_weight=0.0
        self.assigned_deliveries=[] #Teslimat ID'leri
        self.charging = False
        self.charge_time_remaining = 0  # şarjın tamamlanmasına kalan süre 
    def update(self, time_passed: float):
        """
        time_passed: geçen süre (örneğin dakika cinsinden)
        Bu fonksiyon drone durumunu günceller:
        - Eğer şarj oluyorsa, kalan şarj süresini azaltır.
        - Şarj tamamlandıysa, bataryayı full yapar.
        - Uçuyorsa, batarya tüketimini azaltır.
        """

        consumption_rate = 10  # Birim zamanda batarya tüketim oranı 
        threshold = 500        # Batarya kritik eşiği (örn: 500 birim altında şarja gitmeli)

        if self.charging:
            self.charge_time_remaining -= time_passed
            if self.charge_time_remaining <= 0:
                self.charging = False
                self.remaining_battery = self.battery
        else:
            # Uçuş ve batarya tüketimi simülasyonu
            self.remaining_battery -= consumption_rate * time_passed
            if self.remaining_battery < threshold and not self.charging:
                self.go_to_charge()    
    def __repr__(self):
        return (f"Drone(id={self.id}, max_weight={self.max_weight}, battery={self.battery}, speed={self.speed}, "
                f"pos={self.current_pos}, remaining_battery={self.remaining_battery:.1f}, charging={self.charging})")

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
        
