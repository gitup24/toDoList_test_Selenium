
from selenium import webdriver
from selenium.webdriver.common.by import By
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time


#linux
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


driver_location = "/snap/bin/chromium.chromedriver"
options = Options()
service = Service(executable_path=driver_location)

import pytest

#3 ajout anotation. Et importer pytest. Mais per-project virtual environment pas géré de IDEA , seulement pyCharm
@pytest.fixture
#2 creer 1 fct
def setup():
    driver = webdriver.Chrome(service=service, options=options)
    #Ouvrir la page de connection
    driver.get("https://dwils.github.io/todolist/")
    #1remonté. Doit avoir 1 fct englobate
    #4 attendre
    yield driver
    driver.quit()

#ajout tache vide
def test_ajout_tache_vide(setup):
    """Test l'ajout d'une tâche vide et la gestion de l'erreur"""
    driver = setup
    task_input = driver.find_element(By.XPATH, "//input[@placeholder='Ajouter une tâche...']")
    #comme on execute 1! X
    task_input.send_keys("")  # Envoi d'une valeur vide
    add_task_btn = driver.find_element(By.ID, "addTaskButton")
    add_task_btn.click()
    time.sleep(2)  # Attente de l'affichage du message d'erreur

    # Vérification de l'affichage du message d'erreur
    #error msg
    error_message = driver.find_element(By.ID, "errorMessage")  # Adapter l'ID selon ton implémentation
    assert error_message.is_displayed(), "Erreur : aucun message d'erreur affiché après l'ajout d'une tâche vide"