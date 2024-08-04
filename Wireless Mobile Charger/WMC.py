import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_circuit_diagram():
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # Draw Power Source
    ax.add_patch(patches.Rectangle((0.05, 0.7), 0.1, 0.1, edgecolor='black', facecolor='lightblue'))
    ax.text(0.1, 0.75, 'Prise Murale (AC)', ha='center', va='center', fontsize=12)
    
    # Draw Transformer
    ax.add_patch(patches.Rectangle((0.2, 0.7), 0.1, 0.1, edgecolor='black', facecolor='lightgreen'))
    ax.text(0.25, 0.75, 'Transformateur', ha='center', va='center', fontsize=12)
    
    # Draw Bridge Rectifier
    ax.add_patch(patches.Rectangle((0.35, 0.7), 0.1, 0.1, edgecolor='black', facecolor='lightcoral'))
    ax.text(0.4, 0.75, 'Pont Redresseur', ha='center', va='center', fontsize=12)
    
    # Draw Capacitor
    ax.add_patch(patches.Rectangle((0.50, 0.7), 0.1, 0.1, edgecolor='black', facecolor='lightyellow'))
    ax.text(0.55, 0.75, 'Condensateur', ha='center', va='center', fontsize=12)
    
    # Draw Voltage Regulator
    ax.add_patch(patches.Rectangle((0.65, 0.7), 0.1, 0.1, edgecolor='black', facecolor='lightgrey'))
    ax.text(0.7, 0.75, 'Régulateur de Tension', ha='center', va='center', fontsize=12)
    
    # Draw Charger
    ax.add_patch(patches.Rectangle((0.80, 0.7), 0.1, 0.1, edgecolor='black', facecolor='lightblue'))
    ax.text(0.85, 0.75, 'Chargeur Sans Fil', ha='center', va='center', fontsize=12)
    
    # Draw Connections
    ax.annotate('', xy=(0.15, 0.75), xytext=(0.05, 0.75), arrowprops=dict(arrowstyle='->', color='black'))
    ax.annotate('', xy=(0.20, 0.75), xytext=(0.15, 0.75), arrowprops=dict(arrowstyle='->', color='black'))
    ax.annotate('', xy=(0.30, 0.75), xytext=(0.20, 0.75), arrowprops=dict(arrowstyle='->', color='black'))
    ax.annotate('', xy=(0.45, 0.75), xytext=(0.35, 0.75), arrowprops=dict(arrowstyle='->', color='black'))
    ax.annotate('', xy=(0.60, 0.75), xytext=(0.50, 0.75), arrowprops=dict(arrowstyle='->', color='black'))
    ax.annotate('', xy=(0.75, 0.75), xytext=(0.65, 0.75), arrowprops=dict(arrowstyle='->', color='black'))
    
    # Draw Labels
    ax.text(0.35, 0.65, 'AC', ha='center', va='center', fontsize=10, color='black')
    ax.text(0.50, 0.65, 'DC Pulsée', ha='center', va='center', fontsize=10, color='black')
    ax.text(0.65, 0.65, 'DC Stabilisée', ha='center', va='center', fontsize=10, color='black')
    
    # Draw Title
    plt.title('Diagramme du Circuit Redresseur pour Chargeur de Dentifrice Sans Fil', fontsize=14)
    
    # Set limits and remove axes
    ax.set_xlim(0, 1)
    ax.set_ylim(0.6, 0.9)
    ax.axis('off')

    plt.show()

# Call the function to draw the diagram
draw_circuit_diagram()
