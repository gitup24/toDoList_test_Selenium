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
driver = webdriver.Chrome(service=service, options=options)

#initialiser le nabigateur
#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#Ouvrir la page de connection
driver.get("https://dwils.github.io/todolist/")

#Test ajout d'1 tache. On vise cete elt. Inspecter et le viser. id="taskInput" assez precie. Puis version avec XPath. Ajouterune tache ... est le placeHolder
#task_input contiendra. On fait que selectionner l elt
#task_input = driver.find_element(By.ID, "taskInput")
task_input = driver.find_element(By.XPATH, "//input[@placeholder='Ajouter une tâche...']")
#essais :on luis envoie qq chose. On le simule pr pouvoir l'automatiser
task_input.send_keys("Tache 1")
#pour mieux voire
time.sleep(2)

#chercher bouton ds inspecteur
add_task_btn=driver.find_element(By.ID, "addTaskButton")
#action clic
add_task_btn.click()
#et verivier si elet contient ce qu on souhaite


#ajout 1 time sleep de 2 sec pr lui laisser realiser
time.sleep(2)

#verifier/asertion. Identifier le groupe Tache 1 ajoutéé. li >span qui l identifiera "Tache 1". Ms il n a pas d'ID. DOnc on utilise XPATH
#si X <span>, utiliser find by elt. Donne tt les ocurentce ds 1 tableau
#task_text = driver.find_element(By.XPATH, "//span")
task_spans = driver.find_element(By.XPATH, "//span")
#strip retire les espaces inutiles avant et apres de chq chaine pr pas casser la comparaison
task_texts = [task.text.strip for task in task_spans]

#assert any()
assert "Tache 1" in task_texts, f"Erreur : 'Tache 1' non trouvée.. Liste actuelle : {task_texts}"
#N affiche pas de msg donc test reussi
driver.quit()
#executer : python test-us1.pt