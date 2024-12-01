import psutil
import time


def get_network_usage():
    net_io = psutil.net_io_counters()
    bytes_sent = net_io.bytes_sent
    bytes_recv = net_io.bytes_recv
    return bytes_sent, bytes_recv


def main():
    print("Мониторинг сетевой активности. Нажмите Ctrl+C для выхода.")
    old_sent, old_recv = get_network_usage()

    try:
        while True:
            time.sleep(5)
            new_sent, new_recv = get_network_usage()

            sent_per_sec = (new_sent - old_sent) / 5
            recv_per_sec = (new_recv - old_recv) / 5

            print(f"Отправлено: {sent_per_sec / 1024:.2f} KB/s, Получено: {recv_per_sec / 1024:.2f} KB/s")

            old_sent, old_recv = new_sent, new_recv
    except KeyboardInterrupt:
        print("Мониторинг завершен.")


if __name__ == "__main__":
    main()
