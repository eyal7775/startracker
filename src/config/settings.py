
class Settings:
    # History
    history_path_folder = "/history_data"

    # ASK Status
    ask_status_user = "session:mdclone.admin"
    ask_status_header = {'user': ask_status_user,}
    ask_status_url = "http://10.0.2.171:7676/api/v1/system-check"

    # Indexer Status
    indexer_status_user = "session:mdclone.admin"
    indexer_status_header = {'user': ask_status_user,}
    indexer_status_url = "http://10.0.2.171:999/system_check"

    # Rancher Status
    rancher_status_token = "token-tr6mc:vlj4sk9zwptxknk4nhkrws4bp22glpt22gs2hvfrt6tqrp5zkbmbsn"
    rancher_ip_address = "devops-rancher.mdclone.com"
    rancher_api_version = "3"
    rancher_cluster_name = "cdp"
    rancher_status_auth = "Bearer " + rancher_status_token
    rancher_status_ver_url = "https://"+rancher_ip_address+"/""v"+rancher_api_version+"/clusters?name="+rancher_cluster_name
    rancher_status_url = "https://"+rancher_ip_address+"/""v"+rancher_api_version+"/clusters/"

    # DLG Status
    dlg_status_user = "session:mdclone.admin"
    dlg_status_header = {'user': dlg_status_user,}
    dlg_status_url = "https://dcbackend.2app.rancher.mdclone.com/health"

    # Mail Gmail
    email_gmail_from = "sariel.sharfi@mdclone.com"
    email_gmail_to = "eyal.naftalovich@mdclone.com"
    email_gmail_wonder = "plisunfeztkkpmwp"