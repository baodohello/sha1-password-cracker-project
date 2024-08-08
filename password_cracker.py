import hashlib

def crack_sha1_hash(hash, use_salts=False):
    # Load the top 10,000 passwords
    with open('top-10000-passwords.txt', 'r') as file:
        passwords = file.read().splitlines()

    # Load salts if needed
    if use_salts:
        with open('known-salts.txt', 'r') as file:
            salts = file.read().splitlines()
    else:
        salts = ['']  # Use an empty string as a "no salt" option

    # Check each password (with or without salts)
    for password in passwords:
        for salt in salts:
            # Create hash with no salt, prepended salt, and appended salt
            for salted_password in [password, salt + password, password + salt]:
                hashed_password = hashlib.sha1(salted_password.encode()).hexdigest()
                if hashed_password == hash:
                    return password

    # If no match is found
    return "PASSWORD NOT IN DATABASE"
