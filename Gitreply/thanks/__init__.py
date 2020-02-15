import logging
from github import Github
import azure.functions as func
import os

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    try:
        req_body = req.get_json()
        action = req_body.get('action')
        username = req_body['issue']['user']['login']
        con = 1
        if(action != "opened"):
            con = -1
    except:
        con = 0
    if (con==1):
        github = Github(os.environ["GITHUB_PAT"])
        repo = github.get_repo("abhishek0220/MSP-Workshop")
        issue = repo.get_issue(number=req_body['issue']['number'])
        issue.create_comment('Thank you @' + username + '  you for submitting this issue. ' +'We will take this on board and get back to you shortly!')
        return func.HttpResponse(f"Comment Published")
    elif(con == -1): 
        return func.HttpResponse(f"Not Opened")
    else:
        return func.HttpResponse(
             "Please pass a valid request body",
             status_code=400
        )
