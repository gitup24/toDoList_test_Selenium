
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



#initialiser le nabigateur
#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


#Test ajout d'1 tache. On vise cete elt. Inspecter et le viser. id="taskInput" assez precie. Puis version avec XPath. Ajouterune tache ... est le placeHolder
#task_input contiendra. On fait que selectionner l elt

#5 def consomme setup
def test_ajout_tache_valide(setup):
    driver = setup
    #task_input = driver.find_element(By.ID, "taskInput")
    #6incrementer
    # task_input = driver.find_element(By.ID, "taskInput")
    task_input = driver.find_element(By.XPATH, "//input[@placeholder='Ajouter une tâche...']")
    #essais :on luis envoie qq chose. On le simule pr pouvoir l'automatiser
    task_input.send_keys("Tache 1")
    #pour mieux voire
    time.sleep(2)
    #chercher bouton ds inspecteur
    add_task_btn = driver.find_element(By.ID, "addTaskButton")
    #action clic
    add_task_btn.click()
    #et verivier si elet contient ce qu on souhaite
    #ajout 1 time sleep de 2 sec pr lui laisser realiser
    time.sleep(2)
    #verifier/asertion. Identifier le groupe Tache 1 ajoutéé. li >span qui l identifiera "Tache 1". Ms il n a pas d'ID. DOnc on utilise XPATH
    #si X <span>, utiliser find by elt. Donne tt les ocurentce ds 1 tableau
    #task_text = driver.find_element(By.XPATH, "//span")
    task_spans = driver.find_elements(By.XPATH, "//span")
    #strip retire les espaces inutiles avant et apres de chq chaine pr pas casser la comparaison
    task_texts = [task.text.strip() for task in task_spans]
    #assert any()
    time.sleep(4) #C'est un ajout perso.
    assert "Tache 1" in task_texts, f"Erreur : 'Tache 1' non trouvée. Liste actuelle : {task_texts}"
    #N affiche pas de msg donc test reussi
    #executer : python test-us1.pt
    #pour pas r ouvrire 1 nv driver et l executer a chq X. On fait 1 setup. Avec pipe tes
    #7 executer avec pytest test-us1...

#Ajout W taches
#def test_ajout_plusieurs_taches(setup):

#    for x in range(5):
#        test_ajout_tache_valide(setup)

def test_ajout_plusieurs_taches(setup):
    driver = setup
    task_input = driver.find_element(By.XPATH, "//input[@placeholder='Ajouter une tâche...']")
    add_task_btn = driver.find_element(By.ID, "addTaskButton")

    tasks_to_add = ["Tache 1", "Tache 2", "Tache 3"]
    for task in tasks_to_add:
        task_input.clear()
        task_input.send_keys(task)
        add_task_btn.click()
        time.sleep(1)

    # Vérification
    #verification
    #+ precis avec 1 ul
    task_spans = driver.find_elements(By.XPATH, "//ul[@id='taskList']/li/span")
    #task_input = driver.find_element(By.XPATH, "//input[@placeholder='Ajouter une tâche...']")
    #prelever les txt ds les span
    task_texts = [task.text.strip() for task in task_spans]
    #les comparer
    #assert task_texts == task_to_add, f"Erreur : 'Tache {task}' non trouvée. Liste actuelle : {task_texts}"

    assert task_texts == tasks_to_add, f"Erreur : les tâches affichées sont incorrectes :  {task_texts}"