from monitor import get_metrics
from notifier import send_alert
from logger import save_metrics
from process_analyzer import get_top_processes
from health import calculate_health
import time

print("System Guardian Started...")

last_alert = 0
ALERT_COOLDOWN = 120  # 2 minutes

while True:

    metrics = get_metrics()

    save_metrics(metrics)

    health = calculate_health(
        metrics["cpu"],
        metrics["ram"],
        metrics["disk"]
    )

    print(
        f"CPU: {metrics['cpu']}% | "
        f"RAM: {metrics['ram']}% | "
        f"Disk: {metrics['disk']}% | "
        f"Health: {health}/100"
    )

    current_time = time.time()

    # RAM Alert
    if (
        metrics["ram"] > 90
        and current_time - last_alert > ALERT_COOLDOWN
    ):

        top_apps = get_top_processes()

        message = (
            f"RAM Usage: {metrics['ram']}%\n\n"
            f"{top_apps[0][0]} - {top_apps[0][1]:.0f} MB\n"
            f"{top_apps[1][0]} - {top_apps[1][1]:.0f} MB\n"
            f"{top_apps[2][0]} - {top_apps[2][1]:.0f} MB"
        )

        send_alert(
            "⚠ High RAM Usage",
            message
        )

        with open("alerts.log", "a") as f:
            f.write(
                f"{time.ctime()} | RAM Alert | "
                f"RAM={metrics['ram']}%\n"
            )

        last_alert = current_time

    # CPU Alert
    elif (
        metrics["cpu"] > 90
        and current_time - last_alert > ALERT_COOLDOWN
    ):

        top_apps = get_top_processes()

        message = (
            f"CPU Usage: {metrics['cpu']}%\n\n"
            f"{top_apps[0][0]} - {top_apps[0][1]:.0f} MB\n"
            f"{top_apps[1][0]} - {top_apps[1][1]:.0f} MB\n"
            f"{top_apps[2][0]} - {top_apps[2][1]:.0f} MB"
        )

        send_alert(
            "⚠ High CPU Usage",
            message
        )

        with open("alerts.log", "a") as f:
            f.write(
                f"{time.ctime()} | CPU Alert | "
                f"CPU={metrics['cpu']}%\n"
            )

        last_alert = current_time
    if health < 40:
            send_alert(
                "⚠ System Health Critical",
                f"Health Score: {health}/100"
            )
    if metrics["disk"] > 95:
        send_alert(
            "⚠ Disk Almost Full",
            f"Disk Usage: {metrics['disk']}%"
        )

    time.sleep(5)