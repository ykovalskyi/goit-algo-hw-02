
import random
import time
from dataclasses import dataclass, field
from datetime import datetime
from itertools import count
from queue import Queue, Empty
 
# Створити чергу заявок (FIFO)
request_queue: Queue = Queue()
 
# Генератор унікальних номерів заявок: 1, 2, 3, ...
_id_counter = count(1)
 
ISSUES = [
    "Не вмикається ноутбук",
    "Заміна екрана смартфона",
    "Налаштування роутера",
    "Встановлення ПЗ",
    "Чистка від пилу",
    "Відновлення даних",
    "Заміна батареї",
]
CLIENTS = ["Олена", "Андрій", "Марія", "Тарас", "Ірина", "Богдан", "Наталія"]
 
 
@dataclass
class Request:
    """Заявка до сервісного центру."""
    request_id: int
    client: str
    issue: str
    created_at: datetime = field(default_factory=datetime.now)
 
    def __str__(self) -> str:
        return (f"Заявка #{self.request_id:04d} | {self.client:<8} | "
                f"{self.issue} | створена {self.created_at:%H:%M:%S}")
 
 
def generate_request() -> Request:
    """Створює нову заявку з унікальним номером і додає її до черги."""
    new_request = Request(
        request_id=next(_id_counter),
        client=random.choice(CLIENTS),
        issue=random.choice(ISSUES),
    )
    request_queue.put(new_request)
    print(f"[+] Надійшла {new_request}. У черзі: {request_queue.qsize()}")
    return new_request
 
 
def process_request() -> None:
    """Видаляє заявку з початку черги та «обробляє» її."""
    try:
        current = request_queue.get_nowait()  # Видалити заявку з черги
    except Empty:
        print("[!] Черга пуста — нових заявок для обробки немає.")
        return
 
    # Обробити заявку (імітація часу роботи майстра)
    try:
        time.sleep(random.uniform(0.2, 0.6))
    except KeyboardInterrupt:
        print(f"\n[x] Обробку заявки #{current.request_id:04d} перервано.")
        request_queue.task_done()
        raise
    print(f"[✓] Оброблено {current}. Залишилось у черзі: {request_queue.qsize()}")
    request_queue.task_done()
 
 
def main() -> None:
    """Головний цикл: працює, доки користувач не натисне Ctrl+C."""
    print("Сервісний центр розпочав роботу. Для виходу натисніть Ctrl+C.\n")
    try:
        while True:
            # Генеруємо від 0 до 2 нових заявок за один цикл,
            # щоб черга то зростала, то спорожнялася
            for _ in range(random.randint(0, 2)):
                generate_request()
 
            process_request()
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n\nРоботу сервісного центру завершено.")
        print(f"Необроблених заявок у черзі: {request_queue.qsize()}")
 
 
if __name__ == "__main__":
    main()