WIDGET_WEIGHT = 75.0
GIZMO_WEIGHT = 112.0

num_widgets = int(input("How many widgets do you want? "))
num_gizmos = int(input("How many gizmos do you want? "))

total_weight = num_widgets * WIDGET_WEIGHT + num_gizmos * GIZMO_WEIGHT

print(f"Total weight is {total_weight}")
