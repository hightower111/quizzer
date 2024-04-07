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

st.write('level 3 The final level')
counter = 0

genre = st.radio(
    "What is the Riemann hypothesis?",
    ["A conjecture about the distribution of prime numbers", "A proof of the Goldbach conjecture", "A theorem about elliptic curves"],
    key="riemann_hypothesis"
)

if genre == "A conjecture about the distribution of prime numbers":
    counter += 1

genre = st.radio(
    "Who proved Fermat's Last Theorem?",
    ["Pierre de Fermat", "Andrew Wiles", "Carl Friedrich Gauss"],
    key="fermats_last_theorem"
)
if genre == "Andrew Wiles":
    counter += 1

genre = st.radio(
    "What is the chemical symbol for the element einsteinium?",
    ["Es", "Ei", "Em"],
    key="einsteinium_symbol"
)
if genre == "Es":
    counter += 1

genre = st.radio(
    "What is the Hardy-Weinberg equilibrium?",
    ["A law in thermodynamics", "A principle in population genetics", "An equation in quantum mechanics"],
    key="hardy_weinberg_equilibrium",
)
if genre == "A principle in population genetics":
    counter += 1

genre = st.radio(
    "What is the mass of the Higgs boson particle?",
    ["About 125 GeV/c^2", "About 1 MeV/c^2", "About 3 TeV/c^2"],
    key="higgs_boson_mass",
)
if genre == "About 125 GeV/c^2":
    counter += 1

genre = st.radio(
    "Who formulated the general theory of relativity?",
    ["Albert Einstein", "Isaac Newton", "Stephen Hawking"],
    key="general_relativity",
)
if genre == "Albert Einstein":
    counter += 1

genre = st.radio(
    "What is the chemical formula for dimethyl sulfoxide?",
    ["C6H12O6", "C2H6OS", "C3H8O3"],
    key="dimethyl_sulfoxide_formula",
)
if genre == "C2H6OS":
    counter += 1

genre = st.radio(
    "What is the name of the largest known prime number?",
    ["Mersenne prime", "Fermat prime", "Gaussian prime"],
    key="largest_prime",
)
if genre == "Mersenne prime":
    counter += 1

genre = st.radio(
    "Who proposed the wave-particle duality of light?",
    ["Albert Einstein", "Max Planck", "Louis de Broglie"],
    key="wave_particle_duality",
)
if genre == "Louis de Broglie":
    counter += 1

genre = st.radio(
    "What is the chemical symbol for the element darmstadtium?",
    ["Du", "Ds", "Dt"],
    key="darmstadtium_symbol",
)
if genre == "Ds":
    counter += 1

genre = st.radio(
    "Who discovered the structure of DNA?",
    ["Rosalind Franklin", "Gregor Mendel", "James Watson and Francis Crick"],
    key="dna_structure",
)
if genre == "James Watson and Francis Crick":
    counter += 1

score = st.button("Submit", type="primary")

if score:
    st.write(f"You have done well, young scholar! You have gotten {counter}/11 correct.")
if counter > 10:
    st.balloons()

