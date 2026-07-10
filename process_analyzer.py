import psutil

def get_top_processes(limit=3):

    processes = []

    for proc in psutil.process_iter(['name']):

        try:
            ram_mb = proc.memory_info().rss / (1024 * 1024)

            processes.append(
                (proc.name(), ram_mb)
            )

        except:
            pass

    processes.sort(
        key=lambda x: x[1],
        reverse=True
    )

    return processes[:limit]