from selenium import webdriver 
from time import sleep
import random
class Bot:

    def __init__(self):
        """
        Initialize the Bot instance.
        
        This method creates a list of first names, last names, and emails.
        It also sets the bot's zip code and subject.
        Then it calls the go method below in a loop to run the bot 100 times with different names and emails.
        """
        firsts = [
            "John", "Emma", "Michael", "Olivia", "William", "Ava", "James", "Sophia", "Oliver", "Isabella",
            "Benjamin", "Mia", "Elijah", "Charlotte", "Lucas", "Amelia", "Henry", "Harper", "Alexander", "Evelyn",
            "Sebastian", "Abigail", "Jack", "Emily", "Jackson", "Liam", "Aiden", "Grace", "Owen", "Madison",
            "Samuel", "Avery", "Joseph", "Scarlett", "Matthew", "Hannah", "David", "Lily", "Carter", "Ella",
            "Daniel", "Chloe", "Wyatt", "Victoria", "Luke", "Aria", "Gabriel", "Sofia", "Anthony", "Nora",
            "Dylan", "Zoe", "Leo", "Eleanor", "Jaxon", "Penelope", "Christopher", "Mila", "Liam", "Addison",
            "Isaac", "Aubrey", "Lincoln", "Luna", "Andrew", "Stella", "Joshua", "Natalie", "Caleb", "Leah",
            "Nathan", "Hazel", "Ryan", "Violet", "Eli", "Aurora", "Nicholas", "Savannah", "Hunter", "Aaliyah",
            "Christian", "Camila", "Mason", "Ariana", "Julian", "Claire", "Landon", "Skylar", "Aaron", "Bella",
            "Connor", "Lucy", "Ezra", "Anna", "Charles", "Katherine", "Evan", "Maya", "Tyler", "Mila"
        ]
        lasts = [
            "Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor",
            "Anderson", "Thomas", "Jackson", "White", "Harris", "Martin", "Thompson", "Garcia", "Martinez", "Robinson",
            "Clark", "Rodriguez", "Lewis", "Lee", "Walker", "Hall", "Allen", "Young", "Hernandez", "King",
            "Wright", "Lopez", "Hill", "Scott", "Green", "Adams", "Baker", "Gonzalez", "Nelson", "Carter",
            "Mitchell", "Perez", "Roberts", "Turner", "Phillips", "Campbell", "Parker", "Evans", "Edwards", "Collins",
            "Stewart", "Sanchez", "Morris", "Rogers", "Reed", "Cook", "Morgan", "Bell", "Murphy", "Bailey",
            "Rivera", "Cooper", "Richardson", "Cox", "Howard", "Ward", "Torres", "Peterson", "Gray", "Ramirez",
            "James", "Watson", "Brooks", "Kelly", "Sanders", "Price", "Bennett", "Wood", "Barnes", "Ross",
            "Henderson", "Coleman", "Jenkins", "Perry", "Powell", "Long", "Patterson", "Hughes", "Flores", "Washington",
            "Butler", "Simmons", "Foster", "Gonzales", "Bryant", "Alexander", "Russell", "Griffin", "Diaz", "Hayes"
        ]
        emails = [
            "@gamil.com", "@yahoo.com", "@hotmail.com"
        ]
        self.zip = "90001"
        self.subject = 'CEASEFIRE'
        messages = [
            "It's infuriating that the USA remains the sole obstacle to a UN-backed ceasefire in Gaza, consistently voting against it.",
            "The UN's paralysis in the face of Gaza's crisis is a direct result of the USA's stubborn 'no' votes for a ceasefire.",
            "The international community's frustration grows as the USA, with its single vote, obstructs every attempt at a UN-backed ceasefire in Gaza.",
            "The USA's solitary 'no' vote for a Gaza ceasefire in the UN is a betrayal of the organization's founding principles.",
            "The UN's inability to act decisively in Gaza is a direct consequence of the USA's obstructive voting stance on ceasefires.",
            "The USA's continuous 'no' votes for a ceasefire in the UN have rendered the organization impotent in the face of the Gaza crisis.",
            "As children continue to die in Gaza, the world looks helplessly at the UN, paralyzed by the USA's repeated vetoes against a ceasefire.",
            "The USA's relentless opposition to UN-backed ceasefires in Gaza exposes a broken system that undermines global peace efforts.",
            "The UN's credibility is shattered as the USA, with a single vote, holds the organization hostage, preventing a Gaza ceasefire.",
            "The international community's frustration peaks as the USA's solitary vote obstructs progress toward a UN-backed ceasefire in Gaza.",
            "Gaza's tragedy deepens as the USA, wielding its single vote, repeatedly undermines global efforts for a UN-backed ceasefire.",
            "The UN's failure to address the Gaza crisis lies squarely in the USA's repeated 'no' votes for a ceasefire, rendering other voices futile.",
            "The world watches in disbelief as the USA's lone 'no' vote obstructs the path to a UN-backed ceasefire in Gaza.",
            "The USA's dominance in UN voting prevents the organization from fulfilling its mandate in ending the bloodshed in Gaza.",
            "The international community's exasperation grows as the USA, with a single vote, hinders every attempt at a UN-backed ceasefire in Gaza.",
            "Gaza's suffering persists as the USA's 'no' votes in the UN sabotage the prospects of a desperately needed ceasefire.",
            "The USA's solitary opposition to UN-backed ceasefires in Gaza highlights the urgent need for reform within the organization.",
            "As the world pleads for a Gaza ceasefire, the USA's lone 'no' vote in the UN stands as a formidable barrier to peace.",
            "The USA's repeated vetoes against a UN-backed ceasefire in Gaza echo the cries of innocent lives lost in the conflict.",
            "Gaza's anguish deepens with each 'no' vote from the USA, rendering the UN incapable of delivering a ceasefire.",
            "The international community grapples with frustration as the USA's solitary vote thwarts every attempt at a UN-backed ceasefire in Gaza.",
            "The UN's impotence in Gaza is a direct consequence of the USA's unwavering opposition to a ceasefire.",
            "The USA's consistent 'no' votes in the UN make a mockery of the organization's commitment to global peace, especially in Gaza.",
            "Gaza's plight worsens as the USA, with a single vote, repeatedly obstructs the UN's path to a ceasefire.",
            "The international community's outcry for a Gaza ceasefire is drowned out by the USA's resolute opposition within the UN.",
            "The USA's unilateral 'no' votes for a Gaza ceasefire expose the inadequacies of the current UN decision-making process.",
            "Gaza's tragedy is compounded by the USA's repeated 'no' votes in the UN, preventing the organization from fulfilling its peacekeeping role.",
            "The world grapples with frustration as the USA, with a single vote, thwarts every attempt at a UN-backed ceasefire in Gaza.",
            "The USA's consistent 'no' votes for a Gaza ceasefire in the UN perpetuate the suffering of innocent lives caught in the conflict.",
            "As the world pleads for a Gaza ceasefire, the USA's solitary 'no' vote in the UN becomes a symbol of international paralysis.",
            "Gaza's suffering is prolonged by the USA's unyielding opposition to UN-backed ceasefires, undermining the organization's credibility.",
            "The international community's patience wears thin as the USA, with its single vote, obstructs every initiative for a Gaza ceasefire.",
            "Gaza's tragedy deepens as the USA, wielding its single vote, repeatedly undermines global efforts for a UN-backed ceasefire.",
            "The USA's relentless opposition to UN-backed ceasefires in Gaza exposes a broken system that undermines global peace efforts.",
            "The UN's credibility is shattered as the USA, with a single vote, holds the organization hostage, preventing a Gaza ceasefire.",
            "The international community's frustration peaks as the USA's solitary vote obstructs progress toward a UN-backed ceasefire in Gaza.",
            "Gaza's suffering persists as the USA's 'no' votes in the UN sabotage the prospects of a desperately needed ceasefire.",
            "The USA's solitary opposition to UN-backed ceasefires in Gaza highlights the urgent need for reform within the organization.",
            "As the world pleads for a Gaza ceasefire, the USA's lone 'no' vote in the UN stands as a formidable barrier to peace.",
            "The USA's repeated vetoes against a UN-backed ceasefire in Gaza echo the cries of innocent lives lost in the conflict.",
            "Gaza's anguish deepens with each 'no' vote from the USA, rendering the UN incapable of delivering a ceasefire.",
            "The international community grapples with frustration as the USA's solitary vote thwarts every attempt at a UN-backed ceasefire in Gaza.",
            "The UN's impotence in Gaza is a direct consequence of the USA's unwavering opposition to a ceasefire.",
            "The USA's consistent 'no' votes in the UN make a mockery of the organization's commitment to global peace, especially in Gaza.",
            "Gaza's plight worsens as the USA, with a single vote, repeatedly obstructs the UN's path to a ceasefire.",
            "The international community's outcry for a Gaza ceasefire is drowned out by the USA's resolute opposition within the UN.",
            "The USA's unilateral 'no' votes for a Gaza ceasefire expose the inadequacies of the current UN decision-making process.",
            "Gaza's tragedy is compounded by the USA's repeated 'no' votes in the UN, preventing the organization from fulfilling its peacekeeping role.",
            "The world grapples with frustration as the USA, with a single vote, thwarts every attempt at a UN-backed ceasefire in Gaza.",
            "The USA's consistent 'no' votes for a Gaza ceasefire in the UN perpetuate the suffering of innocent lives caught in the conflict.",
            "As the world pleads for a Gaza ceasefire, the USA's solitary 'no' vote in the UN becomes a symbol of international paralysis.",
            "Gaza's suffering is prolonged by the USA's unyielding opposition to UN-backed ceasefires, undermining the organization's credibility."
        ]
        self.driver = webdriver.Chrome("/Users/clarafication/Documents/UN BOT/chromedriver")
        
        # this is a loop to run the bot 100 times with different names and emails
        # the random numbers are used to select a randomly from the lists above   
        for x in range(0,100):
            self.first = firsts[random.randint(0,99)]
            self.last = lasts[random.randint(0,99)]
            self.email = firsts[random.randint(0,99)] + lasts[random.randint(0,99)] + emails[random.randint(0,2)]
            self.message = messages[x]
            self.go() # this calls the go method below
        
    
    def go(self):
        """
        Navigate to the USUN mission contact page and fill out the contact form.

        This method uses the Selenium WebDriver to navigate to the USUN mission contact page. 
        It then fills out the form with the bot's first name, last name, email, zip code, subject, and message. 
        It also handles the reCAPTCHA and submits the form.
        Sleep is used to allow the page to load before the bot interacts with it.
        """
        # this navigates to the USUN mission contact page
        self.driver.get("https://usun.usmission.gov/mission/contact-us/") 
        sleep(2)
        # this fills out the form with the bot's first name, last name, email, zip code, subject, and message
        self.driver.find_element_by_name('input_3').send_keys(self.first) 
        self.driver.find_element_by_name('input_4').send_keys(self.last)
        self.driver.find_element_by_name('input_6').send_keys(self.email)
        self.driver.find_element_by_name('input_11').send_keys(self.zip)
        self.driver.find_element_by_name('input_14').send_keys(self.subject)
        self.driver.find_element_by_name('input_15').send_keys(self.message)
        # this handles the reCAPTCHA
        self.driver.switch_to.default_content() 
        sleep(3)
        self.driver.switch_to.frame(self.driver.find_element_by_xpath(".//iframe[@title='reCAPTCHA']"))
        sleep(4)
        self.driver.find_element_by_id("recaptcha-anchor-label").click()
        sleep(3)
        self.driver.switch_to.default_content()
        sleep(5)
        # this submits the form
        self.driver.find_element_by_id("gform_submit_button_1").click()
        print("in")

Bot() # this calls the Bot class above

