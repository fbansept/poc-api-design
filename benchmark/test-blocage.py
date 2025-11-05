import requests
import time
from concurrent.futures import ThreadPoolExecutor

# URL de l'API à tester
API_URL = "http://localhost/api/todo/list"

def send_request(request_number):
    try:
        response = requests.get(API_URL)
        print(f"Requête {request_number}: {response.status_code} - {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Requête {request_number}: Erreur - {e}")

def test_case_ok():
    """Teste 2 requêtes par seconde (cas OK)."""
    print("\n=== Test 1 : Requêtes OK (2/s) ===")
    for i in range(1, 6):
        send_request(i)
        time.sleep(0.5)  # 2 requêtes par seconde

def test_case_queue():
    """Teste la mise en file d'attente (burst)."""
    print("\n=== Test 2 : File d'attente (burst) ===")
    with ThreadPoolExecutor(max_workers=5) as executor:
        for i in range(1, 11):
            executor.submit(send_request, i)
            time.sleep(0.1)  # 10 requêtes en 1 seconde (dépassement)


if __name__ == "__main__":
    print("Démarrage des tests pour la limite de requêtes Nginx...")
    test_case_ok()
    time.sleep(2)  # Pause pour éviter les interférences
    test_case_queue()
