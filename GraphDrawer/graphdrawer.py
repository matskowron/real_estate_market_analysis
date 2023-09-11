'''
SKOWRON Mateusz | Real estate market analyzer
Github @matskowron 

September 2023
'''

import matplotlib.pyplot as plt
from datetime import datetime

class GraphDrawer:
    def __init__(self, data_frame):
        self.data_frame = data_frame

    def draw_graph(self):
        plt.style.use('Solarize_Light2')
        plt.figure(figsize=(16,9), dpi=300)
        plt.plot(self.data_frame["neighborhood"], self.data_frame["price_per_m2"], 'bo', antialiased=True)
        plt.grid(True)
        plt.autoscale(True)
        plt.xticks(rotation=75)
        plt.xlabel('Neighborhood name', fontsize=12)
        plt.ylabel('Price per m^2 [PLN]', fontsize=12)
        plt.title('Price per m^2 in PLN by neighbourhood', fontsize=15, fontweight='bold')
        plot_name = f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} | Average price per m^2.png'
        plt.savefig(plot_name, bbox_inches='tight')
        return plot_name