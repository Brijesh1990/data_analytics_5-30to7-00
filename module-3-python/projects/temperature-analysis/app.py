import matplotlib.pyplot as plt
import pandas as pd


temperatures = [22, 24, 21, 23, 25, 27, 26, 24, 28, 30, 29, 27, 26, 31, 28]
days = list(range(1, len(temperatures) + 1))

temperature_data = pd.DataFrame({"Day": days, "Temperature": temperatures})

maximum_temperature = temperature_data["Temperature"].max()
minimum_temperature = temperature_data["Temperature"].min()
average_temperature = temperature_data["Temperature"].mean()
above_average_days = temperature_data[
	temperature_data["Temperature"] > average_temperature
]

print(temperature_data.to_string(index=False))
print(f"\nMaximum temperature: {maximum_temperature} °C")
print(f"Minimum temperature: {minimum_temperature} °C")
print(f"Average temperature: {average_temperature:.2f} °C")
print("Days above average:")
print(above_average_days.to_string(index=False))

plt.plot(temperature_data["Day"], temperature_data["Temperature"], marker="o")

plt.title("Daily Temperatures Over 15 Days")
plt.xlabel("Day")
plt.ylabel("Temperature (°C)")
plt.xticks(days)
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("temperature_variation.png", dpi=150)
plt.show()
