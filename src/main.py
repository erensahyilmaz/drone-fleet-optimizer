from src.utils import data_generator, data_loader

def main():
    # Veri üret
    drones = data_generator.generate_drones(5)
    deliveries = data_generator.generate_deliveries(20)
    zones = data_generator.generate_no_fly_zones(2)

    # Veriyi dosyaya kaydet
    data_generator.save_dataset_to_txt(drones, deliveries, zones)

    print("✅ Veri başarıyla 'data/dataset.txt' dosyasına kaydedildi.")

    # Dosyadan veriyi yükle
    drones_loaded, deliveries_loaded, zones_loaded = data_loader.load_dataset()

    print("✅ Dataset başarıyla yüklendi.")
    print(f"Drone sayısı: {len(drones_loaded)}")
    print(f"Teslimat sayısı: {len(deliveries_loaded)}")
    print(f"No-fly zone sayısı: {len(zones_loaded)}")

    print("Drones:")
    for d in drones:
        print(d)  # __repr__ metodu detaylı yazdıracak

    print("\nDeliveries:")
    for dp in deliveries:
        print(dp)

    print("\nNo-Fly Zones:")
    for zone in zones:
        print(zone)

if __name__ == "__main__":
    main()
