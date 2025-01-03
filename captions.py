import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=gemini_api_key)


def generate_captions(heading, description):
  generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
  }

  model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    # safety_settings = Adjust safety settings
    # See https://ai.google.dev/gemini-api/docs/safety-settings
  )

  response = model.generate_content([
    "input: Playgroup Cocomelons | Body Painting Activity",
    "output: Play Group Cocomelons are getting colorful with a fun body painting activity!🎨🧑‍🎨 Our little artists are exploring their creativity while learning about colors and shapes in a playful way.",
    "input: Playgroup Cocomelons | Learn about Body Parts",
    "output: Play Group Cocomelons are learning about body parts by making faces!🌝🖍️ Our little learners are having a blast discovering different features while getting creative with their art.",
    "input: KG2 Ocean | Introducing letter \"d\"",
    "output: KG 2 Ocean is diving into the world of lowercase letter \"d\"!🦖  Our little explorers are having a blast discovering the letter d through fun activities and playful learning.",
    "input: KG1 Spiderman | Learning Their Age",
    "output: KG 1 Spider-Man Class is learning about how old they are as part of the topic 'All About Me'! 📅⌛ Our little learners are excited to share their ages while exploring their identities and celebrating individuality.",
    "input: KG1 Spiderman | Hand Prints",
    "output: KG 1 Spider-Man Class is sharing 'This is my handprint'🖐️🤗 as part of the topic 'All About Me'! Our little learners are expressing themselves creatively while exploring their identities.",
    "input: KG1 Superman | Fingerprint Name Craft",
    "output: KG 1 Super-Man Class is getting creative by putting their fingerprints on top of their names! 👆 Our little artists are having fun personalizing their work while exploring their creativity.",
    "input: KG2 Orbiters | Learning Uppercase \"C\"",
    "output: KG 2 Orbiters are crunching into learning with uppercase C!🥕🔤  Our little learners are discovering that C is for Carrot through fun and engaging activities.",
    "input: KG2 Orbiters | Introducing Lowercase \"b\"",
    "output: KG 2 Orbiters are fluttering into learning with lowercase b! 🔤🔤\nOur little ones are discovering that b is for bat through exciting activities and playful learning.",
    "input: Playgroup Cocomelons | Leaning Number 1",
    "output: Play Group Cocomelons are learning all about the number one! 1️⃣🥇🔢Our little learners are having fun exploring and recognizing the number one through interactive activities and play.",
    "input: Bridge Class | Recycling Lesson",
    "output: Bridge Class is diving into a recycling lesson by sorting items into plastic, glass, metal, and paper! ♻️🍃 Our young learners are understanding the importance of recycling and how to take care of the environment in a fun and educational way.",
    "input: Playgroup Cocomelons | Learning Red Color",
    "output: Play Group Cocomelons are learning about the color red by making strawberries using their handprints! 🍓👋✨ Our little artists are having so much fun exploring colors through this creative activity.",
    "input: Playgroup Cocomelons | Practicing their Names",
    "output: Play Group Cocomelons are practicing to tell their names by pasting papers on the first letter of their names! ✨🖍️ Our little learners are enjoying this interactive activity while getting familiar with their initials. .",
    "input: Playgroup Cocomelons | First Day Craft",
    "output: Play Group Cocomelons are celebrating their first day of school with a special craft activity! 🎨✨ Our little ones are creating fun and colorful crafts to mark this exciting milestone.",
    "input: Playgroup | Introducing Body Parts",
    "output: Play Group is exploring the fascinating world of body parts! 🦵🖐️✨ Our little learners are having a blast discovering and naming their body parts through interactive activities and fun games. .",
    "input: KG 1 | Making a bunny",
    "output: KG 1 is getting creative by making a bunny using circles! 🐰🔵✨ Our little artists are enjoying this fun activity that combines creativity and shape recognition.",
    "input: KG 1 | Introducing Number 2",
    "output: KG 1 is excited to explore the number 2! ✌️✨ Our little learners are engaging in fun activities to understand the concept of 'two' through play and exploration.",
    "input: KG 1 | First letter of your Name",
    "output: KG 1 is having a colorful time painting the first letter of their names! 🎨✨ Our little artists are exploring creativity while learning to recognize their initials.",
    "input: KG1 | Collecting Trash",
    "output: KG 1 is engaging in the 'Collecting Trash' activity to learn about protecting the environment! 🌍♻️✨ Our little eco-warriors are excited to contribute to a cleaner planet while having fun outdoors.",
    "input: KG 1 | Number 1 Craft",
    "output: KG 1 is enhancing their fine motor skills with a fun number one craft! 🍎✨ Our little ones are pasting torn pieces on the apple to learn all about the number one through this hands-on activity.",
    "input: KG2 Ocean | Learning Uppercase \"A\"",
    "output: KG2 Ocean is diving into learning with uppercase A! 🅰️🌊 Our little explorers are having a blast discovering the letter A through fun and creative activities.",
    "input: "+heading+" | "+description,
    "output: ",
  ])

  tail = '''
.
.
.
.
Contact us : ￼076 947 6534
Early Birds Child Care,
Branches : Karapitiya | Hikkaduwa
.
.
#earlybirdschildcare #earlybirds #storyofearlybirds  #galle #children #childcare #montessori'''

  caption = response.text + tail

  return caption



