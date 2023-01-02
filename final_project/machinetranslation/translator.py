import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from dotenv import load_dotenv

load_dotenv()

apikey = os.environ["apikey"]
url = os.environ["url"]

# task 9 - translator_instance
authenticator = IAMAuthenticator(apikey)
translator = LanguageTranslatorV3(
    version="2018-05-01", authenticator=authenticator
)

translator.set_service_url(url)

# task 10 - e2f_translator_function
def english_to_french(english_text):
    if english_text is None or len(english_text) == 0:
        return None
    translations = translator.translate(
        text=english_text, model_id="en-fr"
    ).get_result()
    # write the code here
    return translations.get("translations")[0].get("translation")


# task 11 - f2e_translator_function
def french_to_english(french_text):
    if french_text is None or len(french_text) == 0:
        return None
    translations = translator.translate(
        text=french_text, model_id="fr-en"
    ).get_result()
    return translations.get("translations")[0].get("translation")
