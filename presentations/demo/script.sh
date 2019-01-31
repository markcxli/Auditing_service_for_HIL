read -rsp $'\n\n' -n1 key
echo 'curl localhost:8000/list_hil_nodes?nodes=all'
read -rsp $'\n\n' -n1 key
curl localhost:8000/list_hil_nodes?nodes=all
read -rsp $'\n\n' -n1 key

echo 'curl localhost:8000/list_hil_nodes?nodes=free'
read -rsp $'\n\n' -n1 key
curl localhost:8000/list_hil_nodes?nodes=free
read -rsp $'\n\n' -n1 key

echo 'curl localhost:8000/list_hil_projects'
read -rsp $'\n\n' -n1 key
curl localhost:8000/list_hil_projects
read -rsp $'\n\n' -n1 key

echo './switch_auditor_cli.py --help'
read -rsp $'\n\n' -n1 key
./switch_auditor_cli.py --help
read -rsp $'\n\n' -n1 key

echo './switch_auditor_cli.py check-diff node9'
read -rsp $'\n\n' -n1 key
./switch_auditor_cli.py check-diff node9
read -rsp $'\n\n' -n1 key

echo './switch_auditor_cli.py show-diff node7'
read -rsp $'\n\n' -n1 key
./switch_auditor_cli.py show-diff node7
read -rsp $'\n\n' -n1 key


