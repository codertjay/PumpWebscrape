from corporation.bot import PetrolPump

try:
    bot = PetrolPump(teardown=True)
    bot.land_first_page()
    bot.get_petrol_pumps()
    bot.get_petrol_pump_descriptions()
    print("Exiting")

except Exception as a:
    print(a)
