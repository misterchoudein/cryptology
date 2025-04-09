import angr
import claripy

# 1. Charger le binaire Retro2
proj = angr.Project("Retro2", auto_load_libs=False)

# 2. Définir la taille du buffer d'entrée
# D'après le désassemblage, 16 octets sont réservés dans main pour stocker le mot de passe.
password_size = 16

# 3. Créer un bitvector symbolique pour représenter l'entrée (le mot de passe)
# Ce bitvector simulera le contenu de l'entrée standard (stdin) lue par scanf
password = claripy.BVS("password", 8 * password_size)

# 4. Créer l'état initial avec le contenu symbolique en stdin.
# full_init_state configure correctement l'environnement de démarrage (argc, argv, stdin, etc.)
state = proj.factory.full_init_state(stdin=password)

# 5. Identifier les adresses de succès et d'échec dans le binaire
# D'après le désassemblage :
# - Le succès semble se produire au bloc à l'adresse 0x40073b (juste avant l'affichage de "Gagn")
# - L'échec est géré par la fonction AfficherPerdu à l'adresse 0x40074c
success_addr = 0x40073b
fail_addr    = 0x40074c

# 6. Créer un SimulationManager pour explorer les chemins d'exécution
simgr = proj.factory.simulation_manager(state)

# 7. Explorer en cherchant à atteindre l'adresse de succès et en évitant l'adresse d'échec
simgr.explore(find=success_addr, avoid=fail_addr)

# 8. Vérifier si un chemin menant au succès a été trouvé
if simgr.found:
    found_state = simgr.found[0]
    # Extraire le contenu concret du bitvector 'password'
    solution = found_state.solver.eval(password, cast_to=bytes)
    # On coupe à la première occurrence d'un octet nul, si présent
    solution_clean = solution.split(b'\x00', 1)[0]
    print("[+] Mot de passe trouvé :", solution_clean.decode('utf-8', errors='replace'))
else:
    print("[-] Aucun chemin menant à l'adresse de succès n'a été trouvé.")
