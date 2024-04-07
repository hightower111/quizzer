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


st.write('level 2')
counter = 0

genre = st.radio(
    "What is the largest known prime number?",
    ["Mersenne prime", "Fermat prime", "Gaussian prime"],
    key="prime_number"
)

if genre == "Mersenne prime":
    counter += 1

genre = st.radio(
    "Which element has the highest melting point?",
    ["Tungsten", "Carbon", "Rhenium"],
    key="melting_point"
)
if genre == "Tungsten":
    counter += 1

genre = st.radio(
    "What is the speed of light in a vacuum (meters per second)?",
    ["299,792,458 m/s", "300,000,000 m/s", "280,000,000 m/s"],
    key="speed_of_light"
)
if genre == "299,792,458 m/s":
    counter += 1

genre = st.radio(
    "Who formulated the law of general relativity?",
    ["Albert Einstein", "Isaac Newton", "Stephen Hawking"],
    key="general_relativity",
)
if genre == "Albert Einstein":
    counter += 1

genre = st.radio(
    "Which of these animals is not a mammal?",
    ["Platypus", "Armadillo", "Kangaroo"],
    key="mammal",
)
if genre == "Platypus":
    counter += 1

genre = st.radio(
    "What is the chemical formula for caffeine?",
    ["C8H10N4O2", "C6H12O6", "CH4"],
    key="caffeine",
)
if genre == "C8H10N4O2":
    counter += 1

genre = st.radio(
    "What is the boiling point of liquid nitrogen in Celsius?",
    ["-196°C", "-210°C", "-180°C"],
    key="boiling_point_nitrogen",
)
if genre == "-196°C":
    counter += 1

genre = st.radio(
    "Who proposed the theory of evolution by natural selection?",
    ["Charles Darwin", "Gregor Mendel", "Jean-Baptiste Lamarck"],
    key="evolution_theory",
)
if genre == "Charles Darwin":
    counter += 1

genre = st.radio(
    "What is the chemical symbol for gold?",
    ["Au", "Ag", "Fe"],
    key="gold_symbol",
)
if genre == "Au":
    counter += 1

genre = st.radio(
    "What is the most abundant gas in Earth's atmosphere?",
    ["Nitrogen", "Oxygen", "Carbon dioxide"],
    key="atmosphere_gas",
)
if genre == "Nitrogen":
    counter += 1


score = st.button("Submit", type="primary")

if score:
    if counter>7:
        st.switch_page("pages/903944.py")
    else:
        st.write(f"You have done well young traveller, but you have gotten {counter}/10 and the pass mark was 7/10")
        