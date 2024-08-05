services_menu = {
    "Oil change": 35,
    "Tire rotation": 19,
    "Car wash": 7,
    "Car wax": 12
}

# Display the menu
print("Davy's auto shop services")
for service, cost in services_menu.items():
    print(f"{service} -- ${cost}")

# Prompt the user for two services
service1 = input("\nSelect first service:\n")
service2 = input("Select second service:\n")

# Output an invoice for the selected services
print("\nDavy's auto shop invoice\n")

total_cost = 0

# Service 1
if service1 != "-":
    cost1 = services_menu.get(service1, 0)
    print(f"Service 1: {service1}, ${cost1}")
    total_cost += cost1
else:
    print("Service 1: No service")

# Service 2
if service2 != "-":
    cost2 = services_menu.get(service2, 0)
    print(f"Service 2: {service2}, ${cost2}")
    total_cost += cost2
else:
    print("Service 2: No service")

# Display the total cost
print(f"\nTotal: ${total_cost}")


