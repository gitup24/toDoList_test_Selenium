import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

@pytest.fixture
def setup():
    # Initialiser le navigateur
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    # Ouvrir la page de connexion
    driver.get("https://dwils.github.io/todolist/")
    yield driver
    driver.quit()


# Test: Ajouter une tâche
def test_ajout_tache_valide(setup):
    driver = setup
    # task_input = driver.find_element(By.ID, "taskInput")
    task_input = driver.find_element(By.XPATH, "//input[@placeholder='Ajouter une tâche...']")
    task_input.send_keys("Tache 1")
    time.sleep(2)
    add_task_btn = driver.find_element(By.ID, "addTaskButton")
    add_task_btn.click()
    time.sleep(2)
    task_spans = driver.find_elements(By.XPATH, "//span")
    task_texts = [task.text.strip() for task in task_spans]

    time.sleep(4) #C'est un ajout perso.

    assert "Tache 1" in task_texts, f"Erreur : 'Tache 1' non trouvée. Liste actuelle : {task_texts}"