import fake_useragent as fua
import random as rd
import string
import requests
import imaplib
import re


class CHartbeachBot:
    # API key for proxies
    API_KEY = ""

    # Set proxy for http and https requests
    proxies = {
        "http": f'http://scraperapi:{API_KEY}@proxy-server.scraperapi.com:8001',
        "https": f'http://scraperapi:{API_KEY}@proxy-server.scraperapi.com:8001'
    }
    # Array of names, pretty lazy, but does the job
    firstName = ["Noah", "Sem", "Liam", "Lucas", "Daan", "Finn", "Levi", "Luuk", "Mees", "James", "Milan", "Sam",
                 "Noud", "Benjamin", "Luca", "Bram", "Mason", "Max", "Thomas", "Adam", "Hugo", "Jesse", "Boaz",
                 "Olivier", "Teun", "Julian", "Lars", "Thijs", "Gijs", "Siem", "Guus", "Mats", "Zayn", "Otis", "Jens",
                 "Jack", "Floris", "Ties", "Vince", "Joep", "David", "Jan", "Stijn", "Sven", "Dex", "Jurre", "Morris",
                 "Ruben", "Owen", "Jayden", "Mohammed", "Tobias", "Moos", "Tim", "Abel", "Tijn", "Jace", "Willem",
                 "Oliver", "Cas", "Fedde", "Ryan", "Jaxx", "Roan", "Quinn", "Xavi", "Daniël", "Dani", "Alexander",
                 "Dean", "Jake", "Sepp", "Ezra", "Mohamed", "Pepijn", "Tom", "Jason", "Aiden", "Jax", "Nathan", "Kai",
                 "Rayan", "Pim", "Oscar", "Elias", "Melle", "Boris", "Mick", "Senn", "Samuel", "Lenn", "Hidde", "Amir",
                 "Johannes", "Job", "Joshua", "Niek", "Tygo", "Stef", "Arthur", "Casper", "Ravi", "Nolan", "Aaron",
                 "Stan", "Lev", "Duuk", "Logan", "Jip", "Sep", "Jonah", "Julius", "Elijah", "Joris", "Pieter", "Sef",
                 "Loek", "Kyan", "Daley", "Leon", "Odin", "Jim", "Lewis", "Felix", "Bas", "Thijmen", "Simon", "Jacob",
                 "Alex", "Hamza", "Joël", "Milo", "Omar", "Hendrik", "Joah", "Jelle", "Jelte", "Raf", "Seth", "Ali",
                 "Robin", "Cornelis", "Vigo", "Daniel", "Jonas", "Mace", "Dylan", "Ibrahim", "Bodhi", "Kay", "Lex",
                 "Aron", "Jonathan", "Louis", "Mateo", "Joey", "Jules", "Mika", "Imran", "Jasper", "Joas", "Lukas",
                 "Victor", "Luc", "Mayson", "Fabian", "Yusuf", "Filip", "Koen", "Ayden", "Kaj", "Philip", "Rens",
                 "Charlie", "Kees", "Luka", "Ted", "Damian", "Bobby", "Evan", "Kian", "Wout", "Faas", "Gerrit", "Miran",
                 "Riley", "Ayoub", "Raff", "Vic", "Valentijn", "Vik", "Emir", "Jamie", "Muhammed", "Niels", "Timo",
                 "Nick", "Youssef", "Ayaz", "Beau", "Jort", "Leo", "Sil", "Lio", "Micha", "Zayd", "Dirk", "Florian",
                 "Matteo", "Matthijs", "Quinten", "Sten", "Vinz", "Ivan", "Jayson", "Luke", "Laurens", "Frenkie",
                 "Ömer", "Ben", "Ilyas", "Sami", "Chris", "Lux", "Rafael", "Twan", "Scott", "Lasse", "Maxim", "Fynn",
                 "Jaivey", "Joe", "Justin", "Eden", "Jop", "Manuel", "Matthias", "Olaf", "Eli", "Fender", "Jordan",
                 "Jayce", "Mike", "Lou", "Tyler", "Aras", "Ian", "Nouri", "Jay", "Mohammad", "Pelle", "Harvey", "Ahmed",
                 "Bob", "Huub", "Ilay", "Jari", "Marinus", "Lowen", "Novan", "Amin", "Berend", "Louay", "Miles",
                 "Miraç", "Muhammad", "Noël", "Riv", "Xem", "Bilal", "Bodi", "Dante", "Julan", "Rowan", "Eymen", "Naud",
                 "Ole", "Rein", "Zion", "Boet", "Brent", "Liyam", "Riff", "Levy", "Noan", "Revi", "Zakaria", "Maurits",
                 "Musa", "Seff", "Tijs", "Ivar", "Rijk", "Safouan", "Vincent", "Fos", "Juda", "Kasper", "Thom", "Ace",
                 "Jona", "Lorenzo", "Mark", "Senna", "Abe", "Flynn", "Jesper", "Jorn", "Marcel", "Sev", "Stenn",
                 "Wouter", "Antoni", "Dorian", "Gabriel", "Ilias", "Kyano", "Maas", "Mehmet", "Mert", "Younes", "Alan",
                 "Bowie", "Dez", "Ivo", "Mels", "Oskar", "Viggo", "Yves", "Dax", "Kerem", "Lennon", "Michael",
                 "Mustafa", "Toon", "Collin", "Ethan", "Lyam", "Moussa", "Reza", "Seb", "Thijn", "Tijmen", "Boas",
                 "Colin", "Kaan", "Loet", "Mahir", "Ralph", "Tuur", "Tycho", "Arie", "Christiaan", "Donny", "Joes",
                 "Leonardo", "Quin", "Sebastiaan", "Shane", "Tommy", "Xavier", "Aleksander", "Dave", "Douwe", "Ferre",
                 "Mirza", "Reda", "Silvan", "Toby", "Yahya", "Bruno", "Damin", "Dexx", "Dion", "Jakub", "Klaas", "Len",
                 "Sebastian", "Sverre", "Wolf", "Isaac", "Jur", "Maarten", "Manu", "Seppe", "Siebe", "Tibbe", "Yasin",
                 "Anouar", "Benja", "Davey", "Foss", "George", "Jimmy", "Johan", "Kevin", "Nox", "Otto", "Isaiah",
                 "Kjeld", "Lennox", "Malik", "Merijn", "Rafaël", "Rico", "Stefan", "Thiago", "Joost", "Josh", "Teije",
                 "Tristan", "Mads", "Marcus", "Mart", "Robert", "Bjorn", "Cody", "Gabriël", "Jackson", "Marijn", "Mink",
                 "Tieme", "Axel", "Davi", "Idris", "Jeppe", "Junayd", "Menno", "Mylo", "Peter", "Rick", "Yassin",
                 "Yassir", "Albert", "Brenn", "Jacobus", "Kacper", "Kick", "Mex", "Midas", "Naoufal", "Sebas",
                 "Zakariya", "Zeyd", "Ahmad", "Anas", "Denzel", "Matthew", "Mik", "Mitch", "Nils", "Danilo", "Duco",
                 "Finley", "Gideon", "Maximilian", "Safouane", "Senne", "Tymon", "William", "Yiğit", "Zef", "Adriaan",
                 "Björn", "Bryan", "Lenny", "Milano", "Erik", "Frederik", "Giel", "Javi", "Jaxon", "Leendert", "Louie",
                 "Martin", "Natan", "Sieb", "Viktor", "Aidan", "Bart", "Christian", "Davy", "Devin", "Enzo", "Evert",
                 "Ismail", "Jad", "Jeremiah", "Joa", "John", "Luciano", "Sander", "Brandon", "Chase", "Diego", "Dries",
                 "Elia", "Finnley", "Jimi", "Karam", "Nassim", "Ralf", "Wessel", "Yanis", "Alparslan", "Bradley",
                 "Deniz", "Dennis", "Ediz", "Kane", "Miguel", "Samuël", "Silas", "Tobi", "Tobin", "Yannick", "Bruce",
                 "Ensar", "Jeremy", "Kobe", "Leonard", "Maher", "Manoah", "Milas", "Nicolas", "Quint", "Tije",
                 "Valentino", "Wes", "Yassine", "Abdullah", "Daaf", "Gerard", "Giovanni", "Jaimy", "Jakob", "Jorrit",
                 "Kuzey", "Kylian", "Mathijs", "Nino", "Oliwier", "Sjors", "Storm", "Alec", "Anton", "Arda", "Ayman",
                 "Damon", "Diaz", "Enes", "Glenn", "Jairo", "Jaylen", "Jayvano", "Juul", "Keano", "Matz", "Rayen",
                 "River", "Roef", "Teunis", "Umut", "Youp", "Badr", "Benyamin", "Djayden", "Fer", "Gianni", "Hein",
                 "Isa", "Jaïr", "Jordy", "Kayden", "Kenzo", "Levin", "Mathias", "Micah", "Nigel", "Siep", "Ziggy",
                 "Ziyad"]
    lastName = ["de Jong", "Jansen", "de Vries", "van den Berg", "van Dijk", "Bakker", "Janssen", "Visser", "Smit",
                "Meijer", "de Boer", "Mulder", "de Groot", "Bos", "Vos", "Peters", "Hendriks", "van Leeuwen", "Dekker",
                "Brouwer", "de Wit", "Dijkstra", "Smits", "de Graaf", "van der Meer", "Kok", "Jacobs", "van der Linden",
                "de Haan", "Vermeulen", "van den Heuvel", "van der Veen", "van den Broek", "de Bruin", "Schouten",
                "de Bruijn", "van Beek", "van der Heijden", "Willems", "van Vliet", "Hoekstra", "Maas", "Verhoeven",
                "Koster", "van Dam", "Prins", "Blom", "Huisman", "Peeters", "de Jonge", "Kuipers", "van der Wal",
                "van Veen", "Post", "Kuiper", "Veenstra", "Kramer", "van den Brink", "Scholten", "van Wijk", "Postma",
                "Martens", "Vink", "de Ruiter", "Timmermans", "Groen", "van de Ven", "Gerritsen", "Jonker", "van Loon",
                "Boer", "Willemsen", "Smeets", "de Lange", "Bosch", "de Vos", "van Dongen", "Schipper", "de Koning",
                "Koning", "van der Laan", "Driessen", "van Doorn", "Hermans", "Evers", "van der Velden",
                "van den Bosch", "van der Meulen", "Hofman", "Bosman", "Wolters", "Sanders", "Mol", "van der Horst",
                "Kuijpers", "Molenaar", "de Leeuw", "Verbeek", "Stam", "Kroon", "Groot", "Timmer", "de Rooij",
                "Wouters", "Groeneveld", "Roos", "de Haas", "Schaap", "van Rijn", "Bosma", "Pronk", "Koopman", "Vonk",
                "Verhagen", "Snijders", "Dekkers", "van Es", "Zijlstra", "van der Velde", "Versteeg", "Boon", "Klein",
                "Stevens", "Simons", "Gerrits", "Aarts", "Otten", "Muller", "Verweij", "Bouwman", "van Schaik", "Blok",
                "de Jager", "Klaassen", "Jager", "Rutten", "Damen", "van Eijk", "van der Heide", "Cornelissen",
                "van Rooij", "Vermeer", "Geurts", "Bouman", "Franken", "Teunissen", "Faber", "Lammers", "Boersma",
                "Arts", "Roelofs", "Buijs", "van Os", "Joosten", "Venema", "Verhoef", "Thijssen", "Derksen",
                "Schuurman", "Visscher", "Derks", "Goossens", "van den Akker", "Wiersma", "Kersten", "Timmerman",
                "van der Werf", "Baas", "Baars", "Brouwers", "van Essen", "van Lieshout", "Kamphuis", "van der Plas",
                "van Driel", "Wessels", "van Rooijen", "Hoek", "van Rossum", "Zwart", "van Eck", "van Gils", "Bouma",
                "Arends", "van der Ploeg", "van der Steen", "van den Bos", "Vissers", "Bijl", "Hartman", "Knol",
                "Tromp", "van Dalen", "Terpstra", "de Ruijter", "Hoogendoorn", "Rietveld", "den Hartog", "van Berkel",
                "Kooistra", "Feenstra", "Boonstra", "van de Pol", "Schut", "den Boer", "Pieters", "Koopmans", "Keizer",
                "Konings", "Stolk", "van Zanten", "de Ridder", "Smulders", "Veldman", "Schepers", "van Vugt", "Brink",
                "Boers", "van der Molen", "Vis", "de Waal", "de Jongh", "van der Zee", "Nieuwenhuis", "Albers", "Brand",
                "Brinkman", "Klomp", "van Duijn", "Keijzer", "van Velzen", "van der Sluis", "van der Veer",
                "van Egmond", "Schreurs", "Kooijman", "van Hoof", "Verheijen", "Lamers", "Kool", "Nijenhuis",
                "Heemskerk", "Heijnen", "Willemse", "Nijland", "Brands", "Reinders", "Leenders", "de Visser", "Berends",
                "Meijers", "de Kok", "Bergsma", "van Gelder", "Veldhuis", "Ruiter", "Schippers", "Drost", "Theunissen",
                "Swinkels", "Wijnen", "Schutte", "Verschoor", "van der Linde", "Hoogeveen", "Wagenaar",
                "van der Hoeven", "de Wilde", "Kooij", "Fransen", "Manders", "Klaver", "Mulders", "Jonkers",
                "van Kessel", "van Putten", "Steenbergen", "de Graaff", "Nijhuis", "Bongers", "van Kempen",
                "Bouwmeester", "Pol", "Franssen", "van der Burg", "Lemmens", "Geerts", "den Ouden", "Koops",
                "van Mourik", "Yilmaz", "de Winter", "van Ginkel", "Beckers", "van Wijngaarden", "Veerman", "Versluis",
                "Schreuder", "Bruinsma", "van Bergen", "Hendriksen", "Drenth", "de Laat", "van der Woude",
                "Groenendijk", "Schoenmakers", "Verheij", "Houben", "Valk", "van Kampen", "Swart", "Boom", "Boot",
                "van Houten", "van de Wetering", "Borst", "Coenen", "van de Laar", "Lubbers", "Timmers", "Kamp",
                "Nguyen", "Westra", "Weijers", "Oomen", "Kroes", "van der Meij", "de Beer", "Burger", "van der Ven",
                "van Hees", "van der Poel", "Berendsen", "Hiemstra", "Bruins", "van Laar", "van Alphen", "van Erp",
                "van der Kolk", "Scheffer", "Blaauw", "van der Lee", "van Keulen", "van den Bergh", "van Schijndel",
                "van den Hoek", "Moonen", "Raaijmakers", "Jaspers", "van Esch", "Engels", "Harmsen", "Dam",
                "van der Pol", "Vogel", "Schellekens", "de Waard", "Burgers", "Dijk", "Hoogland", "Beekman", "Dijkman",
                "Verkerk", "van Boxtel", "van der Hoek", "van Pelt", "Zonneveld", "Veldhuizen", "van Tol",
                "van Rijswijk", "van Oosten", "Elzinga", "Snijder", "Janssens", "Snel", "Huizinga", "Staal", "Hagen",
                "van den Hurk", "Heijmans", "Janse", "Pot", "Roest", "Koot", "van Tilburg", "van der Vliet",
                "van der Voort", "Koelewijn", "Douma", "van Soest", "van der Meijden", "Nijhof", "Smith", "Wolf", "Tol",
                "Kerkhof", "Kloosterman", "Kusters", "Bartels", "van Mierlo", "Schenk", "de Klerk", "van Engelen",
                "van Hal", "Stoop", "Donkers", "de Man", "Brugman", "de Kort", "Berkhout", "Vogels", "Klok", "Snoek",
                "Hermsen", "Smid", "Alberts", "Westerhof", "Troost", "Engelen", "den Hollander", "Witteveen", "Jonkman",
                "Veen", "van de Wiel", "Zuidema", "Koolen", "Scholte", "Pennings", "van der Weide", "van den Boogaard",
                "Bijlsma", "ter Horst", "Schmidt", "Zwaan", "Slot", "van Gestel", "de Bie", "Kremer", "van de Kamp",
                "Cox", "van der Aa", "Akkerman", "Ros", "van Delft", "Donker", "Hamers", "Schilder", "Reitsma",
                "de Weerd", "Meijerink", "van Kooten", "Hartog", "Wijnands", "Reijnders", "van de Sande", "Mertens",
                "de Zeeuw", "Hollander", "Buis", "van Santen", "Hendrikx", "Linders", "Bruin", "Kuijper", "Moes",
                "Claassen", "Miedema", "van Schie", "van Uden", "de Heer", "van der Valk", "Goedhart", "van den Boom",
                "Hol", "Schuurmans", "ter Haar", "Nijboer", "van der Graaf", "Mensink", "Polman", "Witte", "Bax",
                "van Deursen", "Stegeman", "Coolen", "Spaans", "Buitenhuis", "van Ingen", "van Buuren", "Wever",
                "van Hout", "Weber", "van Gent", "Schmitz", "van de Velde", "Verburg", "Hulshof", "Ooms",
                "van der Zwan", "van der Spek", "Verheul", "de Geus", "van Oorschot", "Bol", "van der Beek",
                "van Lierop", "Veltman", "Krijgsman", "ten Have", "Schrijver", "van Beers", "Beumer", "van Ham",
                "van der Zanden", "Cremers", "Nijman", "van der Vegt", "Haan", "Nijssen", "Kaya", "Verstappen", "Braam",
                "Vrolijk", "van Bruggen", "van Maanen", "Ali", "Hendrix", "Wassink", "Martina", "Oudshoorn", "Pater",
                "van Gool", "Laan", "van Dooren", "Krol", "van der Werff", "van Ooijen", "van Riel", "van Oosterhout",
                "Bal", "Romijn", "Verschuren", "Bloem", "Rademaker", "Veldkamp", "van Zon", "van den Oever",
                "van Haren", "Mohamed", "van Gemert", "Jans", "van Helden", "Gielen", "Klijn", "Kroeze", "van Kleef",
                "Ahmed", "van der Heiden", "Habets", "Hof", "Nijkamp", "Zwiers", "van 't Hof", "Lam", "Gorter",
                "Kanters", "van Noort", "Bekkers", "Bergman", "Scheepers", "van Bommel", "Dijkhuizen", "van der Putten",
                "Bleeker", "Pijnenburg", "Griffioen", "Krijnen", "Broeders", "de Goede", "van der Ham", "Hofstede",
                "de Roos", "de Roo", "van der Kooij", "de Zwart", "de Nijs", "Mooij", "van Aalst", "van Laarhoven",
                "Nauta", "Winter", "Broekhuizen", "Tijssen", "van Oort", "Bekker", "Rovers", "Hoogenboom", "Schot",
                "van Wanrooij", "Koenen", "Winters", "Hopman", "van Tongeren", "Prinsen", "Bouwhuis", "van de Graaf",
                "Luijten", "Maassen", "van Haaren", "Bogers", "de Wolf", "Yildiz", "van Iersel", "Ras", "Broers",
                "Nelissen", "van Hoorn", "Bron", "Verbruggen", "Spijker", "Landman", "Maat", "van Galen", "Kessels",
                "van Aken", "Wolfs", "Akkermans", "Heeren", "Oosting", "Verstegen", "van Ommen", "van Diepen",
                "Pieterse", "Sterk", "de Rijk", "Rozema", "Groenewegen", "Verboom", "Baan", "Jongsma", "Nieuwenhuizen"]
    
    # Initialize bot
    def __init__(self, referralCode):
        self.referralCode = referralCode
        self.headers = {
            'authority': 'app.viral-loops.com',
            'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
            'x-ucid': 'w9K5IiOEF5qogWn96ZGqYx54OyE',
            'sec-ch-ua-mobile': '?0',
            'content-type': 'application/json',
            'user-agent': f'{fua.UserAgent().chrome}',
            'sec-ch-ua-platform': '"Windows"',
            'accept': '*/*',
            'origin': 'https://www.hartbeach.nl',
            'sec-fetch-site': 'cross-site',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://www.hartbeach.nl/',
            'accept-language': 'nl-NL,nl;q=0.9',
        }
        self.data = ""
        self.response = None

    def change_useragent(self):
        """
        Change user-agent to make it look like different devices send the requests
        :return:
        """
        self.headers['user-agent'] = fua.UserAgent().chrome

    def create_data(self):
        """
        Create randomized post data to send to giveaway
        :return: Nothing
        """
        # Choose names
        random_firstname = rd.choice(self.firstName)
        random_lastname = rd.choice(self.lastName)

        random_add = ""

        # Decide to use first letter or full first name by chance
        random_number1 = rd.randint(1, 4)
        if random_number1 == 1:
            email_firstname = random_firstname[0]
        else:
            email_firstname = random_firstname

        # Choose to add number after by chance
        random_number2 = rd.randint(1, 10)

        # Random number added
        if random_number2 < 4:
            random_add = random_add.join(rd.choice(string.digits[1:]) for i in range(random_number2))
        # Add birthdate after first+last name
        elif random_number2 == 4:
            rd1 = rd.randint(1, 30)
            if rd1 < 10:
                random_add += '0'
            random_add += str(rd1)
            rd2 = rd.randint(1, 12)
            if rd2 < 10:
                random_add += '0'
            random_add += str(rd2)
        # Add birthyear
        elif random_number2 == 5:
            random_add += str(rd.randint(1970, 2003))

        else:
            pass
        # Create string of post request to server
        self.data = f'{{"params":{{"event":"registration","user":{{"firstname":"{random_firstname}","lastname":"{random_lastname}",' \
                    f'"email":"{email_firstname.lower() + random_lastname.replace(" ", "").lower() + random_add + "@privatehosting.email" }","extraData":{{}},"consents":{{"1120":false,"1121":false,"1122":false,' \
                    f'"1150":true}}}},"referrer":{{"referralCode":"{self.referralCode}"}},"refSource":"copy","acquiredFrom":"popup"}},' \
                    '"publicToken":"w9K5IiOEF5qogWn96ZGqYx54OyE"} '

    # Send data generated
    def execute_request(self, timeout=3):
        """
        Send post request to the host of the giveaway
        :param timeout: Seconds to wait for response before raising exception
        :return: Nothing
        """
        # Try except to not wait for response
        try:
            self.response = requests.post('https://app.viral-loops.com/api/v2/events', headers=self.headers,
                                          data=self.data,
                                          proxies=self.proxies, verify=False, timeout=timeout)
        except requests.exceptions.ReadTimeout:
            pass

    def create_make_request(self):
        """
        Function to scramble user agent, create new post data and send the request
        :return: Nothing
        """
        self.change_useragent()
        self.create_data()
        self.execute_request()


if __name__ == "__main__":
    # Put in code, doesnt work now
    bot = CHartbeachBot("")
    bot.change_useragent()
    bot.create_data()
    print(bot.data)
    bot.execute_request()
