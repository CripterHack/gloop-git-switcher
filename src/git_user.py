import subprocess

def get_current_git_user():
    try:
        name = subprocess.check_output(["git", "config", "--global", "user.name"]).decode().strip()
        email = subprocess.check_output(["git", "config", "--global", "user.email"]).decode().strip()
        return name, email
    except subprocess.CalledProcessError:
        return None, None

def set_git_user(name, email):
    subprocess.run(["git", "config", "--global", "user.name", name])
    subprocess.run(["git", "config", "--global", "user.email", email]) 