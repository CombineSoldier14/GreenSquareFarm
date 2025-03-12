from git import Repo
import uuid
import shutil
import os
import time
import requests
local_dir = "greensquarefarm"
if os.path.isdir("greensquarefarm"):
  shutil.rmtree("greensquarefarm")
  print("deleted")
repo = Repo.clone_from("git@github.com:CombineSoldier14/GreenSquareFarm.git", local_dir)
update_file = "blank.txt"
os.chdir("greensquarefarm")
def webhook(message):
    webhook = "WEBHOOK_HERE"
    useWebhook = (webhook != None)

    if useWebhook:
        requests.post(webhook, {
            "content": "{} :green_square:".format(message)
        })
while True:
  with open(f"{update_file}", "a") as f:
      f.write("\n{}".format(str(uuid.uuid4())))
  repo.index.add("blank.txt")
  repo.index.commit("update the file")
  os.system("git push")
  webhook(message="# New Git Push\n<@951639877768863754>, your no-life shenagans are still working!")
  time.sleep(2880 * 60)

