import subprocess

# Dossier où se trouvent les fichiers PEM
cert_directory = "C:\\temo\\2023 Certificat\\"

# Chemin d'OpenSSL
openssl_path = "C:\\openssl\\openssl"

# Fichiers nécessaires
root_cert = f'"{cert_directory}root_ca.pem"'
intermediate_cert1 = f'"{cert_directory}intermediate_ca1.pem"'
intermediate_cert2 = f'"{cert_directory}intermediate_ca2.pem"'
end_entity_cert = f'"{cert_directory}cert.pem"'
chain_file = f'"{cert_directory}chain.pem"'

# Fonction pour exécuter les commandes OpenSSL et capturer la sortie
def run_openssl(command):
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
        return result.stdout + result.stderr
    except Exception as e:
        return str(e)

# Commandes OpenSSL pour vérifier les certificats
commands = [
    f'{openssl_path} verify -verbose -CAfile {chain_file} {root_cert}',
    f'{openssl_path} verify -crl_download -crl_check -verbose -CAfile {chain_file} {intermediate_cert1}',
    f'{openssl_path} verify -crl_download -crl_check -verbose -CAfile {chain_file} {intermediate_cert2}',
    f'{openssl_path} verify -crl_download -crl_check -verbose -CAfile {chain_file} {end_entity_cert}'
]

# Fichier pour enregistrer les résultats
output_file = cert_directory + "verification_results.txt"

# Exécuter les commandes et enregistrer les résultats
with open(output_file, "w") as file:
    for cmd in commands:
        file.write(f"Running command: {cmd}\n")
        output = run_openssl(cmd)
        file.write(output)
        file.write("\n" + "="*80 + "\n")

print(f"Les résultats de la vérification sont enregistrés dans {output_file}")
