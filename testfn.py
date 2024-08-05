# Prompt for four weights. Add all weights to a list. Output list.
weights = []
for i in range(1, 5):
    weight = float(input(f"Enter weight {i}:\n"))
    weights.append(weight)
    
print(f"Weights: {weights}")
# Output average of weights.

average_weight = sum(weights) / len(weights)
print(f"\nAverage weight: {average_weight:.2f}")

# Output max weight from list.

max_weight = max(weights)
print(f"Max weight: {max_weight:.2f}")

# Prompt the user for a list index and output that weight in pounds and kilograms.

location = int(input("\nEnter a list location (1 - 4):\n"))
user_weight = weights[location - 1]
user_weight_kg = user_weight / 2.2
print(f"Weight in pounds: {user_weight:.2f}")
print(f"Weight in kilograms: {user_weight_kg:.2f}")

# Sort the list and output it.

sorted_weights = sorted(weights)
print(f"\nSorted list: {sorted_weights}")

print(f'{average_weight:.2f}')
print(f'{max_weight:.2f}')