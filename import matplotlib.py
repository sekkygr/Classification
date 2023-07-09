import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

fig, ax = plt.subplots(figsize=(12, 12))

# Add rectangles for the main categories
satisfied_effort = Rectangle((0.5, 0.5), 0.5, 0.5, facecolor='lightblue', alpha=0.1)
satisfied_no_effort = Rectangle((0.5, 0.75), 0.5, 0.5, facecolor='lightgray', alpha=0.1)
unsatisfied_effort = Rectangle((0.5, 0), 0.5, 0.5, facecolor='purple', alpha=0.1)
unsatisfied_no_effort = Rectangle((0, 0), 0.5, 0.5, facecolor='salmon', alpha=0.1)
ax.add_patch(satisfied_effort)
ax.add_patch(satisfied_no_effort)
ax.add_patch(unsatisfied_effort)
ax.add_patch(unsatisfied_no_effort)

# Add text for the main categories
ax.text(0.75, 0.75, "Satisfied with Genetic Condition\nand Making Effort", ha='center', va='center', fontsize=12, alpha=0.8)
ax.text(0.25, 0.75, "Satisfied with Genetic Condition\nand Not Making Effort", ha='center', va='center', fontsize=12, alpha=0.8)
ax.text(0.75, 0.25, "Unsatisfied but Making Effort", ha='center', va='center', fontsize=12, alpha=0.8)
ax.text(0.25, 0.25, "Unsatisfied and Not Making Effort", ha='center', va='center', fontsize=12, alpha=0.8)

# Add rectangles for the subcategories
honest_resignation = Rectangle((0, 0), 0.25, 0.25, facecolor='salmon', alpha=0.3)
honest_acceptance = Rectangle((0.25, 0.25), 0.25, 0.25, facecolor='salmon', alpha=0.4)
deceptive_failed_not_selfaware_lighter = Rectangle((0.5, 0), 0.25, 0.25, facecolor='plum', alpha=0.1)
deceptive_successful_not_selfaware_lighter = Rectangle((0.75, 0.25), 0.25, 0.25, facecolor='plum', alpha=0.5)
deceptive_failed_selfaware_lighter = Rectangle((0.75, 0), 0.25, 0.25, facecolor='plum', alpha=0.2)
deceptive_successful_selfaware_lighter = Rectangle((0.5, 0.25), 0.25, 0.25, facecolor='plum', alpha=0.3)

honest2 = Rectangle((0.75, 0.75), 0.25, 0.25, facecolor='lightblue', alpha=0.9)
deceptive_successful_selfaware2 = Rectangle((0.5, 0.5), 0.25, 0.25, facecolor='lightblue', alpha=0.1)
deceptive_successful_not_selfaware2 = Rectangle((0.5, 0.75), 0.25, 0.25, facecolor='lightblue', alpha=0.6)

honest_no_effort1 = Rectangle((0.25, 0.75), 0.25, 0.25, facecolor='lightgray', alpha=0.9)
honest_no_effort2 = Rectangle((0, 0.5), 0.25, 0.25, facecolor='lightgray', alpha=0.1)
honest_no_effort3 = Rectangle((0, 0.75), 0.25, 0.25, facecolor='lightgray', alpha=0.6)

ax.add_patch(honest_acceptance)
ax.add_patch(honest_resignation)
ax.add_patch(deceptive_failed_not_selfaware_lighter)
ax.add_patch(deceptive_successful_not_selfaware_lighter)
ax.add_patch(deceptive_failed_selfaware_lighter)
ax.add_patch(deceptive_successful_selfaware_lighter)
ax.add_patch(honest2)
ax.add_patch(deceptive_successful_selfaware2)
ax.add_patch(deceptive_successful_not_selfaware2)

ax.add_patch(honest_no_effort1)
ax.add_patch(honest_no_effort2)
ax.add_patch(honest_no_effort3)

# Add text for the subcategories
ax.text(0.125, 0.125, "Honest Gesture\n(Resignation)", ha='center', va='center', fontsize=10)
ax.text(0.375, 0.375, "Honest Gesture\n(Acceptance)", ha='center', va='center', fontsize=10)
ax.text(0.625, 0.125, "Deceptive Gesture\nFailed\n(Not Self-aware)", ha='center', va='center', fontsize=10)
ax.text(0.875, 0.375, "Deceptive Gesture\nSuccessful\n(Not Self-aware)", ha='center', va='center', fontsize=10)
ax.text(0.875, 0.125, "Deceptive Gesture\nFailed\n(Self-aware)", ha='center', va='center', fontsize=10)
ax.text(0.625, 0.375, "Deceptive Gesture\nSuccessful\n(Self-aware)", ha='center', va='center', fontsize=10)
ax.text(0.875, 0.875, "Honest Gesture", ha='center', va='center', fontsize=10)
ax.text(0.625, 0.625, "Deceptive Gesture\nSuccessful\n(Self-aware)", ha='center', va='center', fontsize=10)
ax.text(0.625, 0.875, "Deceptive Gesture\nSuccessful\n(Not Self-aware)", ha='center', va='center', fontsize=10)

ax.text(0.375, 0.875, "Honest Gesture", ha='center', va='center', fontsize=10)
ax.text(0.125, 0.625, "Deceptive Gesture\nSuccessful\n(Self-aware)", ha='center', va='center', fontsize=10)
ax.text(0.125, 0.875, "Deceptive Gesture\nSuccessful\n(Not Self-aware)", ha='center', va='center', fontsize=10)

# Set the limits and labels
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

plt.title("Classification of People Based on Deceptive Gestures and Satisfaction with Genetic Condition")
plt.show()