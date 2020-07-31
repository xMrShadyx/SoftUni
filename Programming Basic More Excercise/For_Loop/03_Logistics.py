amount_of_items = int(input())

total_cargo = 0
bus = 200
truck = 175
train = 120
cargo_bus = 0
cargo_truck = 0
cargo_train = 0
price = 0

for i in range(amount_of_items):
    cargo = int(input())
    total_cargo += cargo
    if cargo <= 3:
        cargo_bus += cargo
    elif 4 <= cargo <= 11:
        cargo_truck += cargo
    elif cargo >= 12:
        cargo_train += cargo

total_cargo_price = (cargo_bus * bus + cargo_truck * truck + cargo_train * train) / total_cargo
avg_bus = cargo_bus / total_cargo * 100
avg_truck = cargo_truck / total_cargo * 100
avg_train = cargo_train / total_cargo * 100
print(f"{total_cargo_price:.2f}")
print(f"{avg_bus:.2f}%")
print(f"{avg_truck:.2f}%")
print(f"{avg_train:.2f}%")
