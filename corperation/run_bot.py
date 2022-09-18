from .bot import PetrolPump

try:
    bot = PetrolPump(teardown=True)
    bot.land_first_page()
    bot.template_list()
    print("Exiting")

except Exception as a:
    print(a)