import matplotlib.pyplot as plt

def process_data(file_name, user_name):
    try:
        data = []
        with open(file_name, 'r') as file:
            header = file.readline().strip().split(',')
            name_index = header.index('Name')
            time_index = header.index('Time')

            for line in file:
                fields = line.strip().split(',')
                if fields[name_index] == user_name:
                    data.append(float(fields[time_index]))

        if not data:
            print(f"No data found")
            return

        min_time = min(data)
        max_time = max(data)
        avg_time = sum(data) / len(data)

        print(f"Min Time: {min_time:.3f} seconds")
        print(f"Max Time: {max_time:.3f} seconds")
        print(f"Average Time: {avg_time:.3f} seconds")

        plt.figure(figsize=(8, 5))
        plt.plot(data, marker='o', linestyle='-', color='b', label=user_name)
        plt.title(f"Data for {user_name}")
        plt.xlabel("Instance")
        plt.ylabel("Time (Seconds)")
        plt.legend()
        plt.grid(True)
        plt.show()

    except FileNotFoundError:
        print(f"{file_name} not found.")
    except ValueError:
        print("Couldn't read {file_name")

file_name = "/workspaces/Level-1-Project/Data.csv"
user_name = input("Enter name to search for: ")
process_data(file_name, user_name)
