import langchain
import openai
import os

from dotenv import load_dotenv
load_dotenv()

from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain import ConversationChain
from langchain.chat_models import ChatOpenAI

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
SERP_API_KEY = os.getenv("SERP_API_KEY")

llm = OpenAI(temperature=0.9)


event_context = '''
What is the name of the main event? Boda de Camila y Daniel Who is the host of the main event? Camila y Daniel What are the contact details of the host? Daniel: +525512301882 When does the main event start? 45212.3333333333 When does the main event end? 45046.0833333333 In what city is the main event taking place? Merida, Yucatan If there is one location where the whole event is taking place, what is the location? Merida, Yucatan To what airport or airports should guests arrive? Merida international airport (MID) What are the recommended hotels for the event? Courtyard by Marriott Mérida Downtown Mencionar Boda Camila y Daniel, Code: WDC Toll Free: 1 800 344 0548 Email: hotelesreservaciones@grupopresidente.com www.marriott.com/events/start.mi +52-999-454-3000 Av. Colón 504, Centro, 97000 Mérida, Yuc., Mexico Wayam Mundo Imperial Via Web: Click on ‘’Special Code’’, then ‘’Discount Code’' and type CAMYDAN141023 in order to see the discounted rate for the wedding week. USA: 844 855 9253 Email: reservaciones@mundoimperial.com www.mundoimperial.com/wayam/book/dates-of-stay 800-090-99-00 Av. Colón 508, García Ginerés, 97070 Mérida, Yuc., Mexico Villa Mercedes Merida, Curio Collection by Hilton Código: GRCYD Email: midvm_reservations@hilton.com www.hilton.com/en/hotels/midvmqq-villa-mercedes-merida/ +-52-999-942-9000 Av. Colón 500, Centro, 97000 Mérida, Yuc., Mexico Rosas & Xocolate Código: Camila&Daniel2023 Email: frontdesk@rosasandxocolate.com www.rosasandxocolate.com +52-999-924-2992 Paseo de Montejo 480, Zona Paseo Montejo, Centro, Mérida, Yucatán 97000 Holiday Inn Mérida Código: BCD www.ihg.com/holidayinn/hotels/us/en/merida/midmx/hoteldetail +52-9999-42-8800--635--626 Av. Colón 498, entre Paseo Montejo Y Calle 60, Zona Paseo Montejo, Centro, 97000 Mérida, Yuc., Mexico Hotel NH Collection Mérida Código: 2200682701 Email: reservas.ame@nh-hotels.com *Note: We heard recently this hotel overbooked on a wedding weekend and cancelled reservations at the last minute, just something to keep in mind. www.nh-hotels.com/b2b-ccg/c4456bfe613b3dfeb49de341f2ac468e +52-55-30-98-76-46 C. 60 346, Zona Paseo Montejo, Centro, 97000 Mérida, Yuc., Mexico What are other recommended activities around the area? Food Guide (some places require reservations) Tho Aperitivo | Breakfast Justo Bread | Breakfast Merci | Breakfast Rosas & Xocolate | Breakfast - Lunch - Dinner La Libertad | Breakfast Pan & Kof.feé | Breakfast Cuna Mérida | Breakfast Volta Café Santa Lucía | Breakfast Cigno | Breakfast - Lunch Teya Santa Lucia | Lunch Mugy | Lunch - Dinner Micaela Mar y Leña | Lunch - Dinner Crabster | Lunch - Dinner Ramiro Cocina | Lunch - Dinner Almadía | Lunch - Dinner Elio Al Mare | Lunch - Dinner Holoch | Lunch - Dinner Arcano | Lunch - Dinner Picheta | Lunch - Dinner Intimo | Lunch - Dinner Emplumado | Lunch - Dinner Maria Raiz Y Tierra | Lunch - Dinner Oliva | Lunch - Dinner Homu | Lunch - Dinner Néctar | Lunch - Dinner K’u’uk | Lunch - Dinner Kii’wik | Breakfast La Tradición | Lunch La Chaya Maya | Lunch - Dinner Helados Colón | Ice Cream & Desserts Ixi’im | Lunch - Dinner | Located a 50 min drive outside the city in a luxury hotel. Bar Guide El Lagarto de Oro Salón Gallos El Remate de Montejo Ignoto La Negrita Catrin Flamel Bar Murcielago Places to See Outside the City Cenote Mucuyche | 1 hour Cenote San Ignacio | 45 min Chichén Itzá | Pyramids | 1.5 hours Uxmal | Pyramids | 1 hour Valladolid | Town | 2.5 hours Izamal | Town | 1.5 hours Sisal | Beach | 1 hour Progreso | Beach | 30 min Hacienda Viva Sotuta de Peon | Henequén Tours & a Restaurant | 50 min How should guests confirm their attendance? https://withjoy.com/camilaydaniel/rsvp How can guests cancel their attendance? https://withjoy.com/camilaydaniel/rsvp What is the agenda for the event? Golf tournament October 13 at 9am October 13 at 2pm El jaguar golf club Please arrange your own transportation There is parking Golf attire Same hotels Welcome cocktail October 13 at 7pm October 13 at 9pm MUGY Please arrange your own transportation There is no parking Casual attire Same hotels Wedding October 14 at 4:30pm October 15 at 2:00am Haciendo Chichí Suarez There will be transportation provided to the hacienda and back from the Wayam and the Courtyard Hotels. Final schedule will be defined closer to the date. There is no parking Women: Formal Jardín | Men: Guayabera Same hotels
'''

event_system_messages = '''
You are a helpful coordinator for an event. You help people assisting the event or planning the event know where they need to be, what they need to be prepared, what is important to know, and anything that they might require related to the event.
This is the event information:
{}
Answer the following question based on the information above. If the answer is not provided in the information above, give a logical answer without being too specific.
QUESTION: {}
ANSWER:
'''


class EventAgent():


    def say_hello(self):
        prompt = "Say hello in a random and fun way"
        print(llm(prompt))

    def connect_chatgpt(self, user_input):
        print(llm(user_input))

    def create_prompt(self, user_input):
        return event_system_messages.format(event_context, user_input)
    
    def answer_event_FAQs(self, user_input):
        prompt = self.create_prompt(user_input)
        print(llm(prompt))