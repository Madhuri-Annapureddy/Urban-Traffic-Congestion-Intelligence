import matplotlib.pyplot as plt
import seaborn as sns

def plot_hourly_traffic(df):

    plt.figure(figsize=(8,5))
    sns.lineplot(x='hour', y='traffic_volume', data=df)
    plt.title("Traffic Volume vs Hour")
    plt.savefig("outputs/graphs/hourly_traffic.png")


def plot_weather_traffic(df):

    plt.figure(figsize=(8,5))
    sns.boxplot(x='weather_main', y='traffic_volume', data=df)
    plt.title("Traffic vs Weather")
    plt.savefig("outputs/graphs/weather_traffic.png")


def traffic_heatmap(df):

    pivot = df.pivot_table(
        values='traffic_volume',
        index='hour',
        columns='month',
        aggfunc='mean'
    )

    plt.figure(figsize=(10,6))
    sns.heatmap(pivot, cmap="coolwarm")
    plt.title("Traffic Heatmap")
    plt.savefig("outputs/graphs/traffic_heatmap.png")