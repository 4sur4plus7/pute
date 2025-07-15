import os
import requests
import phonenumbers
from phonenumbers import geocoder, carrier

def clear_screen():
    os.system("clear" if os.name == "posix" else "cls")

def print_banner():
    GREEN = "\033[32m"
    RESET = "\033[0m"
    banner = f"""
{GREEN}██████╗ ██╗   ██╗████████╗████████╗
██╔══██╗██║   ██║╚══██╔══╝╚══██╔══╝
██████╔╝██║   ██║   ██║      ██║   
██╔═══╝ ██║   ██║   ██║      ██║   
██║     ╚██████╔╝   ██║      ██║   
╚═╝      ╚═════╝    ╚═╝      ╚═╝   
{RESET}
"""
    print(banner)

def lookup_ip():
    ip = input("🌐 IP à lookup : ")
    print(f"[~] Lookup IP via ip-api.com pour {ip} ...\n")
    try:
        res = requests.get(f"http://ip-api.com/json/{ip}").json()
        if res['status'] == 'success':
            print(f"IP : {res.get('query')}")
            print(f"Pays : {res.get('country')} ({res.get('countryCode')})")
            print(f"Région : {res.get('regionName')}")
            print(f"Ville : {res.get('city')}")
            print(f"ISP : {res.get('isp')}")
            print(f"Organisation : {res.get('org')}")
            print(f"Latitude : {res.get('lat')}")
            print(f"Longitude : {res.get('lon')}")
            print(f"Fuseau horaire : {res.get('timezone')}")
        else:
            print("Erreur lors de la recherche IP.")
    except Exception as e:
        print(f"Erreur : {e}")
    input("\n[Enter] pour revenir au menu...")

def lookup_discord_id():
    user_id = input("📛 ID Discord à lookup : ")
    print(f"🔍 Lookup Discord ID : {user_id}")
    print("⚠️ Fonction à activer après achat clé API.")
    input("\n[Enter] pour revenir au menu...")

def lookup_email_zehef():
    email = input("📧 Email à lookup (Zehef) : ")
    os.system(f"python3 zehef/zehef.py -e {email}")
    input("\n[Enter] pour revenir au menu...")

def grab_link_modifiable():
    base_link = input("🔗 Lien modifiable (ex: invite, tiktok.com) : ")
    modif = input("✅ Modifications à ajouter (ex: ?user=xyz) : ")
    final_link = f"{base_link}{modif}"
    print(f"➡️ Lien final : {final_link}")
    input("\n[Enter] pour revenir au menu...")

def validate_email_h8mail():
    email = input("📧 Email à valider (H8mail leaks) : ")
    os.system(f"h8mail -t {email}")
    input("\n[Enter] pour revenir au menu...")

def clear_dm():
    token = input("🔑 Token Discord : ")
    print("⛔ Clear DM non implémenté (selfbot).")
    input("\n[Enter] pour revenir au menu...")

def lookup_num():
    num = input("📞 Numéro (avec +indicatif) : ")
    try:
        parsed = phonenumbers.parse(num)
        print(f"✔️ Valide : {phonenumbers.is_valid_number(parsed)}")
        print(f"🌍 Pays : {geocoder.description_for_number(parsed, 'fr')}")
        print(f"📡 Opérateur : {carrier.name_for_number(parsed, 'fr')}")
    except Exception as e:
        print(f"⛔ Erreur : {e}")
    input("\n[Enter] pour revenir au menu...")

def lookup_username_slash():
    username = input("🆔 Username à lookup : ")
    if not username:
        return
    os.system(f"cd slash && python3 slash.py {username}")
    input("\n[Enter] pour revenir au menu...")

def lookup_instagram():
    username = input("📸 Username Instagram : ")
    sessionid = input("🔐 Entre ton sessionid Instagram (voir doc) : ")
    os.system(f"toutatis -u {username} -s {sessionid}")
    input("\n[Enter] pour revenir au menu...")

def lookup_snapchat():
    url = input("👻 URL Snapchat : ")
    if "snapchat.com" in url:
        print("✅ URL valide.")
    else:
        print("⛔ Lien invalide.")
    input("\n[Enter] pour revenir au menu...")

def lookup_tiktok():
    url = input("🎵 URL TikTok : ")
    if "tiktok.com" in url:
        print("✅ URL valide.")
    else:
        print("⛔ Lien invalide.")
    input("\n[Enter] pour revenir au menu...")

def webhook_spammer():
    webhook = input("🔗 URL webhook Discord : ")
    print("⛔ Webhook spammer non implémenté.")
    input("\n[Enter] pour revenir au menu...")

def main():
    while True:
        clear_screen()
        print_banner()
        print("=== MENU pute ===")
        print("1. lookup ip              8. lookup discord")
        print("2. lookup email           9. grab lien modifiable")
        print("3. valide email          10. clear dm")
        print("4. lookup numéro         11. webhook spammer")
        print("5. lookup username")
        print("6. lookup Instagram")
        print("7. lookup Snapchat")
        print("8. lookup TikTok")
        print("0. Quitter")
        choice = input("Ton choix : ")

        if choice == "1":
            lookup_ip()
        elif choice == "2":
            lookup_email_zehef()
        elif choice == "3":
            validate_email_h8mail()
        elif choice == "4":
            lookup_num()
        elif choice == "5":
            lookup_username_slash()
        elif choice == "6":
            lookup_instagram()
        elif choice == "7":
            lookup_snapchat()
        elif choice == "8":
            lookup_tiktok()
        elif choice == "9":
            grab_link_modifiable()
        elif choice == "10":
            clear_dm()
        elif choice == "11":
            webhook_spammer()
        elif choice == "0":
            print("Bye !")
            break
        else:
            print("⛔ Choix invalide.")
            input("\n[Enter] pour réessayer...")

if __name__ == "__main__":
    main()
