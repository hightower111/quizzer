import streamlit as st

st.set_page_config(initial_sidebar_state='collapsed')

st.markdown(
    '''
<style>
    [data-testid='collapsedControl'] {
        display: none
    }
</style>
    ''',
    unsafe_allow_html = True
)

counter = 0
genre = st.radio(
   "what is the average amount of cups of coffee drank every day in the US",
    ["1 :coffee:", "2 :coffee:", "3 :coffee:"],
    key="coffe"
)

if genre == "3 :coffee:":
    counter+=1

genre = st.radio(
   "What is the capital of France?",
    ["London","Paris", "Berlin"],
    key="capital"
)
if genre == "Paris":
    counter += 1

genre = st.radio(
   "What is the largest planet in our solar system?",
    ["Jupiter", "Saturn", "Neptune"],
    key="planet"
)
if genre == "Jupiter":
    counter += 1


genre = st.radio(
   "How many continents are there in the world?",
    ["5", "8", "7"],
    key="continents",
)
if genre == "7":
    counter += 1

genre = st.radio(
   "What is the chemical symbol for water?",
    ["CO2","H2O", "O2"],
    key="water",
)
if genre == "H2O":
    counter += 1

genre = st.radio(
   "Who wrote 'Romeo and Juliet'?",
    [ "Jane Austen", "Charles Dickens","William Shakespeare"],
    key="Romeo and Juliet",
)
if genre == "William Shakespeare":
    counter += 1


genre = st.radio(
   "What is the largest ocean on Earth?",
    ["Pacific Ocean", "Atlantic Ocean", "Indian Ocean"],
    key="ocean",
)
if genre == "Pacific Ocean":
    counter += 1


genre = st.radio(
   "What is the boiling point of water in Celsius?",
    ["100°C", "0°C", "50°C"],
    key="boiling point",
)
if genre == "100°C":
    counter += 1


genre = st.radio(
   "What is the closest planet to the Sun?",
    ["Mercury", "Venus", "Mars"],
    key="closest planet",
)
if genre == "Mercury":
    counter += 1



score = st.button("Submit", type="primary")

if score:
    if counter>7:
        st.switch_page("pages/7834783.py")
    else:
        st.write(f"You have done well young traveller, but you have gotten {counter}/10 and the pass mark was 7/10")
        