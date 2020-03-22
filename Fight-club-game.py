import random
import time

def hit(chance, power = 1):
    time.sleep(power * 1.5)
    if random.randrange(1,101) < chance:
        return 1
    else:
        return 0

def attack_direction(directions):
    return random.choice(directions)

def attack_power(enemies_power):
    return random.choice(enemies_power)

turns = 1

directions = ["lewo", "prawo"]
enemies_life = {"Człowiek": 1500, "Rycerz": 2000, "Niedźwiedź": 3000, "Smok": 4000, "Czarownik": 2500, "Wilk": 1500}
enemies_damage = {"Człowiek": 100, "Rycerz": 150, "Niedźwiedź": 350, "Smok": 500, "Czarownik": 200, "Wilk": 250}
enemies_chance = {"Człowiek": 40, "Rycerz": 60, "Niedźwiedź": 50, "Smok": 30, "Czarownik": 70, "Wilk": 80}
enemies_power = list(range(1, 4))
life = 2500
weapons = {1: "hammer", 2: "big_sword", 3: "small_sword", 4: "dagger"}
weapons_chance = {"hammer": 20, "big_sword": 40, "small_sword": 65, "dagger": 80}
weapons_damage = {"hammer": 500, "big_sword": 250, "small_sword": 150, "dagger": 100}
weapons_pl = {"hammer": "Młot", "big_sword": "Miecz oburęczny", "small_sword": "Miecz jednoręczny", "dagger": "Sztylet"}
hit_power = {1: "lekki, szybki i precyzyjny atak", 2: "Średnio mocny i średnio celny atak", 3: "mocny, powolny i mało celny atak"}

enemy = random.choice(list(enemies_life.keys()))

print("Idziesz sobie spokojnie laskiem, aż tu nagle wyskakuje", enemy + "!")
print()
time.sleep(1)
enemy_life = enemies_life[enemy]
while life > 0 and enemy_life > 0:
    print("------------------------")
    print(turns, "tura. Twoje życie:", life, ", życie przeciwnika:", enemy_life)
    print()
    # wybór broni przed każdym atakiem
    while True:
        print("Wybierz broń:")
        print("1. Młot - DAMAGE: " + str(weapons_damage["hammer"]) + "HP | CHANCE: " + str(weapons_chance["hammer"]) + "%")
        print("2. Miecz oburęczny - DAMAGE: " + str(weapons_damage["big_sword"]) + "HP | CHANCE: " + str(weapons_chance["big_sword"]) + "%")
        print("3. Miecz jednoręczny - DAMAGE: " + str(weapons_damage["small_sword"]) + "HP | CHANCE: " + str(weapons_chance["small_sword"]) + "%")
        print("4. Sztylet - DAMAGE: " + str(weapons_damage["dagger"]) + "HP | CHANCE: " + str(weapons_chance["dagger"]) + "%")
        try:
            weapon = weapons[int(input())]
        except:
            print("Nieprawidłowy wybór. Spróbuj ponownie")
            print()
            continue

        if weapon in weapons_pl:
            break
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie")
            print()
            continue
    print("Wybrałeś", weapons_pl[weapon])
    print()

    # wybór mocy uderzenia przed każdym atakiem
    while True:
        power = int(input("""Wybierz moc ataku. Im mocniejszy atak, tym jest wolniejszy oraz mniejsza szansa na trafienie
1. Słaby, dokładny
2. Normalny
3. Mocny, niecelny
"""))
        if power in range(1, 4):
            print()
            print("Wybrałeś", hit_power[power])
            break
        else:
            print("Nie ma takiej mocy uderzenia. Spróbuj ponownie")
            print()
            continue
    # przeliczenie uszkodzeń oraz szansy na trafienie na bazie wyboru poziomu power
    weapons_chance_now = {
                    weapon: weapons_chance[weapon] * 2 / power
                    for weapon in weapons_chance
    }
    
    weapons_damage_now = {
                    weapon: weapons_damage[weapon] * power / 2
                    for weapon in weapons_damage
    }

    time.sleep(2)
    print()
    print("Atakujesz...")
    if hit(weapons_chance_now[weapon], power) == 1:
        enemy_life -= weapons_damage_now[weapon]
        if enemy_life < 0:
            enemy_life = 0
        time.sleep(2)
        print("Trafiłeś! Zabrałeś przeciwnikowi", weapons_damage_now[weapon], "punktów! Zostało mu", enemy_life, "życia")
        if enemy_life == 0:
            print("Zwycięstwo! Gratulacje!")
            break
        time.sleep(2)

        # UNIK CIOSU PRZECIWNIKA
        try:
            print()
            print("Teraz " + enemy +" będzie atakował... Szykuj się do szybkiego uniku!" )
            time.sleep(3)
            print()
            start = time.perf_counter()
            direction_evade = directions[int(input("""Atak! Masz tylko 2 sekudny na unik! Wpisz szybko, w którą stronę zrobić unik 
1. W lewo! 
2. W prawo!
"""))-1]
            end = time.perf_counter()
            if end - start > 2:
                direction_evade = attack_direction(directions)
                print("Nie zdążyłeś! Zrobienie uniku zajęło Tobie aż", round(end - start, 2), "sekund. W ostatniej chwili rzucasz się w", direction_evade)
            else:
                print("Szybka decyzja! Rzucenie się w", direction_evade, "zajęło Ci tylko", round(end - start, 2), "sekund")

        except:
            direction_evade = attack_direction(directions)
            print("Nie zdążyłeś! W ostatniej chwili rzucasz się w", direction_evade)

        # PRZECIWNIK ATAKUJE
        attack = attack_direction(directions)
        # PRZELICZENIE USZKODZEŃ I SZANS NA TRAFIENIE NA BAZIE LOSOWANIA MOCY CIOSU
        enemy_power = attack_power(enemies_power)
        time.sleep(2)
        print(enemy, "wybrał", hit_power[enemy_power])
        time.sleep(2)
        enemies_chance_now = {
                        weapon: enemies_chance[weapon] * 2 / enemy_power
                        for weapon in enemies_chance
        }
        
        enemies_damage_now = {
                        weapon: enemies_damage[weapon] * enemy_power / 2
                        for weapon in enemies_damage
        }

        print(enemy, "atakuje...")
        time.sleep(2)
        if hit(enemies_chance_now[enemy]) == 1 and direction_evade != attack:
            life -= enemies_damage_now[enemy]
            if life < 0:
                life = 0
            print("Dostałeś!", enemy, "zaatakował w swoje", attack , ",a Ty rzuciłeś się w swoje", direction_evade,  "i zabrał Tobie", enemies_damage_now[enemy], "punktów. Zostało Ci", life, "życia")
            if life == 0:
                print("Nie żyjesz! Koniec gry")  
                break          
            time.sleep(3)
            print()
            turns += 1
            continue
        else:
            print("Unik!", enemy, "uderzył w swoje", attack, "i udało Ci się zrobić unik w swoje", direction_evade, "! Brawo kolej na Twój atak!")
            time.sleep(3)
            print()
            turns += 1
            continue
    else:
        print("Nie trafiłeś! Zostało mu", enemy_life, "życia")
        time.sleep(2)
        try:
            print()
            print("Teraz " + enemy + " będzie atakował... Szykuj się do szybkiego uniku!" )
            time.sleep(3)
            print()
            start = time.perf_counter()
            direction_evade = directions[int(input("""Atak! Masz tylko 2 sekudny na unik! Wpisz szybko, w którą stronę zrobić unik 
1. W lewo! 
2. W prawo!
"""))-1]
            end = time.perf_counter()
            if end - start > 2:
                direction_evade = attack_direction(directions)
                print("Nie zdążyłeś! Zrobienie uniku zajęło Tobie aż", round(end - start, 2), "sekund. W ostatniej chwili rzucasz się w", direction_evade)
            else:
                print("Szybka decyzja! Rzucenie się w", direction_evade, "zajęło Ci tylko", round(end - start, 2), "sekund")

        except:
            direction_evade = attack_direction(directions)
            print("Nie zdążyłeś! W ostatniej chwili rzucasz się w", direction_evade)

        # PRZECIWNIK ATAKUJE
        attack = attack_direction(directions)
        # PRZELICZENIE USZKODZEŃ I SZANS NA TRAFIENIE NA BAZIE LOSOWANIA MOCY CIOSU
        enemy_power = attack_power(enemies_power)
        time.sleep(2)
        print(enemy, "wybrał", hit_power[enemy_power])
        time.sleep(2)
        enemies_chance_now = {
                        weapon: enemies_chance[weapon] * 2 / enemy_power
                        for weapon in enemies_chance
        }
        
        enemies_damage_now = {
                        weapon: enemies_damage[weapon] * enemy_power / 2
                        for weapon in enemies_damage
        }

        print(enemy, "atakuje...")
        time.sleep(2)
        if hit(enemies_chance_now[enemy]) == 1 and direction_evade != attack:
            life -= enemies_damage_now[enemy]
            if life < 0:
                life = 0
            print("Dostałeś!", enemy, "zaatakował w swoje", attack, ", a Ty rzuciłeś się w swoje", direction_evade,  "i zabrał Tobie", enemies_damage_now[enemy], "punktów. Zostało Ci", life, "życia")
            if life == 0:
                print("Nie żyjesz! Koniec gry")
                break
            time.sleep(3)
            print()
            turns += 1
            continue
        else:
            print("Unik!", enemy, "uderzył w swoje", attack, "i udało Ci się zrobić unik w swoje", direction_evade, "! Brawo kolej na Twój atak!")
            time.sleep(3)
            print()
            turns += 1
            continue