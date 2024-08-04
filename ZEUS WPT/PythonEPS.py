import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_wpt_diagram():
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # Draw Power Source
    ax.add_patch(patches.Rectangle((0.1, 0.7), 0.1, 0.1, edgecolor='black', facecolor='lightblue'))
    ax.text(0.15, 0.75, 'Power Source', ha='center', va='center', fontsize=12)
    
    # Draw Transmitter Unit
    ax.add_patch(patches.Rectangle((0.3, 0.6), 0.2, 0.2, edgecolor='black', facecolor='lightgreen'))
    ax.text(0.4, 0.7, 'Transmitter Unit', ha='center', va='center', fontsize=12)
    ax.add_patch(patches.Ellipse((0.4, 0.65), 0.1, 0.05, edgecolor='black', facecolor='white'))
    ax.text(0.4, 0.65, 'Transmitter Coil', ha='center', va='center', fontsize=10)
    ax.add_patch(patches.Rectangle((0.35, 0.55), 0.1, 0.05, edgecolor='black', facecolor='lightgrey'))
    ax.text(0.4, 0.575, 'Driver Circuit', ha='center', va='center', fontsize=10)
    ax.add_patch(patches.Rectangle((0.35, 0.52), 0.1, 0.03, edgecolor='black', facecolor='lightgrey'))
    ax.text(0.4, 0.53, 'Oscillator Circuit', ha='center', va='center', fontsize=10)

    # Draw Receiver Unit
    ax.add_patch(patches.Rectangle((0.6, 0.6), 0.2, 0.2, edgecolor='black', facecolor='lightcoral'))
    ax.text(0.7, 0.7, 'Receiver Unit', ha='center', va='center', fontsize=12)
    ax.add_patch(patches.Ellipse((0.7, 0.65), 0.1, 0.05, edgecolor='black', facecolor='white'))
    ax.text(0.7, 0.65, 'Receiver Coil', ha='center', va='center', fontsize=10)
    ax.add_patch(patches.Rectangle((0.65, 0.55), 0.1, 0.05, edgecolor='black', facecolor='lightgrey'))
    ax.text(0.7, 0.575, 'Rectifier Circuit', ha='center', va='center', fontsize=10)
    ax.add_patch(patches.Rectangle((0.65, 0.52), 0.1, 0.03, edgecolor='black', facecolor='lightgrey'))
    ax.text(0.7, 0.53, 'Regulation Circuit', ha='center', va='center', fontsize=10)

    # Draw Connections
    ax.annotate('', xy=(0.3, 0.7), xytext=(0.2, 0.7), arrowprops=dict(arrowstyle='->', color='black'))
    ax.annotate('', xy=(0.5, 0.7), xytext=(0.3, 0.7), arrowprops=dict(arrowstyle='->', color='black'))
    ax.annotate('', xy=(0.6, 0.7), xytext=(0.5, 0.7), arrowprops=dict(arrowstyle='->', color='black'))

    # Draw Load
    ax.add_patch(patches.Rectangle((0.9, 0.7), 0.1, 0.1, edgecolor='black', facecolor='lightyellow'))
    ax.text(0.95, 0.75, 'Powered Device', ha='center', va='center', fontsize=12)

    # Draw Control and Communication
    ax.add_patch(patches.Rectangle((0.4, 0.85), 0.2, 0.1, edgecolor='black', facecolor='lightgrey'))
    ax.text(0.5, 0.9, 'Control Circuit', ha='center', va='center', fontsize=12)

    # Draw Resonance Components
    ax.add_patch(patches.Rectangle((0.2, 0.4), 0.2, 0.1, edgecolor='black', facecolor='lightblue'))
    ax.text(0.3, 0.45, 'Resonance Components', ha='center', va='center', fontsize=12)

    # Draw Cooling System
    ax.add_patch(patches.Rectangle((0.7, 0.4), 0.2, 0.1, edgecolor='black', facecolor='lightgrey'))
    ax.text(0.8, 0.45, 'Cooling System', ha='center', va='center', fontsize=12)

    # Draw Safety Components
    ax.add_patch(patches.Rectangle((0.2, 0.2), 0.2, 0.1, edgecolor='black', facecolor='lightcoral'))
    ax.text(0.3, 0.25, 'Safety Components', ha='center', va='center', fontsize=12)

    # Draw User Interface
    ax.add_patch(patches.Rectangle((0.9, 0.2), 0.1, 0.1, edgecolor='black', facecolor='lightgreen'))
    ax.text(0.95, 0.25, 'User Interface', ha='center', va='center', fontsize=12)

    # Set limits and remove axes
    ax.set_xlim(0, 1.2)
    ax.set_ylim(0, 1)
    ax.axis('off')

    plt.title('Wireless Power Transfer System Diagram')
    plt.show()

# Call the function to draw the diagram
draw_wpt_diagram()
