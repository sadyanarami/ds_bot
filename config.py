from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("TOKEN")
X_API_KEY = env.str("X_API_KEY")
