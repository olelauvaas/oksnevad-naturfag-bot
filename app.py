import streamlit as st
from openai import OpenAI

# 🔐 Sett opp API-nøkkel (bruk st.secrets eller hardkod forsiktig under testing)
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# 🎭 Systemrolle – lagd for naturfag
systemrolle = (
    "Du er en inspirerende og kunnskapsrik naturfaglærer på videregående skole. "
    "Du gjør naturfag lett å forstå ved å bruke metaforer, analogier og hverdagsbilder. "
    "Du forklarer dette på en meget enkel måte som passer for ungdom på 16 år."
    "Du snakker varmt, engasjert og med glimt i øyet. Svar tydelig og forklar gjerne i punktform når det passer."
)

# 🖼️ Streamlit-grensesnitt
st.title("🔬 Naturfag GPT – Øksnevad")

spørsmål = st.text_input("Still et spørsmål om naturfag:")

if spørsmål:
    with st.spinner("Tenker litt..."):
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": systemrolle},
                {"role": "user", "content": spørsmål}
            ]
        )
        svar = response.choices[0].message.content
        st.markdown(svar)