from src.utils.data_loader import load_dataset

# Veriyi yükle
drones, deliveries, zones = load_dataset()

# Verileri yazdır
print("Drones:")
for d in drones:
    print(d)

print("\nDeliveries:")
for dp in deliveries:
    print(dp)

print("\nNo-Fly Zones:")
for z in zones:
    print(z)