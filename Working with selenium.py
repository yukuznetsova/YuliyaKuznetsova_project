#!pip install --upgrade selenium
#!pip install --upgrade webdriver_manager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import re
import sqlite3

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://en.wikipedia.org/wiki/Anxiety_disorder")
anxiety_1 = []
anxiety_2 = []
b = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/table/tbody")
for i in range(4, len(b.find_elements(By.TAG_NAME, "tr"))):
    st_1 = driver.find_element(By.XPATH, f"/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/table/tbody/tr[{i}]/th").text
    st_2 = driver.find_element(By.XPATH, f"/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/table/tbody/tr[{i}]/td").text
    st_2 = str(st_2)
    st_2 = re.sub("\\[\d{0,}\\]", '', st_2)
    anxiety_1.append (st_1)
    anxiety_2.append (st_2)
anxiety_df = pd.DataFrame([(anxiety_1, anxiety_2) for anxiety_1, anxiety_2 in zip (anxiety_1, anxiety_2)])
anxiety_df.columns = ['category', 'anxiety']
anxiety_df

driver.get("https://en.wikipedia.org/wiki/Major_depressive_disorder")
depression_1 = []
depression_2 = []
b = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/table/tbody")
for i in range(5, len(b.find_elements(By.TAG_NAME, "tr"))):
    st_1 = driver.find_element(By.XPATH, f"/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/table/tbody/tr[{i}]/th").text
    st_2 = driver.find_element(By.XPATH, f"/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/table/tbody/tr[{i}]/td").text
    st_2 = str(st_2)
    st_2 = re.sub("\\[\d{0,}\\]", '', st_2)
    depression_1.append(st_1)
    depression_2.append(st_2)
depression_df = pd.DataFrame([(depression_1, depression_2) for depression_1, depression_2 in zip (depression_1, depression_2)])
depression_df.columns = ['category', 'depression']
depression_df

driver.get("https://en.wikipedia.org/wiki/Schizophrenia")
schizophrenia_1 = []
schizophrenia_2 = []
b = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/table/tbody")
for i in range(5, len(b.find_elements(By.TAG_NAME, "tr"))):
    st_1 = driver.find_element(By.XPATH, f"/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/table/tbody/tr[{i}]/th").text
    st_2 = driver.find_element(By.XPATH, f"/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/table/tbody/tr[{i}]/td").text
    st_2 = str(st_2)
    st_2 = re.sub("\\[\d{0,}\\]", '', st_2)
    schizophrenia_1.append(st_1)
    schizophrenia_2.append(st_2)
schizophrenia_df = pd.DataFrame([(schizophrenia_1, schizophrenia_2) for schizophrenia_1, schizophrenia_2 in zip (schizophrenia_1, schizophrenia_2)])
schizophrenia_df.columns = ['category', 'schizophrenia']
schizophrenia_df

driver.get("https://en.wikipedia.org/wiki/Bipolar_disorder")
bipolar_1 = []
bipolar_2 = []
b = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/table/tbody")
for i in range(5, len(b.find_elements(By.TAG_NAME, "tr"))):
    st_1 = driver.find_element(By.XPATH, f"/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/table/tbody/tr[{i}]/th").text
    st_2 = driver.find_element(By.XPATH, f"/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/table/tbody/tr[{i}]/td").text
    st_2 = str(st_2)
    st_2 = re.sub("\\[\d{0,}\\]", '', st_2)
    bipolar_1.append (st_1)
    bipolar_2.append (st_2)
bipolar_df = pd.DataFrame([(bipolar_1, bipolar_2) for bipolar_1, bipolar_2 in zip (bipolar_1, bipolar_2)])
bipolar_df.columns = ['category', 'bipolar_disorder']
bipolar_df

driver.get("https://en.wikipedia.org/wiki/Eating_disorder")
eating_1 = []
eating_2 = []
b = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/table/tbody")
for i in range(2, len(b.find_elements(By.TAG_NAME, "tr"))):
    st_1 = driver.find_element(By.XPATH, f"/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/table/tbody/tr[{i}]/th").text
    st_2 = driver.find_element(By.XPATH, f"/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/table/tbody/tr[{i}]/td").text
    st_2 = str(st_2)
    st_2 = re.sub("\\[\d{0,}\\]", '', st_2)
    eating_1.append (st_1)
    eating_2.append (st_2)
eating_df = pd.DataFrame([(eating_1, eating_2) for eating_1, eating_2 in zip (eating_1, eating_2)])
eating_df.columns = ['category', 'eating_disorders']
eating_df

driver.get("https://en.wikipedia.org/wiki/Substance_use_disorder")
drug_1 = []
drug_2 = []
b = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/table/tbody")
for i in range(5, len(b.find_elements(By.TAG_NAME, "tr"))):
    st_1 = driver.find_element(By.XPATH, f"/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/table/tbody/tr[{i}]/th").text
    st_2 = driver.find_element(By.XPATH, f"/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/table/tbody/tr[{i}]/td").text
    st_2 = str(st_2)
    st_2 = re.sub("\\[\d{0,}\\]", '', st_2)
    drug_1.append (st_1)
    drug_2.append (st_2)
drug_df = pd.DataFrame([(drug_1, drug_2) for drug_1, drug_2 in zip (drug_1, drug_2)])
drug_df.columns = ['category', 'drug_use_disorders']
drug_df

conn = sqlite3.connect("database.sqlite")
c = conn.cursor()

anxiety_df.to_sql("info_anxiety", conn)
schizophrenia_df.to_sql("info_schizophrenia", conn)
bipolar_df.to_sql("info_bipolar_disorder", conn)
eating_df.to_sql("info_eating_disorders", conn)
drug_df.to_sql("info_drug_use_disorders", conn)
depression_df.to_sql("info_depression", conn)

c.execute("""
SELECT info_anxiety.*, info_bipolar_disorder.bipolar_disorder
FROM info_anxiety LEFT OUTER JOIN info_bipolar_disorder
ON info_anxiety.category = info_bipolar_disorder.category;
""").fetchall()

an_bip = """SELECT info_anxiety.*, info_bipolar_disorder.bipolar_disorder
FROM info_anxiety LEFT OUTER JOIN info_bipolar_disorder
ON info_anxiety.category = info_bipolar_disorder.category"""
t_an_bip = pd.read_sql(an_bip, conn)

sc_eat = """SELECT info_schizophrenia.*, info_eating_disorders.eating_disorders
FROM info_schizophrenia LEFT OUTER JOIN info_eating_disorders
ON info_schizophrenia.category = info_eating_disorders.category"""
t_sc_eat = pd.read_sql(sc_eat, conn)

t_an_bip.to_sql("an_bip", conn)
t_sc_eat.to_sql("sc_eat", conn)

abse = """SELECT an_bip.*, sc_eat.eating_disorders, sc_eat.schizophrenia
FROM an_bip LEFT OUTER JOIN sc_eat
ON an_bip.category = sc_eat.category"""
t_abse = pd.read_sql(abse, conn)
t_abse = t_abse.drop (t_abse.columns [[0]], axis = 1)

dr_dep = """SELECT info_drug_use_disorders.*, info_depression.depression
FROM info_drug_use_disorders LEFT OUTER JOIN info_depression
ON info_drug_use_disorders.category = info_depression.category"""
t_dr_dep = pd.read_sql(dr_dep, conn)

t_abse.to_sql("abse", conn)
t_dr_dep.to_sql("dr_dep", conn)

all_d = """SELECT abse.*, dr_dep.drug_use_disorders, dr_dep.depression
FROM abse LEFT OUTER JOIN dr_dep
ON abse.category = dr_dep.category"""
t_all_d = pd.read_sql(all_d, conn)
t_all_d = t_all_d.drop (t_all_d.columns [[0]], axis = 1)
t_all_d.set_index(t_all_d.columns [0])

t_all_d.to_csv("All_disorders.csv")
