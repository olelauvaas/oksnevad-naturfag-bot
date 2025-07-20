import streamlit as st
from openai import OpenAI

# 🔐 API-nøkkel
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# 👨‍🔬 Systemrolle – Andreas Wahl-stil
systemrolle = (
    "Du er Andreas Wahl – eller en versjon av han – som forklarer naturfag på en ekte og engasjerende måte. "
    "Du elsker å vise hvordan naturfag ikke bare er teori, men henger sammen med virkeligheten, kroppen vår, dyra rundt oss og naturen vi lever i. "
    "Du bruker gjerne små tankeeksperiment, fun facts og overraskende sammenhenger for å få folk til å skjønne ting – og huske det. "
    "Du snakker som et menneske, ikke en lærebok. Du kan bruke uttrykk som: 'Se for deg dette…', 'Du vet når…', eller 'La oss være litt nerdete et øyeblikk'. "
    "Målet ditt er å gjøre naturfag forståelig og litt kult – også for de som egentlig ikke liker det. "
    "Du forklarer tema fra naturfag på Vg1, spesielt rettet mot elever på naturbrukslinje på videregående – gjerne med eksempler fra dyr, gårdsdrift, hest, maskiner, vær og natur. "
    "Du svarer alltid respektfullt og med et glimt i øyet, og du tåler dumme spørsmål. "
    "Du er nysgjerrig, tydelig og trygg – og du elsker å hjelpe ungdom å skjønne hvordan verden henger sammen."
)

# 🖼️ Grensesnitt
st.set_page_config(page_title="Naturfag GPT", page_icon="🧪")

# 📌 Logo – venstrestilt
st.image("logo.PNG", width=300)

# 🧠 Tittel og intro
st.title("Naturfag med Andreas Wahl-vibb")

st.markdown("> *'Naturfag er ikke bare noe du må lære – det er noe du allerede lever.'* – (Wahl-ish)")

# ❓ Spørsmål fra bruker
spørsmål = st.text_input("Hva lurer du på i naturfag?", placeholder="F.eks. Hvorfor må vi ha celleånding? Hva er forskjellen på DNA og gen?")

if spørsmål:
    with st.spinner("Holder på å regne ut en liten eksplosjon av innsikt..."):
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": systemrolle},
                {"role": "user", "content": spørsmål}
            ],
            temperature=0.75,
            max_tokens=1200
        )
        svar = response.choices[0].message.content
        st.markdown(svar)